from django import forms
from . import models


class DateInput(forms.DateInput):
    input_type = 'date'

class DisplayData(forms.ModelForm):
    from_date = forms.DateField(widget= DateInput)
    to_date = forms.DateField(widget= DateInput)
    
    class Meta:
        model = models.DisplayForm
        fields = ['species_name', 'in_country', 'in_county', 'from_date', 'to_date']
