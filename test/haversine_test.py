import unittest
import numpy as np
from src.haversine import distance, new_point


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

        # Accurate to within 500m is good enough
        self.assertLess(abs(d_ny_orl_act - d_ny_orl_exp), 500)

    def test_stl_spk(self):
        """Calculate the distance between Seattle and Spokane"""

        stl_lat = 47.6062
        stl_long = 122.3321
        spk_lat = 47.6588
        spk_long = 117.4260

        # Distance in km According to Google...
        d_stl_spk_exp = 367.3e3
        d_stl_spk_act = distance(stl_lat, stl_long, spk_lat, spk_long)

        # Accurate to within 500m is good enough
        self.assertLess(abs(d_stl_spk_act - d_stl_spk_exp), 500)


class NewPointTest(unittest.TestCase):

    def test_stl_new_points(self):
        """
        Generate some points within different distances from Seattle. Then
        verify they are at approximately the correct distance.
        """

        stl_lat = 47.6062
        stl_long = 122.3321
        n = 20
        theta_range = np.linspace(0, 2 * np.pi, n)
        dist_range = np.linspace(1, 100e3, n)

        for t, d in [(t, d) for t in theta_range for d in dist_range]:
            new_lat, new_long = new_point(stl_lat, stl_long, d, t)
            error = distance(new_lat, new_long, stl_lat, stl_long) - d
            self.assertLess(abs(error / d), 0.005)


if __name__ == '__main__':
    unittest.main()
