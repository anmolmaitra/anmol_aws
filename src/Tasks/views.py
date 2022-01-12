from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse

from .forms import TaskForm
from django.views.generic import (
ListView,
CreateView,
UpdateView,
DeleteView
)

from .models import Tasks, TaskCategory

class TaskCreateView(CreateView):
    template_name = 'task_create.html'
    form_class = TaskForm
    queryset = Tasks.objects.all()

class TaskUpdateView(UpdateView):
    template_name = 'task_create.html'
    form_class = TaskForm
    queryset = Tasks.objects.all()

    def get_success_url(self):
        return '/task_list?taskCatVal='+self.kwargs['selectedDD']


class TaskListView(LoginRequiredMixin, ListView):
    login_url = '../login/'
    redirect_field_name = 'redirect_to'
    queryset = Tasks.objects.all()

    def get_queryset(self):
        result = Tasks.objects.all()
        cat_filter = self.request.GET.get('taskCatVal')
        print('cat_filter',cat_filter)
        if cat_filter  is not None:
            task_cat = TaskCategory.objects.get(id=cat_filter)
            if task_cat.categoryName != "ALL":
                result = Tasks.objects.filter(category=cat_filter)
        return result

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['taskCategory'] = TaskCategory.objects.all()
        context['selectedDD'] = self.request.GET.get('taskCatVal')
        print(context['selectedDD'])
        return context


class TaskDeleteView(DeleteView):
    template_name = 'tasks/task_delete.html'
    form_class = TaskForm
    queryset = Tasks.objects.all()

    def get_success_url(self):
        return '/task_list?taskCatVal='+self.kwargs['selectedDD']

