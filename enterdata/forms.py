from django import forms
from django.forms.widgets import DateInput
from . import models


class DateInput(forms.DateInput):
    input_type = 'date'

class EnterData(forms.ModelForm):
    date_seen = forms.DateField(widget = DateInput)
    class Meta:
        model = models.Sighting
        fields = ['species', 'in_country', 'in_county', 'date_seen', 'photo']

    def __init__(self, * args, **krwargs):
        super().__init__(* args, **krwargs)
        self.fields['in_county'].queryset = models.County.objects.none()
        
        if 'in_country' in self.data:
            try:
                country_id = int(self.data.get('in_country'))
                self.fields['city'].queryset = models.County.objects.filter(country_id=country_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['in_county'].queryset = self.instance.country.county_set.order_by('name')