from django.urls import path
from . import views

urlpatterns = [
    path('', views.manageSchedule, name='ManageSchedule'),
]
