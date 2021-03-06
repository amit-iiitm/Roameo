import urllib2
import json
from googleplaces import GooglePlaces, types, lang
import googlemaps
import os
import requests
import urllib


#os.environ['http_proxy']='http://182.48.248.67/'
#os.environ['https_proxy']='https://182.48.248.67/'



# urllib2 opener to connection through a proxy using the CONNECT method, (useful for SSL)
# tested with python 2.4

import urllib2
import urllib
import httplib
import socket


class ProxyHTTPConnection(httplib.HTTPConnection):

    _ports = {'http' : 80, 'https' : 443}


    def request(self, method, url, body=None, headers={}):
        #request is called before connect, so can interpret url and get
        #real host/port to be used to make CONNECT request to proxy
        proto, rest = urllib.splittype(url)
        if proto is None:
            raise ValueError, "unknown URL type: %s" % url
        #get host
        host, rest = urllib.splithost(rest)
        #try to get port
        host, port = urllib.splitport(host)
        #if port is not defined try to get from proto
        if port is None:
            try:
                port = self._ports[proto]
            except KeyError:
                raise ValueError, "unknown protocol for: %s" % url
        self._real_host = host
        self._real_port = port
        httplib.HTTPConnection.request(self, method, url, body, headers)
        

    def connect(self):
        httplib.HTTPConnection.connect(self)
        #send proxy CONNECT request
        self.send("CONNECT %s:%d HTTP/1.0\r\n\r\n" % (self._real_host, self._real_port))
        #expect a HTTP/1.0 200 Connection established
        response = self.response_class(self.sock, strict=self.strict, method=self._method)
        (version, code, message) = response._read_status()
        #probably here we can handle auth requests...
        if code != 200:
            #proxy returned and error, abort connection, and raise exception
            self.close()
            raise socket.error, "Proxy connection failed: %d %s" % (code, message.strip())
        #eat up header block from proxy....
        while True:
            #should not use directly fp probablu
            line = response.fp.readline()
            if line == '\r\n': break


class ProxyHTTPSConnection(ProxyHTTPConnection):
    
    default_port = 443

    def __init__(self, host, port = None, key_file = None, cert_file = None, strict = None):
        ProxyHTTPConnection.__init__(self, host, port)
        self.key_file = key_file
        self.cert_file = cert_file
    
    def connect(self):
        ProxyHTTPConnection.connect(self)
        #make the sock ssl-aware
        ssl = socket.ssl(self.sock, self.key_file, self.cert_file)
        self.sock = httplib.FakeSocket(self.sock, ssl)
        
                                       
class ConnectHTTPHandler(urllib2.HTTPHandler):

    def do_open(self, http_class, req):
        return urllib2.HTTPHandler.do_open(self, ProxyHTTPConnection, req)


class ConnectHTTPSHandler(urllib2.HTTPSHandler):

    def do_open(self, http_class, req):
        return urllib2.HTTPSHandler.do_open(self, ProxyHTTPSConnection, req)


if __name__ == '__main__':
    
    import sys
    
    opener = urllib2.build_opener(ConnectHTTPHandler, ConnectHTTPSHandler)
    urllib2.install_opener(opener)
    req = urllib2.Request(url='https://192.168.1.1')
    req.set_proxy('192.168.1.254:3128', 'https')
    f = urllib2.urlopen(req)
    print f.read()


YOUR_API_KEY = 'AIzaSyAh5ATqZJulZAAe9Z1A95rO1CtFNWusQS4'

#response=urllib2.urlopen('https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=-33.8670522,151.1957362&radius=500&types=food&name=cruise&key=AIzaSyAurou_pOhlh_dHlPtnKG1f8qIwZBRhXr4')

#response=urllib2.urlopen('http://www.google.com')
#print response.read()

#response=requests.get('https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=-33.8670522,151.1957362&radius=500&types=mall&name=cruise&key=AIzaSyAurou_pOhlh_dHlPtnKG1f8qIwZBRhXr4')

#print response


# pull lat and lng from your parks database and construct a url like:
url = 'https://maps.googleapis.com/maps/api/geocode/json?latlng=40.714224,-73.961452&key=AIzaSyAh5ATqZJulZAAe9Z1A95rO1CtFNWusQS4'

resp = requests.get('https://maps.googleapis.com/maps/api/geocode/json?latlng=40.714224,-73.961452&key=AIzaSyAh5ATqZJulZAAe9Z1A95rO1CtFNWusQS4').read()
print resp
#print resp.read() # json string convert to python dict

