from django.contrib.gis.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class Appointment(models.Model):
    name = models.CharField(max_length=50,
                            verbose_name=_('Name'),
                            help_text=_('Name your appointment'))
    description = models.TextField(
        verbose_name=_('Description'),
        blank=True,
        help_text=_('Enter necessary details about your appointment'))
    datetime = models.DateTimeField(
        verbose_name=_('Date and time'),
        help_text=_('Date and time of the appointment'))
    place = models.PointField(verbose_name=_('Place'),
                              help_text=_('Place where meet'))

    def __repr__(self):
        return f"<{self.__class__.name}>: {self.name}, {self.datetime}"

    def get_absolute_url(self):
        s = ShortCut.objects.get(appointment=self)
        return reverse('home') + f"{s.shortcut}"


class ShortCut(models.Model):
    shortcut = models.CharField(max_length=50, unique=True)
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
