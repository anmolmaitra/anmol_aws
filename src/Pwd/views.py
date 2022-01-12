from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Pwd

# Create your views here.
@login_required(login_url='../login/')
def pwd_list_view(request):
    queryset = Pwd.objects.all()
    context = {
        "object_list": queryset
    }
    return render(request, "pwd_list.html", context)
