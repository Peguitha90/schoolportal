from django.shortcuts import render
from django.http  import HttpResponse

def calendar1(request):
    return render(request, 'calendar1/calendar.html')

# def dashboard(request):
#    return render(request, 'userprofile/dashboard.html')
# Create your views here.
