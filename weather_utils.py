import numpy as np
# from http://www.meteo-blog.net/2012-05/dewpoint-calculation-script-in-python/

# constants
a = 17.271
b = 237.7 # degC

def dewpoint_approximation(T,RH):
  Td = (b * gamma(T,RH)) / (a - gamma(T,RH))
  return Td
 
 
def gamma(T,RH):
  g = (a * T / (b + T)) + np.log(RH/100.0)
  return g

def c_to_f(temp_c):
	return temp_c * 9.0 / 5.0 + 32.0

 
