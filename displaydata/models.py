from django.db import models
from django.db.models.base import Model
from django.contrib.auth.models import User
from django.db.models.deletion import PROTECT
from enterdata.models import Country, County, Species

class DisplayForm(models.Model):
    species_name = models.ForeignKey(Species, on_delete=PROTECT)
    in_country = models.ForeignKey(Country, on_delete=PROTECT)
    in_county = models.ForeignKey(County, on_delete=PROTECT)
    from_date = models.DateField()
    to_date = models.DateField()
    birder = models.ForeignKey(User, on_delete=PROTECT, default=None)

    def __str__(self): 
        return self.species_name  #function to return the name of the instance of DisplayForm