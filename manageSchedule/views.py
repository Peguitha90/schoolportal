from django.shortcuts import render
from django.http  import HttpResponse

def manageSchedule(request):
    return render(request, 'manageSchedule/manageSchedule.html')

# def dashboard(request):
#    return render(request, 'userprofile/dashboard.html')
# Create your views here.
