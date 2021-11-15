
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'birdapp.settings')

import django
django.setup()
from enterdata.models import Sighting

def populate():
    sighting_list = [
    {
  'species': 'Black-necked Grebe',
  'date_seen': '2018-01-06',
  'in_country': 'England',
  'in_county': 'York',
  'birder': 1,
}]

    for sighting in sighting_list:
        add_sighting(sighting['species'], sighting['date_seen'], sighting['in_country'], sighting['in_county'], sighting['birder'])

def add_sighting(species, date_seen, in_country, in_county, birder):
    s = Sighting.objects.get_or_create(species = species, 
                                        date_seen = date_seen,
                                        in_country = in_country,
                                        in_county = in_county, 
                                        birder = birder)[0]
    s.species = species
    s.date_seen = date_seen
    s.in_country = in_country
    s.in_county = in_county
    s.birder = birder
    s.save()
    return s

if __name__ == '__main__':
    print('Starting population script...')
    populate()
