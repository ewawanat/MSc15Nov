from django.db import models
from django.db.models.base import Model
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE, PROTECT
from datetime import date

class Country(models.Model):
    name = models.CharField(max_length=50)
    class Meta: 
        ordering = ['name']

    def __str__(self):
        return self.name
    
class County(models.Model):
    name = models.CharField(primary_key=True, max_length=50)
    in_country = models.ForeignKey(Country, default=1, max_length=50, on_delete=CASCADE)
    #postcode = models.CharField(max_length=50, blank = True)

    class Meta: 
        ordering = ['name']

    def __str__(self):
        return self.name
    
class Species(models.Model):
    name = models.CharField(max_length=30)

    class Meta: 
        ordering = ['name']

    def __str__(self): 
        return self.name  #function to return the name of the instance of Species
        
class Sighting(models.Model):
    species = models.ForeignKey(Species, default=None, on_delete=PROTECT)
    date_seen = models.DateField(default=date.today)
    photo = models.ImageField(default ='default.png', blank = True)
    in_country = models.ForeignKey(Country, default = None, on_delete = PROTECT)
    in_county = models.ForeignKey(County, default = None, on_delete = PROTECT)
    #sound_file = models.FileField(upload_to=/'sounds/')
    #class Meta:
    # db_table='Audio_store'
    #maybe later add user 
    birder = models.ForeignKey(User, default = None, on_delete = PROTECT)

    def __str__(self): 
        return self.species.name + " "  #function to return the name of the instance of Species