"""schoolportal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', include('login.urls')),
    path('profile/', include('userprofile.urls')),
    path('lockscreen/', include('lockscreen.urls')),
    path('classes/', include('classes.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('calendar/', include('calendar1.urls')),
    path('mailbox/', include('inbox.urls')),
    path('newsfeed/', include('newsfeed.urls')),
    path('admin_classes/', include('manageClasses.urls')),
    path('admin_reports/', include('manageReports.urls')),
    path('admin_schedule/', include('manageSchedule.urls')),
    path('admin_students/', include('manageStudents.urls')),
    path('admin_teachers/', include('manageTeachers.urls')),
]
