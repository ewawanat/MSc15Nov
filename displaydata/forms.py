from django import forms

from enterdata.models import County, Species
from enterdata.views import enterdata
from . import models

class DateInput(forms.DateInput):
    input_type = 'date'

# class SpeciesMultipleChoiceForm(forms.Form):
#     species_select = forms.ModelMultipleChoiceField(queryset=Species.objects.values_list('name'))
    
class DisplayData(forms.ModelForm):
    from_date = forms.DateField(widget= DateInput)
    to_date = forms.DateField(widget= DateInput)
    # species_name = forms.MultipleChoiceField(Species.objects.values('name'))

    class Meta:
        model = models.DisplayForm
        fields = ['species_name', 'in_country', 'in_county', 'from_date', 'to_date']

