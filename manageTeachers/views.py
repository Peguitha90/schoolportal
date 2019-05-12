from django.shortcuts import render
from django.http  import HttpResponse

def manageTeachers(request):
    return render(request, 'manageTeachers/manageTeachers.html')

# def dashboard(request):
#    return render(request, 'userprofile/dashboard.html')
# Create your views here.
