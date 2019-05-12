from django.shortcuts import render
from django.http  import HttpResponse

def manageClasses(request):
    return render(request, 'manageClasses/manageClasses.html')

# def dashboard(request):
#    return render(request, 'userprofile/dashboard.html')
# Create your views here.
