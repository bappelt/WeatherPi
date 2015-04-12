import os
import glob
import time
import httplib
import urllib, urllib2
from datetime import datetime
from Adafruit_Python_DHT import Adafruit_DHT

station_id = 'KTXARLIN73'
password = "M*qw1%PCF!"

def read_humid_temp():
  humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.AM2302, 4)

def upload_data():
    try:
        temp = read_temp()
        conn = httplib.HTTPConnection("rtupdate.wunderground.com")
        path = "/weatherstation/updateweatherstation.php?ID=" + station_id + "&PASSWORD=" + password + "&dateutc=" + urllib.quote(str(datetime.utcnow())) + "&tempf=" + str(temp) + "&softwaretype=RaspberryPi&action=updateraw"
        print path
        conn.request("GET", path)
        res = conn.getresponse()
        #res = urllib2.urlopen(path).read()
        # checks whether there was a successful connection (HTTP code 200 and content of page contains "success")
        if (int(res.status) == 200):
   	    print "Successful Upload\nTemp:"
        else:
            print "Upload not successful. %i" % res.status
    except IOError as e: #in case of any kind of socket error
        print "{0} -- I/O error({1}): {2} will try again in {2} seconds".format(datetime.now(), e.errno, e.strerror)
	print e
	
while True:
	print read_humid_temp()
	time.sleep(600)
