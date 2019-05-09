from django.shortcuts import render
from django.http  import HttpResponse

def login(request):
    return render(request, 'login/login.html')

def lockscreen(request):
    return render(request, 'login/lockscreen.html')
# Create your views here.
