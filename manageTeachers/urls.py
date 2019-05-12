from django.urls import path
from . import views

urlpatterns = [
    path('', views.manageTeachers, name='ManageTeachers'),
]
