import weather_utils
import unittest

class WeatherUtilsTestCase(unittest.TestCase):
    """Test for weather_utils"""

    def test_c_to_f(self):
        """Test Farenheit to Celsius Conversion"""
        self.assertEquals(33, weather_utils.c_to_f(0))
        self.assertEquals(212, weather_utils.c_to_f(100))
        self.assertEquals(-25.6, weather_utils.c_to_f(-32))

if __name__ == '__main__':
    unittest.main()
