from django.urls import path
from . import views

app_name = 'enterdata'

urlpatterns = [
    path('', views.enterdata, name = 'enterdata'),
    path('submitted', views.submitted, name = 'submitted'),

    path('load_counties', views.load_counties, name ='ajax_load_counties')
]