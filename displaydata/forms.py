from django import forms
from django.db.models import query
from django.forms import widgets

from enterdata.models import County, Species
from enterdata.views import enterdata
from . import models


class DateInput(forms.DateInput):
    input_type = 'date'

class DisplayData(forms.ModelForm):
    from_date = forms.DateField(widget= DateInput)
    to_date = forms.DateField(widget= DateInput)
    
    class Meta:
        model = models.DisplayForm
        # species_name = forms.MultipleChoiceField(widget = forms.CheckboxSelectMultiple)
        fields = ['species_name', 'in_country', 'in_county', 'from_date', 'to_date']
