"""letsmeet URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import path

from meetpage.views import AppointmentCreate, AppointmentUpdate

urlpatterns = i18n_patterns(
    path('/lmeet/admin/', admin.site.urls),
    path('/lmeet/<slug:apnt_id>/',
         AppointmentUpdate.as_view(),
         name='appointment_details'),
    path('/lmeet', AppointmentCreate.as_view(), name='home'))
