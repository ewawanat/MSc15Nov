from django import forms
from django.forms.widgets import DateInput
from . import models
import datetime
from django.core.validators import MaxValueValidator

class DateInput(forms.DateInput):
    input_type = 'date'

class EnterData(forms.ModelForm):
    date_seen = forms.DateField(widget = DateInput, validators = [MaxValueValidator(datetime.date.today)])

    class Meta:
        model = models.Sighting
        fields = ['species', 'date_seen', 'photo', 'in_country', 'in_county' ]

