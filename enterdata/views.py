from django import forms
from django.shortcuts import redirect, render
from .models import County, Species
from django.contrib.auth.decorators import login_required
from . import forms
from django.http.response import JsonResponse

@login_required(login_url="/accounts/login/") #this is so that the user can only add data if they are logged in, if not logged in, redirect to login page
def enterdata(request): 
    #species = Species.objects.all().order_by('name')
    
    if request.method == 'POST':
        form = forms.EnterData(request.POST, request.FILES) #to validate the data against the model form
        #to check if the user entered data properly: 
        if form.is_valid():
            #save the data to the database:
            instance_of_data_entry = form.save(commit=False) #created an instance of an article but don't commit to saving it yet
            instance_of_data_entry.user = request.user # to associate the person who collected the data with the logged in user   
            instance_of_data_entry.save()
            #redirect to somewhere
            return redirect('enterdata:submitted')
    else:
        form = forms.EnterData()
    return render(request, 'enterdata/enterdata.html', {'form':form}) 
    # add {'species':species} if want list of species on the page
        
#@login_required(login_url="/accounts/login/") #this is so that the user can only add data if they are logged in, if not logged in, redirect to login page
def submitted(request):
    return render(request, 'enterdata/submitted.html')

# AJAX
def load_counties(request):
    # print("we are here!")
    country_id = request.GET.get('country_id')
    # print(country_id) 
    counties = County.objects.filter(in_country_id=country_id).all()
    # print(counties)
    
    # print(JsonResponse(list(counties.values('in_country', 'name')), safe=False))
    return JsonResponse(list(counties.values('in_country', 'name')), safe=False)
   # return render(request, 'enterdata/county_dropdown_list_options.html', {'counties': counties})

