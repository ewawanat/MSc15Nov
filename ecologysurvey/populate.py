
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecologysurvey.settings')

import django
django.setup()
from enterdata.models import Sighting

def populate():
    sighting_list = [
    {
  'species': 'Black-necked Grebe',
  'date_seen': '01/06/2018',
  'in_country': 'England',
  'in_county': 'York',
  'birder': 'testuser1 ',

},
{
  'species': 'Slavonian Grebe ',
  'date_seen': '13/01/2020',
  'in_country': 'England',
  'in_county': 'York',
  'birder': 'testuser3 ',

},
{
  'species': 'Slavonian Grebe ',
  'date_seen': '25/08/2020',
  'in_country': 'England',
  'in_county': 'York',
  'birder': 'testuser1 ',

},
{
  'species': 'Black-necked Grebe',
  'date_seen': '22/10/2018',
  'in_country': 'England',
  'in_county': 'Wolverhampton ',
  'birder': 'testuser4',

},
{
  'species': 'Black-necked Grebe',
  'date_seen': '05/02/2019',
  'in_country': 'England',
  'in_county': 'York',
  'birder': 'testuser4',

},
{
  'species': 'Black-necked Grebe',
  'date_seen': '15/09/2018',
  'in_country': 'England',
  'in_county': 'Walsall ',
  'birder': 'testuser3 ',

},
{
  'species': 'Red-necked Grebe ',
  'date_seen': '16/11/2018',
  'in_country': 'England',
  'in_county': 'York',
  'birder': 'testuser1 ',

},
{
  'species': 'Slavonian Grebe ',
  'date_seen': '25/08/2019',
  'in_country': 'England',
  'in_county': 'York',
  'birder': 'testuser4',

},
{
  'species': 'Black-necked Grebe',
  'date_seen': '11/12/2020',
  'in_country': 'England',
  'in_county': 'Walsall ',
  'birder': 'testuser1 ',

},
{
  'species': 'Slavonian Grebe ',
  'date_seen': '25/01/2018',
  'in_country': 'England',
  'in_county': 'Wolverhampton ',
  'birder': 'testuser4',

},
{
  'species': 'Slavonian Grebe ',
  'date_seen': '09/10/2019',
  'in_country': 'England',
  'in_county': 'Walsall ',
  'birder': 'testuser4',

},
{
  'species': 'Pied-billed Grebe ',
  'date_seen': '14/08/2020',
  'in_country': 'England',
  'in_county': 'York',
  'birder': 'testuser4',

},
{
  'species': 'Black-necked Grebe',
  'date_seen': '25/06/2018',
  'in_country': 'England',
  'in_county': 'Wolverhampton ',
  'birder': 'testuser3 ',

},
{
  'species': 'Pied-billed Grebe ',
  'date_seen': '08/02/2018',
  'in_country': 'England',
  'in_county': 'York',
  'birder': 'testuser4',

},
{
  'species': 'Slavonian Grebe ',
  'date_seen': '23/11/2018',
  'in_country': 'England',
  'in_county': 'York',
  'birder': 'testuser2 ',

},
{
  'species': 'Little Grebe ',
  'date_seen': '24/01/2020',
  'in_country': 'England',
  'in_county': 'Walsall ',
  'birder': 'testuser3 ',

},
{
  'species': 'Pied-billed Grebe ',
  'date_seen': '19/04/2021',
  'in_country': 'England',
  'in_county': 'York',
  'birder': 'testuser1 ',

},
{
  'species': 'Slavonian Grebe ',
  'date_seen': '09/05/2020',
  'in_country': 'England',
  'in_county': 'Walsall ',
  'birder': 'testuser4',
},
{
  'species': 'Black-necked Grebe',
  'date_seen': '01/08/2018',
  'in_country': 'England',
  'in_county': 'York',
  'birder': 'testuser4',
},
{
  'species': 'Black-necked Grebe',
  'date_seen': '16/02/2019',
  'in_country': 'England',
  'in_county': 'Wolverhampton ',
  'birder': 'testuser4',
}, 
{
  'species': 'Slavonian Grebe ',
  'date_seen': '06/04/2021',
  'in_country': 'Scotland',
  'in_county': 'Shetland Islands',
  'birder': 'testuser4',

},
{
  'species': 'Black-necked Grebe',
  'date_seen': '18/06/2018',
  'in_country': 'Scotland',
  'in_county': 'Perth and Kinross ',
  'birder': 'testuser1 ',

},
{
  'species': 'Black-necked Grebe',
  'date_seen': '20/10/2021',
  'in_country': 'Scotland',
  'in_county': 'Shetland Islands',
  'birder': 'testuser4',

},
{
  'species': 'Black-necked Grebe',
  'date_seen': '27/10/2018',
  'in_country': 'Scotland',
  'in_county': 'Shetland Islands',
  'birder': 'testuser1 ',

},
{
  'species': 'Great Crested Grebe ',
  'date_seen': '29/03/2018',
  'in_country': 'Scotland',
  'in_county': 'Shetland Islands',
  'birder': 'testuser4',

},
{
  'species': 'Pied-billed Grebe ',
  'date_seen': '26/02/2019',
  'in_country': 'Scotland',
  'in_county': 'Shetland Islands',
  'birder': 'testuser3 ',

},
{
  'species': 'Slavonian Grebe ',
  'date_seen': '01/02/2020',
  'in_country': 'Scotland',
  'in_county': 'Renfrewshire ',
  'birder': 'testuser3 ',

},
{
  'species': 'Black-necked Grebe',
  'date_seen': '12/03/2021',
  'in_country': 'Scotland',
  'in_county': 'Shetland Islands',
  'birder': 'testuser2 ',

},
{
  'species': 'Slavonian Grebe ',
  'date_seen': '26/12/2019',
  'in_country': 'Scotland',
  'in_county': 'Shetland Islands',
  'birder': 'testuser3 ',

},
{
  'species': 'Slavonian Grebe ',
  'date_seen': '08/03/2021',
  'in_country': 'Scotland',
  'in_county': 'Inverclyde ',
  'birder': 'testuser4',

},
{
  'species': 'Black-necked Grebe',
  'date_seen': '16/03/2018',
  'in_country': 'Scotland',
  'in_county': 'Orkney Islands ',
  'birder': 'testuser4',

},
{
  'species': 'Black-necked Grebe',
  'date_seen': '19/05/2018',
  'in_country': 'Scotland',
  'in_county': 'Renfrewshire ',
  'birder': 'testuser4',

},
{
  'species': 'Slavonian Grebe ',
  'date_seen': '05/11/2018',
  'in_country': 'Scotland',
  'in_county': 'Renfrewshire ',
  'birder': 'testuser4',

},
{
  'species': 'Pied-billed Grebe ',
  'date_seen': '14/01/2019',
  'in_country': 'Scotland',
  'in_county': 'Shetland Islands',
  'birder': 'testuser1 ',

},
{
  'species': 'Black-necked Grebe',
  'date_seen': '11/06/2019',
  'in_country': 'Scotland',
  'in_county': 'Renfrewshire ',
  'birder': 'testuser4',

},
{
  'species': 'Black-necked Grebe',
  'date_seen': '31/05/2019',
  'in_country': 'Scotland',
  'in_county': 'Shetland Islands',
  'birder': 'testuser4',

},
{
  'species': 'Black-necked Grebe',
  'date_seen': '25/12/2020',
  'in_country': 'Scotland',
  'in_county': 'Perth and Kinross ',
  'birder': 'testuser4',

}, 
{
  'species': 'Slavonian Grebe ',
  'date_seen': '15/05/2021',
  'in_country': 'Northern Ireland',
  'in_county': 'Strabane',
  'birder': 'testuser2 ',

},
{
  'species': 'Great Crested Grebe ',
  'date_seen': '26/01/2018',
  'in_country': 'Northern Ireland',
  'in_county': 'Strabane',
  'birder': 'testuser4',

},
{
  'species': 'Great Crested Grebe ',
  'date_seen': '10/08/2021',
  'in_country': 'Northern Ireland',
  'in_county': 'Cookstown ',
  'birder': 'testuser4',

},
{
  'species': 'Great Crested Grebe ',
  'date_seen': '12/04/2021',
  'in_country': 'Northern Ireland',
  'in_county': 'Omagh ',
  'birder': 'testuser4',

},
{
  'species': 'Crane ',
  'date_seen': '06/08/2020',
  'in_country': 'Northern Ireland',
  'in_county': 'Strabane',
  'birder': 'testuser3 ',

},
{
  'species': 'Slavonian Grebe ',
  'date_seen': '21/06/2021',
  'in_country': 'Northern Ireland',
  'in_county': 'Strabane',
  'birder': 'testuser4',

},
{
  'species': 'Slavonian Grebe ',
  'date_seen': '20/09/2018',
  'in_country': 'Northern Ireland',
  'in_county': 'Cookstown ',
  'birder': 'testuser4',

},
{
  'species': 'Black-necked Grebe',
  'date_seen': '22/10/2019',
  'in_country': 'Northern Ireland',
  'in_county': 'Dungannon ',
  'birder': 'testuser3 ',

},
{
  'species': 'Slavonian Grebe ',
  'date_seen': '13/06/2019',
  'in_country': 'Northern Ireland',
  'in_county': 'Cookstown ',
  'birder': 'testuser3 ',

},
{
  'species': 'Pied-billed Grebe ',
  'date_seen': '08/12/2020',
  'in_country': 'Northern Ireland',
  'in_county': 'Strabane',
  'birder': 'testuser3 ',

},
{
  'species': 'Black-necked Grebe',
  'date_seen': '19/08/2019',
  'in_country': 'Northern Ireland',
  'in_county': 'Strabane',
  'birder': 'testuser4',

},
{
  'species': 'Great Crested Grebe ',
  'date_seen': '30/08/2020',
  'in_country': 'Northern Ireland',
  'in_county': 'Cookstown ',
  'birder': 'testuser4',

},
{
  'species': 'Black-necked Grebe',
  'date_seen': '06/02/2018',
  'in_country': 'Northern Ireland',
  'in_county': 'Cookstown ',
  'birder': 'testuser3 ',
},
{
  'species': 'Black-necked Grebe',
  'date_seen': '29/10/2021',
  'in_country': 'Northern Ireland',
  'in_county': 'Cookstown ',
  'birder': 'testuser4',
},
{
  'species': 'Slavonian Grebe ',
  'date_seen': '23/12/2018',
  'in_country': 'Northern Ireland',
  'in_county': 'Strabane',
  'birder': 'testuser4',
},
{
  'species': 'Black-necked Grebe',
  'date_seen': '30/06/2020',
  'in_country': 'Northern Ireland',
  'in_county': 'Strabane',
  'birder': 'testuser4',
},
{
  'species': 'Black-necked Grebe',
  'date_seen': '06/12/2019',
  'in_country': 'Northern Ireland',
  'in_county': 'Strabane',
  'birder': 'testuser4',
}, 
{
  'species': 'Black-necked Grebe',
  'date_seen': '15/01/2018',
  'in_country': 'Wales',
  'in_county': 'Ceredigion',
  'birder': 'testuser4',

},
{
  'species': 'Black-necked Grebe',
  'date_seen': '15/05/2018',
  'in_country': 'Wales',
  'in_county': 'Ceredigion',
  'birder': 'testuser4',

},
{
  'species': 'Black-necked Grebe',
  'date_seen': '11/04/2020',
  'in_country': 'Wales',
  'in_county': 'Carmarthenshire ',
  'birder': 'testuser4',

},
{
  'species': 'Black-necked Grebe',
  'date_seen': '21/05/2021',
  'in_country': 'Wales',
  'in_county': 'Ceredigion',
  'birder': 'testuser4',

},
{
  'species': 'Black-necked Grebe',
  'date_seen': '17/07/2020',
  'in_country': 'Wales',
  'in_county': 'Ceredigion',
  'birder': 'testuser4',

},
{
  'species': 'Great Crested Grebe ',
  'date_seen': '22/06/2019',
  'in_country': 'Wales',
  'in_county': 'Ceredigion',
  'birder': 'testuser3 ',

},
{
  'species': 'Black-necked Grebe',
  'date_seen': '17/10/2020',
  'in_country': 'Wales',
  'in_county': 'Ceredigion',
  'birder': 'testuser4',

},
{
  'species': 'Black-necked Grebe',
  'date_seen': '28/02/2020',
  'in_country': 'Wales',
  'in_county': 'Pembrokeshire ',
  'birder': 'testuser4',

},
{
  'species': 'Slavonian Grebe ',
  'date_seen': '25/06/2019',
  'in_country': 'Wales',
  'in_county': 'Pembrokeshire ',
  'birder': 'testuser3 ',

},
{
  'species': 'Black-necked Grebe',
  'date_seen': '15/02/2020',
  'in_country': 'Wales',
  'in_county': 'Pembrokeshire ',
  'birder': 'testuser2 ',

},
{
  'species': 'Little Grebe ',
  'date_seen': '22/02/2019',
  'in_country': 'Wales',
  'in_county': 'Pembrokeshire ',
  'birder': 'testuser1 ',

},
{
  'species': 'Black-necked Grebe',
  'date_seen': '31/08/2020',
  'in_country': 'Wales',
  'in_county': 'Neath Port Talbot ',
  'birder': 'testuser3 ',

},
{
  'species': 'Black-necked Grebe',
  'date_seen': '06/09/2018',
  'in_country': 'Wales',
  'in_county': 'Ceredigion',
  'birder': 'testuser3 ',

},
{
  'species': 'Slavonian Grebe ',
  'date_seen': '15/04/2020',
  'in_country': 'Wales',
  'in_county': 'Ceredigion',
  'birder': 'testuser4',

},
{
  'species': 'Black-necked Grebe',
  'date_seen': '16/11/2018',
  'in_country': 'Wales',
  'in_county': 'Ceredigion',
  'birder': 'testuser3 ',

},
{
  'species': 'Slavonian Grebe ',
  'date_seen': '18/05/2020',
  'in_country': 'Wales',
  'in_county': 'Carmarthenshire ',
  'birder': 'testuser4',

},
{
  'species': 'Black-necked Grebe',
  'date_seen': '11/02/2020',
  'in_country': 'Wales',
  'in_county': 'Ceredigion',
  'birder': 'testuser2 ',
}]
    for sighting in sighting_list:
        add_sighting(sighting['species'], sighting['date_seen'], sighting['in_country'], sighting['in_county'], sighting['birder'])

def add_sighting(species, date_seen, in_county, in_country, birder):
    s = Sighting.objects.get_or_create(species = species, 
                                        date_seen = date_seen,
                                        in_country = in_country,
                                        in_county =in_county, 
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