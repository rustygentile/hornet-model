import numpy as np


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
