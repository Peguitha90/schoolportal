from django.shortcuts import render
from django.http  import HttpResponse

def profile(request):
    return render(request, 'userprofile/userprofile.html')

# Create your views here.
