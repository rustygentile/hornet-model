"""
Prepare and clean data for regression models and simulations. Be sure the
shapefile and project data are downloaded first.
"""
import pandas as pd
import numpy as np
import datetime as dt
import geopandas as geo

__author__ = 'Rusty Gentile'


def clean_date(s, year=None):
    """Used to filter the data only for the selected year"""
    try:
        d = dt.datetime.strptime(str(s), '%Y-%m-%d %H:%M:%S')
        if d.year == year:
            return d.timestamp()
        else:
            return np.nan
    except ValueError:
        return np.nan


def make_training_set(year):
    df = pd.read_excel('./data/2021MCMProblemC_DataSet.xlsx', engine='openpyxl')

    # We are only interested in data that has been ID'd
    df_train = df[df['Lab Status'].str.endswith('ID')]

    # Add a column based on the lab results: 1=positive, 0=negative
    df_train['ID'] = df_train['Lab Status'].apply(lambda s: int(s.startswith('P')))

    df_train['ts'] = df_train['Detection Date'].apply(clean_date, year=year)
    return df_train.dropna()


def make_test_set(year):
    df = pd.read_excel('./data/2021MCMProblemC_DataSet.xlsx', engine='openpyxl')

    # We are only interested in data that has been ID'd
    df_train = df[df['Lab Status'].str.startswith('Un')]

    # Add this column for completeness
    df_train['ID'] = df_train['Lab Status'].apply(lambda s: False)

    df_train['ts'] = df_train['Detection Date'].apply(clean_date, year=year)
    return df_train.dropna()


def reduce_shapefile():
    """
    The original file contained more geography than we need. By discarding
    some of the state shapes, we can save computation time in our simulations.
    """

    states_to_keep = [
        'British Columbia',
        'Yukon',
        'Alberta',
        'Washington',
        'Oregon',
        'Idaho',
        'Montana',
        'Nevada',
        'California',
        'Utah',
        'Wyoming'
    ]

    def drop_states(s):
        for k in states_to_keep:
            if s.upper() == k.upper():
                return s.upper()
        return None

    df = geo.read_file('./data/USA_Canada/USA_Canada_ShapefileMerge.shp')
    df['StateName'] = df['StateName'].apply(drop_states)
    df_reduced = df[df['StateName'].notnull()]
    df_reduced.to_file('./data/states_reduced/states_reduced.shp')


def main():
    df_19 = make_training_set(2019)
    df_20 = make_training_set(2020)
    df_19.to_csv('./data/train_2019.csv')
    df_20.to_csv('./data/train_2020.csv')

    df_19_test = make_test_set(2019)
    df_20_test = make_test_set(2020)
    df_19_test.to_csv('./data/test_2019.csv')
    df_20_test.to_csv('./data/test_2020.csv')

    reduce_shapefile()


if __name__ == '__main__':
    main()
