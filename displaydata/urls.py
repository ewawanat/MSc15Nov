from django.urls import path
from . import views

app_name = 'displaydata'

urlpatterns = [
    path('', views.displayData, name = 'displaydata'),
]