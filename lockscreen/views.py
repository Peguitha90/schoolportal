from django.shortcuts import render
from django.http  import HttpResponse

def lockscreen(request):
     return render(request, 'lockscreen/lockscreen.html')
# Create your views here.
