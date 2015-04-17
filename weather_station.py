import os
import glob
import time
import httplib
import urllib, urllib2
from datetime import datetime
import weather_utils
import humid_temp

station_id = os.environ('WEATHER_UNDERGROUND_STATION_ID')
password = os.environ('WEATHER_UNDERGROUND_PASSWORD')

def upload_data(data):
    try:
        conn = httplib.HTTPConnection("rtupdate.wunderground.com")
        path = ("/weatherstation/updateweatherstation.php?ID=" + station_id + "&PASSWORD=" + password
                + "&dateutc=" + urllib.quote(str(datetime.utcnow())) + "&tempf=" + str(data['temp_f'])
                + "&humidity=" + str(data['humidity'])
                + "&dewptf=" + str(data['dewptf'])
                + "&softwaretype=RaspberryPi&action=updateraw")
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

def get_data():
  data = humid_temp.get_data()
  return data

while True:
  data = get_data()
  upload_data(data)
  time.sleep(600)
