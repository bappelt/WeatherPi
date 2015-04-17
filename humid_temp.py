# import Adafruit_Python_DHT
import weather_utils
import Adafruit_DHT

def read_humid_temp():
  humidity, temp_c = Adafruit_DHT.read_retry(Adafruit_DHT.AM2302, 4)
  temp_f = temp_c * 9.0 / 5.0 + 32.0
  return { 'temp_f': temp_f, 'temp_c': temp_c, 'humidity': humidity }
