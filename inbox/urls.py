from django.urls import path
from . import views

urlpatterns = [
    path('', views.mail_box, name='Mailbox'),
    path('compose/', views.compose, name='Compose'),
    path('read-mail/', views.read_mail, name='Mailbox'),
]
