import unittest
from src.haversine import distance
 

class DistanceTest(unittest.TestCase):

    def test_orl_nyc(self):
        """Calculate the distance between Orlando and NY based on lat/long"""

        ny_lat = 40.7128
        ny_long = 74.0060
        orl_lat = 28.5383
        orl_long = 81.3792

        # Distance in km According to Google...
        d_ny_orl_exp = 1511e3
        d_ny_orl_act = distance(ny_lat, ny_long, orl_lat, orl_long)

        # Accurate to within 300m is good enough
        self.assertLess(abs(d_ny_orl_act - d_ny_orl_exp), 300)

    def test_stl_spk(self):
        """Calculate the distance between Seattle and Spokane"""

        stl_lat = 47.6062
        stl_long = 122.3321
        spk_lat = 47.6588
        spk_long = 117.4260

        # Distance in km According to Google...
        d_stl_spk_exp = 367.3e3
        d_stl_spk_act = distance(stl_lat, stl_long, spk_lat, spk_long)

        # Accurate to within 300m is good enough
        self.assertLess(abs(d_stl_spk_act - d_stl_spk_exp), 300)


if __name__ == '__main__':
    unittest.main()
