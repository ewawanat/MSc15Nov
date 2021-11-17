from django.urls import path
from . import views

app_name = 'displaydata'

urlpatterns = [
    path('', views.displayData, name = 'displaydata'),
    path('load_counties', views.load_counties, name ='ajax_load_counties')
]