import unittest
import numpy as np
from src.simulate import simulate


class SimulationTest(unittest.TestCase):

    def test_sim_no_geo(self):
        """Setup a random simulation"""
        stl_lat = 47.6062
        stl_long = -122.3321
        n_starting_hives = 10
        coords = []
        for i in range(n_starting_hives):
            coords.append((stl_lat + np.random.random(), stl_long + np.random.random()))

        df = simulate(coords, 2020, 10)
        print(df.head())
        print(df.tail())


    def test_sim_geo(self):
        """Setup a random simulation with a geometry file"""
        stl_lat = 47.6062
        stl_long = -122.3321
        n_starting_hives = 10
        coords = []
        for i in range(n_starting_hives):
            coords.append((stl_lat + np.random.random(), stl_long + np.random.random()))

        df = simulate(coords, 2020, 10,
                      shape_file='../data/states_reduced/states_reduced.shp')

        print(df.head())
        print(df.tail())


if __name__ == '__main__':
    unittest.main()
