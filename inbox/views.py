from django.shortcuts import render
from django.http  import HttpResponse

def mail_box(request):
    return render(request, 'inbox/mail_box.html')

def compose(request):
    return render(request, 'inbox/compose.html')

def read_mail(request):
    return render(request, 'inbox/read-mail.html')

# def dashboard(request):
#    return render(request, 'userprofile/dashboard.html')
# Create your views here.
