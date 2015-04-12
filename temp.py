import os
import glob
import time
import httplib
import urllib, urllib2
from datetime import datetime
import Adafruit_DHT

station_id = 'KTXARLIN73'
password = "M*qw1%PCF!"

def read_humid_temp():
  humidity, temp_c = Adafruit_DHT.read_retry(Adafruit_DHT.AM2302, 4)
  temp_f = temp_c * 9.0 / 5.0 + 32.0
  return { 'temp_f': temp_f, 'temp_c': temp_c, 'humidity': humidity }

def upload_data(data):
    try:
        conn = httplib.HTTPConnection("rtupdate.wunderground.com")
        path = "/weatherstation/updateweatherstation.php?ID=" + station_id + "&PASSWORD=" + password + "&dateutc=" + urllib.quote(str(datetime.utcnow())) + "&tempf=" + str(data['temp_f']) + "&humidity=" + str(data['humidity']) + "&softwaretype=RaspberryPi&action=updateraw"
        print path
        conn.request("GET", path)
        res = conn.getresponse()
        #res = urllib2.urlopen(path).read()
        # checks whether there was a successful connection (HTTP code 200 and content of page contains "success")
        if (int(res.status) == 200):
   	    print "Successful Upload"
        else:
            print "Upload not successful. %i" % res.status
    except IOError as e: #in case of any kind of socket error
        print "{0} -- I/O error({1}): {2} will try again in {2} seconds".format(datetime.now(), e.errno, e.strerror)
	print e
	
while True:
        data = read_humid_temp()
        upload_data(data)
	time.sleep(600)
