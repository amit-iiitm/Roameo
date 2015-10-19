import googlemaps
from googlemaps import Client
import json
import urllib2
import os

#os.environ['http_proxy']='http://182.48.248.67/'
#os.environ['https_proxy']='https://182.48.248.67/'

'''opener = urllib2.build_opener(
                urllib2.HTTPHandler(),
                urllib2.HTTPSHandler(),
                urllib2.ProxyHandler({'https': 'https:86294517@182.48.248.67:3128'}))
urllib2.install_opener(opener)'''


'''response=urllib2.urlopen('https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=-33.8670522,151.1957362&radius=500&types=food&name=cruise&key=AIzaSyAurou_pOhlh_dHlPtnKG1f8qIwZBRhXr4')
print "hearing the response"
latitute=-33.8670522
longitude=151.1957362
url='https://maps.googleapis.com/maps/api/place/nearbysearch/json?location='+str(latitute)+','+str(longitude)+'&radius='+str(500)+'&types=food&name=cruise&key=AIzaSyAurou_pOhlh_dHlPtnKG1f8qIwZBRhXr4\''''


def parse(self,response):
	try:
		print response.status
		print '???????????????????????????????????'
		if response.status==200:
			self.driver.implicitly_wait(5)
			self.driver.get(response.url)
			print response.url
			print '!!!!!!!!!!!!'
	except httplib.BadStatusLine:
		pass

#parse(urllib2.urlopen('https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=-33.8670522,151.1957362&radius=500&types=food&name=cruise&key=AIzaSyAurou_pOhlh_dHlPtnKG1f8qIwZBRhXr4'))

#parse(urllib.urlopen('http://'))
def get_directions(start,end):
	
	mapService= Client('AIzaSyDpo931DWDqeeHXeaNAvydQH4isieEHc9s')

	directions=mapService.directions(start,end)

	#print each step in directions to console
	#print json.dumps(directions,indent=4,sort_keys=True)

	for step in directions[0]['legs'][0]['steps']:
    		print step['html_instructions']
    		print 


def get_nearby(latitute,longitude):
	url='https://maps.googleapis.com/maps/api/place/nearbysearch/json?location='+latitute+','+longitude+'&radius=500&types=food&key=AIzaSyAurou_pOhlh_dHlPtnKG1f8qIwZBRhXr4'

	response=urllib2.urlopen(url).read()
	print response
	places=[]
	for result in response['results']:
		places.append(result['vicinity'])
	print places
	return places

def lat_lng(addr):
	latitute=addr.split(',')[0]
	longitude=addr.split(',')[1]
	print latitute
	print longitude	
	get_nearby(latitute,longitude)

lat_lng("28.635308,77.224960")
#get_nearby(-33.8670522,151.1957362)
#proxy=urllib2.ProxyHandler()
#opener=urllib2.build_opener(proxy)
#urllib2.install_opener(opener)
#response=opener.open('http://www.google.com')
#response=urllib2.urlopen('https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=-33.8670522,151.1957362&radius=500&types=food&name=cruise&key=AIzaSyAurou_pOhlh_dHlPtnKG1f8qIwZBRhXr4')


#response=urllib2.urlopen('http://www.google.com').read()
#print response



#geocoding to get latitute and longitude of a place form a name
#gmaps = Client(key='AIzaSyCH1UT4Uk7P5FyuK1Rp2muCC_EgQUDNaTs')
#geocode_result=gmaps.geocode('Taj Palace, No 2, Sardar Patel Marg, Diplomatic Enclave, New Delhi, Delhi 110021, India')

#reverse_geocode_result=gmaps.reverse_geocode((40.714224,-73.961452))

#print geocode_result
#print reverse_geocode_result


#Request directions via public transit
#now=datetime.now()
#directions_result=gmaps.directions(source,end,mode="transit",departure_time=now)
def get_sorted(cur_user,list_user):
	cur_addr=[]
	cur_addr.append(cur_user.split(',')[0])
	cur_addr.append(cur_user.split(',')[1])
	list_user_distance=[]
	for key,value in list_user:
		list_user_distance.append(key)
	dict_dist={}
	for user in list_user_distance:
		temp=[]
		temp.append(user.split(',')[0])
		temp.append(user.split(',')[1])
		value=get_distance(cur_addr,temp)
		dict_dist[value]=list_user[user]
	return dict_dist
def get_distance(source,dest):
	url='https://maps.googleapis.com/maps/api/distancematrix/json?origins='+source[0]+','+source[1]+'&destinations='+dest[0]+','+dest[1]+'&mode=bicycling&language=fr-FR&key=AIzaSyCvrVNMZxbDUFvASS1IfcI9Kqsg9cWEmd8'
	response=urllib2.urlopen(url).read()
	for row in response['rows']:
		return row['elements'][0]['distance']['value']
