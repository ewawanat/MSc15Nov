from django import forms
from django.core import validators
from django.forms.widgets import DateInput
from . import models
import datetime
from django.core.validators import MaxValueValidator

class DateInput(forms.DateInput):
    input_type = 'date'

class EnterData(forms.ModelForm):
    date_seen = forms.DateField(widget = DateInput, validators = [MaxValueValidator(datetime.date.today)])

    # def clean_date(self):
    #     date_seen = self.cleaned_data['date_seen']
    #     if date_seen > datetime.date.today():
    #         raise forms.ValidationError("The date cannot be in the future")
    #     return date_seen

    class Meta:
        model = models.Sighting
        fields = ['species', 'date_seen', 'photo', 'in_country', 'in_county' ]

