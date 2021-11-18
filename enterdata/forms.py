from django import forms
from django.forms.widgets import DateInput
from . import models


class DateInput(forms.DateInput):
    input_type = 'date'

class EnterData(forms.ModelForm):
    date_seen = forms.DateField(widget = DateInput)
    class Meta:
        model = models.Sighting
        fields = ['species', 'date_seen', 'photo', 'in_country', 'in_county' ]

    # def __init__(self, * args, **krwargs):
    #     super().__init__(* args, **krwargs)