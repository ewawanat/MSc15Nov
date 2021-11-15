import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'birdapp.settings')

import django
django.setup()
from enterdata.models import Sighting

def add_sighting(species_name, in_country,in_county, from_date, to_date, birder):
    s = Sighting.objects.get_or_create()