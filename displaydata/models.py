from django.db import models
from django.db.models.base import Model
from django.contrib.auth.models import User
from django.db.models.deletion import PROTECT
from django.db.models.fields.related import ForeignKey, ManyToManyField
from django.forms.fields import MultipleChoiceField
from enterdata.models import Country, County, Species
from enterdata.views import enterdata
from multiselectfield import MultiSelectField
from multiselectfield import MultiSelectFormField


class DisplayForm(models.Model):
    
    # species_set = species_name.objects.values_list('name')
   # species_name = models.ForeignKey(Species, on_delete=PROTECT)
   # MultiSelectField(Species, choices = SPECIES_CHOICES, on_delete=PROTECT)
    species_name = models.ManyToManyField(Species)
    in_country = models.ForeignKey(Country, on_delete=PROTECT)
    in_county = models.ForeignKey(County, on_delete=PROTECT, blank=True)
    from_date = models.DateField()
    to_date = models.DateField()
    birder = models.ForeignKey(User, on_delete=PROTECT, default=None)

    def __str__(self): 
        return self.species_name  #function to return the name of the instance of DisplayForm