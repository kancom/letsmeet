from crispy_forms.bootstrap import Div, FormActions
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Button, Fieldset, Layout, Submit
from dateutil import parser as du_parser
from django import forms
from django.forms.fields import DateTimeField
from django.shortcuts import get_object_or_404
from django.utils.translation import gettext_lazy as _
from django.views.generic.edit import CreateView, UpdateView
from mapwidgets.widgets import GooglePointFieldWidget
from tempus_dominus.widgets import DateTimePicker

from letsmeet import utils
from meetpage.models import Appointment, ShortCut

GooglePointFieldWidget.template_name = 'google-point-field-widget.html'


class CustomDateTimeField(DateTimeField):
    def to_python(self, value):
        value = du_parser.parse(value)
        return super().to_python(value)


class DetailForm(forms.ModelForm):
    datetime = CustomDateTimeField(
        label=_('Date and time'),
        help_text=_('Date and time of the appointment'),
        widget=DateTimePicker(
            options={
                # 'useCurrent': True,
                # 'inline': True,
                # 'allowInputToggle': True,
                'collapse': False,
            },
            attrs={
                'append': 'fa fa-calendar',
                'icon_toggle': True,
                'input_toggle': False,
            }))

    class Meta:
        model = Appointment
        fields = (
            'name',
            'description',
            'datetime',
            'place',
        )
        context_object_name = "app_details"

        widgets = {
            # 'datetime':
            # DateTimePicker(
            #     options={
            #         # 'useCurrent': True,
            #         # 'inline': True,
            #         # 'allowInputToggle': True,
            #         'collapse': False,
            #     },
            #     attrs={
            #         'append': 'fa fa-calendar',
            #         'icon_toggle': True,
            #         'input_toggle': False,
            #     }),
            'place': GooglePointFieldWidget,
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.include_media = False
        self.helper.form_class = 'form-horizontal container-fluid'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-8'
        self.helper.layout = Layout(
            Fieldset(_('Short description'), 'name', 'description'),
            Fieldset(
                _('When and where?'),
                'datetime',
                # Div(
                #     FieldWithButtons(
                #         Field('datetime',
                #               css_class='datetimepicker-input',
                #               data_target="#datetimepicker1",
                #               wrapper_class='date'),
                #         Div(Div(css_class='input-group-text fa fa-calendar'),
                #             css_class='input-group-append',
                #             data_target="#datetimepicker1",
                #             data_toggle="datetimepicker"),
                #         data_toggle="datetimepicker",
                #         id='datetimepicker1',
                #         data_target_input="nearest",
                #         css_class='input-group date'),
                #     # data_toggle="datetimepicker",
                #     # data_target="#datetimepicker1"),
                #     css_class='from-group row',
                #     id='div_id_datetime'),
                'place'),
            # https://stackoverflow.com/questions/37442706/copy-url-from-browser-using-clipboard-js
            FormActions(
                Submit('save', _('Save changes')),
                # Button('cancel', 'Cancel'),
                Button("copyurl", _("Copy to clipboard"))),
            Fieldset(
                _('Share via'),
                Div(id='sharevia',
                    css_class='ya-share2 ',
                    data_services="vkontakte,facebook,viber,whatsapp,telegram")
            ))


class AppointmentUpdate(UpdateView):
    form_class = DetailForm
    template_name = "templates/appointment_details.html"

    def get_object(self):
        shortcut = get_object_or_404(ShortCut, shortcut=self.kwargs['apnt_id'])
        return shortcut.appointment


class AppointmentCreate(CreateView):
    form_class = DetailForm
    template_name = "templates/appointment_details.html"

    def form_valid(self, form):
        self.object: Appointment = form.save()
        s = ShortCut(appointment=self.object,
                     shortcut=utils.get_url_shortcut(str(self.object.pk)))
        s.save()
        return super().form_valid(form)

    def get_success_url(self):
        return self.object.get_absolute_url()
