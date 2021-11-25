from django.forms.widgets import Select
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from enterdata.models import Country, County, Sighting, Species
from . import forms
import json
from django.http.response import HttpResponse, JsonResponse
import csv


@login_required(login_url="/accounts/login/") #this is so that the user can only add data if they are logged in, if not logged in, redirect to login page
def displayData(request):
    context_dict = {}
    display_form = forms.DisplayData()
    context_dict['form'] = display_form
    england = Country.objects.get(name = 'England')
    all_in_england = Sighting.objects.filter(in_country=england)

    if request.method == 'POST': 
        # print("request.POST:")
        # print(request.POST)
        # print("!!!! species_name printed:")
        # print(request.POST['species_name'])
        # print("getlist")
        # print(request.POST.getlist('species_name'))

        # print(request.POST.getlist('species_name')[0])
    

        selected_species = request.POST.getlist('species_name')
        country_selected = Country.objects.get(id=request.POST['in_country'])
        #county_selected = County.objects.filter(name__in=request.POST.getlist('in_county'))
        from_date_selected = request.POST['from_date']
        to_date_selected = request.POST['to_date']

        list_dict = [  
        ] #make an array 

        list_for_line_graph = [
            ]
            
        for each_species in selected_species:       # iterate over selected species
            result = Species.objects.get(id=each_species) # match the id with each of the species id
            all_sightings = Sighting.objects.filter(species = result) \
                .filter(in_country__in = request.POST.getlist('in_country')) \
                .filter(in_county__in = request.POST.getlist('in_county')) \
                .filter(date_seen__range = [from_date_selected, to_date_selected])
            # create an all_sightings varable which is filtered by the searched for data

            # print(all_sightings)

            
            for i in all_sightings:
                sightings_per_month = 0
                for j in all_sightings: 
                    if i.date_seen.month == j.date_seen.month: 
                        sightings_per_month +=1
                
                dict = {'species_name': i.species.name, 'frequency': sightings_per_month, 'month': i.date_seen.month}
                name_exists = False
                for name in list_for_line_graph: 
                    if len(list_for_line_graph)!=0:
                        if name["species_name"] == i.species.name and name["month"] == i.date_seen.month:
                            name_exists = True
                if name_exists == False:
                    list_for_line_graph.append(dict)
                
            for i in all_sightings: # looop over all the sightings 
                occurrence = 0 #start counting ocurrence of each sighting at 0
                for j in all_sightings: 
                    if i.species.name == j.species.name: #when the same species name is found
                        occurrence += 1 #add 1 to the occurrence 
                        
                dict = {'species_name': i.species.name, 'frequency': occurrence}  #create a dict with all species names and frequency of their occurrence       
                name_exists = False # set the name existing in the dictionary to false
                for name in list_dict: # loop over the names in the dictionary
                    if len(list_dict)!=0: # if the length of the dictionary is not 0
                        if name["species_name"] == i.species.name: #if the name of the species is equal to the one currently being looked at 
                            name_exists = True #set name_exists to true (name exists in the dictionary)
                if name_exists == False: #if name does not exist in the dictionary 
                    list_dict.append(dict) #append the name as a key to the dict


        # print(list_dict)
        print("line graph data:")
        print(list_for_line_graph)

        all_birds_sighted_json = json.dumps(list_dict) 
        context_dict['jsondata'] = all_birds_sighted_json
        # print(all_birds_sighted_json)
    return render(request, 'displaydata/displaydata.html', context = context_dict)

#AJAX Species.objects.get(id=each_species)
def load_counties(request):
    # print("we are here!")
    # print(request.GET)
    country_id = request.GET.getlist('country_id[]')
    # print(country_id) 

    counties = County.objects.filter(in_country_id__in=country_id).all()
    # print(counties)
    
    return JsonResponse(list(counties.values('in_country', 'name')), safe=False)


#to export data from Sightings table: 
def export(request):

    response = HttpResponse(content_type = 'text/csv')
    writer = csv.writer(response)
    writer.writerow(['Species name', 'Country', 'County', 'Date seen', 'birder ID'])

    for sighting in Sighting.objects.all().values_list('species__name', 'in_country__name', 'in_county', 'date_seen', 'birder'):
        writer.writerow(sighting)
    
    #to tell the browser what to do with the response: 
    response['Content-Disposition'] = 'attachment; filename="sightings.csv"'

    return response