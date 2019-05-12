from django.shortcuts import render
from django.http  import HttpResponse

def classes(request):
    return render(request, 'classes/classes.html')

# def dashboard(request):
#    return render(request, 'userprofile/dashboard.html')
# Create your views here.
