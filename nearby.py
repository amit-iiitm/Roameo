from __future__ import absolute_import
from googleplaces import GooglePlaces, types, lang
import googlemaps
import os


import cgi
try:
    import json
except ImportError:
    import simplejson as json
import urllib

# For compatibility with Python 3
try:
    from urllib import request as urllib2  # Python 3 import
except ImportError:
    import urllib2
import warnings






#os.environ['http_proxy']='http://182.48.248.67/'
#os.environ['https_proxy']='https://182.48.248.67/'


YOUR_API_KEY = 'AIzaSyAurou_pOhlh_dHlPtnKG1f8qIwZBRhXr4'

google_places = GooglePlaces(YOUR_API_KEY)
'''
#geocoding to get latitute and longitude of a place form a name
gmaps = googlemaps.Client(key='AIzaSyCH1UT4Uk7P5FyuK1Rp2muCC_EgQUDNaTs')
#geocode_result=gmaps.geocode('Taj Palace, No 2, Sardar Patel Marg, Diplomatic Enclave, New Delhi, Delhi 110021, India')

reverse_geocode_result=gmaps.reverse_geocode((40.714224,-73.961452))

print geocode_result
print reverse_geocode_result


#Request directions via public transit
now=datetime.now()
directions_result=gmaps.directions(source,end,mode="transit",departure_time=now)
'''

# You may prefer to use the text_search API, instead.
lat_lng={'lat':40.714224,'lng':-73.961452}
query_result = google_places.nearby_search(lang.ENGLISH,None, 'London',
               lat_lng, None, int(3200), 'ranking.PROMINENCE',
               False, [])

if query_result.has_attributions:
    print query_result.html_attributions


for place in query_result.places:
    # Returned places from a query are place summaries.
    print place.name
    print place.geo_location
    print place.place_id

    # The following method has to make a further API call.
    place.get_details()
    # Referencing any of the attributes below, prior to making a call to
    # get_details() will raise a googleplaces.GooglePlacesAttributeError.
    print place.details # A dict matching the JSON response from Google.
    print place.local_phone_number
    print place.international_phone_number
    print place.website
    print place.url

    # Getting place photos

    for photo in place.photos:
        # 'maxheight' or 'maxwidth' is required
        photo.get(maxheight=500, maxwidth=500)
        # MIME-type, e.g. 'image/jpeg'
        photo.mimetype
        # Image URL
        photo.url
        # Original filename (optional)
        photo.filename
        # Raw image data
        photo.data


# Adding and deleting a place
try:
    added_place = google_places.add_place(name='Mom and Pop local store',
            lat_lng={'lat': 51.501984, 'lng': -0.141792},
            accuracy=100,
            types=types.TYPE_HOME_GOODS_STORE,
            language=lang.ENGLISH_GREAT_BRITAIN)
    print added_place.place_id # The Google Places identifier - Important!
    print added_place.id

    # Delete the place that you've just added.
    google_places.delete_place(added_place.place_id)
except GooglePlacesError as error_detail:
    # You've passed in parameter values that the Places API doesn't like..
    print error_detail
