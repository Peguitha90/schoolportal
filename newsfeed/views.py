from django.shortcuts import render
from django.http  import HttpResponse

def newsfeed(request):
    return render(request, 'newsfeed/newsfeed.html')

# def dashboard(request):
#    return render(request, 'userprofile/dashboard.html')
# Create your views here.
