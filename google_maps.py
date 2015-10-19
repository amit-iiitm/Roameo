import googlemaps
from googlemaps import Client

api_key='AIzaSyAdBgFT0O0_4nq6lWH3ab1jtFIfJVm0vUI'
gmaps=Client(api_key)
address='ABV-IIITM Gwalior'
lat, lng = gmaps.address_to_latlng(address)
print lat, lng
