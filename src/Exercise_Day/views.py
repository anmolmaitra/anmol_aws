from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from datetime import date

from .models import Exercise, Exercise_Category, Exercise_Day
from django.contrib.auth.decorators import login_required

from django.views.generic import (
ListView
)


class ExerciseDayListView(LoginRequiredMixin, ListView):
    login_url = '../login/'
    redirect_field_name = 'redirect_to'
    def dispatch(self, *args, **kwargs):
         requestId = self.request.GET.get('id')
         ids = self.request.GET.getlist('id')
         print("ids "+str(ids))
         if requestId is not None:
            for EdId in ids:
                record = Exercise_Day.objects.get(id=EdId)
                delOldEx = Exercise_Day.objects.filter(exercise__Exercise_Name=record.exercise.Exercise_Name).delete()
                record.id = None
                today = date.today()
                record.Ex_Date = today
                record.save()
            return HttpResponseRedirect("/exerciseday_list/?ExCatVal="+self.request.GET.get('ExCatVal'))
         return super().dispatch(*args, **kwargs)

    def get_queryset(self):
         result = Exercise_Day.objects.order_by('Ex_Date')
         ec_filter = self.request.GET.get('ExCatVal')

         if ec_filter is not None:
             selectedCat = Exercise_Category.objects.get(id=ec_filter)
             if selectedCat.Exercise_Cat != "ALL":
                result = Exercise_Day.objects.filter(exercise__Category=ec_filter).order_by('Ex_Date')
         return result

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print("Inside get_context_data")
        context['ExCategory'] = Exercise_Category.objects.all()
        context['selectedEC'] = self.request.GET.get('ExCatVal')
        return context

