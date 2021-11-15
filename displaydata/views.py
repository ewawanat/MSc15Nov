from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from enterdata.models import Country, County, Sighting, Species
from . import forms
from django.shortcuts import HttpResponse
import json


@login_required(login_url="/accounts/login/") #this is so that the user can only add data if they are logged in, if not logged in, redirect to login page
def displayData(request):
    context_dict = {}
    display_form = forms.DisplayData()
    context_dict['form'] = display_form
    england = Country.objects.get(name = 'England')
    all_in_england = Sighting.objects.filter(in_country=england)

    if request.method == 'POST': 
        #print(request.POST['species_name'])
        species_selected_name = Species.objects.get(id=request.POST['species_name']).name
        #  print(species_selected_name)

        species_selected = Species.objects.get(id=request.POST['species_name'])
        country_selected = Country.objects.get(id=request.POST['in_country'])
        county_selected = County.objects.get(name=request.POST['in_county'])
        from_date_selected = request.POST['from_date']
        to_date_selected = request.POST['to_date']

        print( country_selected, county_selected, from_date_selected, to_date_selected)

      #  all_sightings = Sighting.objects.filter(species = species_selected) \

        all_sightings = Sighting.objects.filter(species = species_selected).filter(in_country = country_selected) \
            .filter(in_county = county_selected)

        print(all_sightings)

        list_dict = [  
        ]
        for i in all_sightings: 
            occurrence = 0
            for j in all_sightings: 
                if i.species.name == j.species.name: 
                    occurrence += 1
            dict = {'species_name': i.species.name, 'frequency': occurrence}        
            name_exists = False
            for name in list_dict: 
                if len(list_dict)!=0: 
                    if name["species_name"] == i.species.name:
                        name_exists = True
            if name_exists == False:
                list_dict.append(dict)

        print(list_dict)

        all_birds_sighted_json = json.dumps(list_dict)
        context_dict['jsondata'] = all_birds_sighted_json
        print(all_birds_sighted_json)
    return render(request, 'displaydata/displaydata.html', context = context_dict)