from django.shortcuts import render
from django.http  import HttpResponse

def manageStudents(request):
    return render(request, 'manageStudents/manageStudents.html')

# def dashboard(request):
#    return render(request, 'userprofile/dashboard.html')
# Create your views here.
