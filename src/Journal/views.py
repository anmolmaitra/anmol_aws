from django.shortcuts import render
from .models import Journal

# Create your views here.
def journal_detail_view(request):
    obj = Journal.objects.filter(IsVisible='True').last()
    context = {
        'object': obj
    }
    return render(request, "detail.html", context)
