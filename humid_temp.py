# import Adafruit_Python_DHT
import weather_utils
import Adafruit_DHT

def get_data():
  humidity, temp_c = Adafruit_DHT.read_retry(Adafruit_DHT.AM2302, 4)
  temp_f = weather_utils.c_to_f(temp_c)
  return {  'temp_f': temp_f,
            'temp_c': temp_c,
            'humidity': humidity,
            'dewptf': weather_utils.dewpoint_f(temp_f) }
