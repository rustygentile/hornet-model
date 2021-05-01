import numpy as np
import pandas as pd
import geopandas as geo
from shapely.geometry import Point
import logging
from .haversine import new_point

__author__ = 'Rusty Gentile'

logger = logging.getLogger(__name__)


class ShapeChecker:
    """
    Use this to read in a shape file only once. Then call check_shape() from
    our Hive objects.
    """
    def __init__(self, file_location):
        df = geo.read_file(file_location)
        self.shapes = [i[1]['geometry'] for i in df.iterrows()]

    def check_shape(self, lat, long):
        pt = Point(long, lat)
        for s in self.shapes:
            if pt.within(s):
                return True

        return False


class Hive:
    """
    Model of a hornet hive for simulations. Every hive will randomly either
    survive or die out. Hive that survive will spawn new queens which go on
    to start new hives.

    See simulate() for usage.
    """

    def __init__(self, lat, long, year, parameters=None, point_validator=None):

        self.lat = lat
        self.long = long
        self.year = year

        self.survived = None
        self.surviving_queens = 0
        self.MAX_ATTEMPTS = 1000

        # Defaults:
        if parameters is None:
            self.parameters = {
                'p_survival': 0.5,
                'p_queen_survival': 0.1,
                'new_queens': 30,
                'dispersal_range': 100e3
            }
        else:
            self.parameters = parameters

        if point_validator is None:
            self.point_validator = lambda x, y: True
        else:
            self.point_validator = point_validator

    def calculate_survival(self):
        self.survived = np.random.random() < self.parameters['p_survival']
        return self.survived

    def child_hive(self, lat, long):
        return Hive(lat, long, self.year+1, parameters=self.parameters,
                    point_validator=self.point_validator)

    def generate_new_coordinates(self):
        for i in range(self.MAX_ATTEMPTS):
            theta = np.random.random() * 2 * np.pi
            dist = np.random.random() * self.parameters['dispersal_range']
            lat, long = new_point(self.lat, self.long, dist, theta)
            if self.point_validator(lat, long):
                return lat, long

        raise OverflowError('Unable to find a new valid location')

    def disperse(self):
        new_hives = []
        for _ in range(self.parameters['new_queens']):
            if np.random.random() < self.parameters['p_queen_survival']:
                self.surviving_queens += 1
                lat, long = self.generate_new_coordinates()
                new_hives.append(self.child_hive(lat, long))
        return new_hives


def simulate(coordinates, start, n, hive_parameters=None, shape_file=None):
    """
    Runs a simulation of Asian hornet hive populations.

    Parameters:
    -----------
    coordinates : list
        Initial coordinates of the starting population of hives. Should be of
        the form: [(latitude, longitude)]
    start : int
        Initial year
    n : int
        Number of years to simulate
    hive_parameters : dict
        Optional parameters:
            'p_survival' - Probability that the hive will survive long enough
                for new queens to disperse.
            'p_queen_survival' - Probability for each queen that it will
                survive long enough to build a new hive.
            'new_queens' - Number of queens dispersed assuming the hive
                survives
            'dispersal_range' - Maximum distance between a parent and child hive
    shape_file : String
        Location of shape file for valid locations. If a generated point is
        not within one of these, we assume that a new hive cannot be built
        there.

    Return:
    -------
    results : DataFrame
    """

    # Read in geopandas data if it's available
    if shape_file is not None:
        shape_checker = ShapeChecker(shape_file)
        sc = shape_checker.check_shape
    else:
        sc = None

    # Setup initial population
    current_generation = [
        Hive(lat, long, start, parameters=hive_parameters, point_validator=sc)
        for (lat, long) in coordinates
    ]

    # For storing results. One row = one hive
    results = pd.DataFrame(columns=[
        'year',
        'Latitude',
        'Longitude',
        'survived',
        'surviving_queens'
    ])

    for i in range(n):
        new_generation = []
        n_hives = 0
        for h in current_generation:
            if h.calculate_survival():
                new_generation += h.disperse()
                n_hives += 1

        logger.info(f'Year: {start + i}. '
                    f'{n_hives} of {len(current_generation)} hives survived.')

        data = {
            'year': [h.year for h in current_generation],
            'Latitude': [h.lat for h in current_generation],
            'Longitude': [h.long for h in current_generation],
            'survived': [h.survived for h in current_generation],
            'surviving_queens': [h.surviving_queens for h in current_generation]
        }
        results = pd.concat([results, pd.DataFrame(data)])
        current_generation = new_generation

    return results
