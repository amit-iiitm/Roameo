import urllib3
import requests
from urllib3.connection import UnverifiedHTTPSConnection
from urllib3.connectionpool import connection_from_url
import json


#response=requests.get('https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=-33.8670522,151.1957362&radius=500&types=food&name=cruise&key=AIzaSyAurou_pOhlh_dHlPtnKG1f8qIwZBRhXr4')
#response=requests.get('http://www.google.com')

'''
http = urllib3.PoolManager()

r = https.request('GET', 'http://google.com/')

print r.status, r.data


# Get a ConnectionPool object, same as what you're doing in your question
http = connection_from_url(remote_server_url, maxsize=2)

# Override the connection class to force the unverified HTTPSConnection class
http.ConnectionCls = UnverifiedHTTPSConnection

# Make requests as normal...
r = http.request(...)'''
"""
from urllib3 import HTTPSConnectionPool
with HTTPSConnectionPool('maps.googleapis.com', maxsize=1) as pool:
     #r = pool.request('GET', '/ajax/services/search/web',
                      #fields={'q': 'urllib3', 'v': '1.0'})
     r=pool.request('GET','https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=-33.8670522,151.1957362&radius=500&types=food&name=cruise&key=AIzaSyAurou_pOhlh_dHlPtnKG1f8qIwZBRhXr4')
     print r.status
     print r.data
     """


def get_nearby(location):
	from urllib3 import HTTPSConnectionPool
	with HTTPSConnectionPool('maps.googleapis.com',maxsize=1) as pool:
		r=pool.request('GET','https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={0}&radius=500&types=food&key=AIzaSyAurou_pOhlh_dHlPtnKG1f8qIwZBRhXr4'.format(location))
		#print r.data
		response=r.data
		#print response
		response=json.loads(response)
		places=[]
		for result in response['results']:
			places.append(result['vicinity'])
		return places

def lat_lng(addr):
	latitute=addr.split(',')[0]
	longitude=addr.split(',')[1]
	print latitute
	print longitude	
	get_nearby(latitute,longitude)

#lat_lng("28.635308,77.224960")
print
print
print get_nearby("28.635308,77.224960")
print
