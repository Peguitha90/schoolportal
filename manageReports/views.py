from django.shortcuts import render
from django.http  import HttpResponse

def manageReports(request):
    return render(request, 'manageReports/manageReports.html')

# def dashboard(request):
#    return render(request, 'userprofile/dashboard.html')
# Create your views here.
