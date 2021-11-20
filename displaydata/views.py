from django.forms.widgets import Select
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from enterdata.models import Country, County, Sighting, Species
from . import forms
import json
from django.http.response import JsonResponse



@login_required(login_url="/accounts/login/") #this is so that the user can only add data if they are logged in, if not logged in, redirect to login page
def displayData(request):
    context_dict = {}
    display_form = forms.DisplayData()
    context_dict['form'] = display_form
    england = Country.objects.get(name = 'England')
    all_in_england = Sighting.objects.filter(in_country=england)

    if request.method == 'POST': 
        print("request.POST:")
        print(request.POST)
        print("!!!! species_name printed:")
        print(request.POST['species_name'])
        print("getlist")
        print(request.POST.getlist('species_name'))

        print(request.POST.getlist('species_name')[0])
        


        selected_species_list = []

        selected_species = request.POST.getlist('species_name')
        country_selected = Country.objects.get(id=request.POST['in_country'])
        county_selected = County.objects.filter(name__in=request.POST.getlist('in_county'))
        from_date_selected = request.POST['from_date']
        to_date_selected = request.POST['to_date']

        list_dict = [  
        ] #make an array 

        for each_species in selected_species:
            result = Species.objects.get(id=each_species)
            all_sightings = Sighting.objects.filter(species = result).filter(in_country = country_selected) \
                .filter(in_county__in = request.POST.getlist('in_county'))

            # print(all_sightings)

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

#AJAX
def load_counties(request):
    # print("we are here!")
    country_id = request.GET.get('country_id')
    # print(country_id) 
    counties = County.objects.filter(in_country_id=country_id).all()
    # print(counties)
    
    return JsonResponse(list(counties.values('in_country', 'name')), safe=False)
