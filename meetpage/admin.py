from django.contrib import admin
from django.contrib.gis.db import models
from mapwidgets.widgets import GooglePointFieldWidget

from meetpage.models import Appointment, ShortCut


class AppointmentAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.PointField: {
            "widget": GooglePointFieldWidget
        }
    }


admin.site.register(Appointment, AppointmentAdmin)
admin.site.register(ShortCut)
