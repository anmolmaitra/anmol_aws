from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
    return render(request, "home.html", {})

def login_view(request, *args, **kwargs):
    return render(request, "loginMessage.html", {})
