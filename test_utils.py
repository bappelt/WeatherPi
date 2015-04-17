import weather_utils
import unittest

class WeatherUtilsTestCase(unittest.TestCase):
    """Test for weather_utils"""

    def test_c_to_f(self):
        """Test Farenheit to Celsius Conversion"""
        self.assertEquals(32, weather_utils.c_to_f(0))
        self.assertEquals(212, weather_utils.c_to_f(100))
        self.assertEquals(-25.6, weather_utils.c_to_f(-32))

    def test_c_to_f(self):
        """Test Celsius to Farenheit Conversion"""
        self.assertEquals(0, weather_utils.f_to_c(32))
        self.assertEquals(100, weather_utils.f_to_c(212))
        self.assertEquals(-32, weather_utils.f_to_c(-25.6))

    def test_dew_point_c(self):
        """Test Dewpoint Calculation"""
        self.assertAlmostEqual(15, weather_utils.dewpoint_c(17, 88), 2)

    def test_dew_point_f(self):
        """Test Dewpoint Calculation"""
        self.assertAlmostEqual(58.99, weather_utils.dewpoint_f(62.6, 88), 2)

if __name__ == '__main__':
    unittest.main()
