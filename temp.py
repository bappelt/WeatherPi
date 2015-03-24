import os
import glob
import time
import httplib
import urllib, urllib2
from datetime import datetime

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'

station_id = 'KTXARLIN73'
password = "M*qw1%PCF!"

def read_temp_raw():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines

def read_temp():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        temp_f = temp_c * 9.0 / 5.0 + 32.0
        return temp_f

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
	upload_data()
	time.sleep(600)
