import numpy as np
# from http://www.meteo-blog.net/2012-05/dewpoint-calculation-script-in-python/

# constants
a = 17.271
b = 237.7 # degC

def dewpoint_c(temp_c, rh):
    return (b * gamma(temp_c, rh)) / (a - gamma(temp_c, rh))

def dewpoint_f(temp_f, rh):
    temp_c = f_to_c(temp_f)
    dewpoint_celcius = dewpoint_c(temp_c, rh)
    return c_to_f(dewpoint_celcius)

def gamma(temp_c, rh):
    return (a * temp_c / (b + temp_c)) + np.log(rh/100.0)

def c_to_f(temp_c):
    return temp_c * 9.0 / 5.0 + 32.0

def f_to_c(temp_f):
    return (5.0/9.0)*(temp_f-32)
