"""
Functions for converting between distance and latitude/longitude coordinates.
"""
import numpy as np

__author__ = 'Rusty Gentile'


def distance(lat1, long1, lat2, long2):
    """
    Reference: https://www.movable-type.co.uk/scripts/latlong.html

    Parameters
    ----------
    lat1 : float
        Latitude of the first location in degrees
    long1 : float
        Longitude of the first location in degrees
    lat2 : float
        Latitude of the second location in degrees
    long2 : float
        Longitude of the second location in degrees

    Returns
    -------
    Distance between two locations in meters 
    """

    r = 6371e3
    phi1 = lat1 * np.pi / 180
    phi2 = lat2 * np.pi / 180
    dphi = (lat2 - lat1) * np.pi / 180
    dlambda = (long2 - long1) * np.pi / 180

    a = np.sin(dphi / 2) * np.sin(dphi / 2) + np.cos(phi1) * np.cos(phi2) \
        * np.sin(dlambda / 2) * np.sin(dlambda) / 2

    c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1 - a))

    return r * c


def new_point(lat, long, d, theta):
    """
    Approximates a new set of coordinates given an initial point, a direction,
    and a distance. This is not entirely accurate since it treats the Earth's
    surface as a plane. But for our purposes, it should be good enough.

    Parameters
    ----------
    lat : float
        Latititude of the initial point
    long : float
        Longitude of the initial point
    d : float
        Distance to the new point (meters)
    theta: float
        Angle of the direction between points

    Returns
    -------
    new_lat, new_long
        New coordinates
    """

    r = 6371e3
    meters_per_degree = r / 180 * np.pi

    new_lat = lat + d * np.cos(theta) / meters_per_degree
    new_long = long + d * (
               np.sin(theta) / np.cos(lat * np.pi / 180)
               ) / meters_per_degree

    return new_lat, new_long
