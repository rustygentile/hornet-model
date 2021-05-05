import logging
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from .haversine import distance

__author__ = 'Rusty Gentile'
logger = logging.getLogger(__name__)


def add_distance_feature(df, coords):
    """
    Parameters:
    -----------
    df : DataFrame
        Training data set
    coords : Array
        Coordinates to which to compare the training set. Should be of the
        form: [(lats, longs)]

    Returns:
    df : DataFrame
        Training data set with 'Distance' column added
    """
    train_coords = [
        (d[1]['Latitude'], d[1]['Longitude']) for d in df.iterrows()
    ]
    dists = []
    for train_coord in train_coords:
        shortest = np.inf
        for sim_coord in coords:
            d = distance(train_coord[0],
                         train_coord[1],
                         sim_coord[0],
                         sim_coord[1]) / 1000.
            d = min(shortest, d)

        dists.append(d)

    df['Distance'] = np.array(dists)
    return df


def make_and_run_model(year, sim_file, sim_year, use_ts=False):
    """
    Logistic regression using feature generation based on simulation model
    results.
    """

    # Get training data set coordinates
    df_train = pd.read_csv(f'./data/train_{year}.csv')

    # Get coordinates of simulated population
    df_sim = pd.read_csv(sim_file)
    df_sim_year = df_sim[df_sim['year'] == sim_year]

    sim_coords = [
        (d[1]['Latitude'], d[1]['Longitude']) for d in df_sim_year.iterrows()
    ]

    # Calculate the distance in km to the nearest simulated hive
    logger.info(f'Adding distance feature to {year} training data...')
    df_train = add_distance_feature(df_train, sim_coords)

    # Setup
    model = LogisticRegression()

    # Prepare data
    Y = df_train['ID']
    x1 = np.array(df_train['Latitude'])
    x2 = np.array(df_train['Longitude'])
    x3 = np.array(df_train['Distance'])
    x4 = np.array(df_train['ts']) / 1e9
    if use_ts:
        X = np.array([x1, x2, x3, x4]).T
    else:
        X = np.array([x1, x2, x3]).T

    # Train the model
    model.fit(X, Y)
    logger.info(f'Training complete for {year} model')

    # Make predictions on the training set
    df_train['Probability'] = model.predict_proba(X).T[1]
    df_train.to_csv(f'./data/results/train_coupled_predictions_{year}.csv')

    # Prepare test data
    df_test = pd.read_csv(f'./data/test_{year}.csv')
    logger.info(f'Adding distance feature to {year} test data...')
    df_test = add_distance_feature(df_test, sim_coords)

    x1 = np.array(df_test['Latitude'])
    x2 = np.array(df_test['Longitude'])
    x3 = np.array(df_test['Distance'])
    x4 = np.array(df_test['ts']) / 1e9
    if use_ts:
        X = np.array([x1, x2, x3, x4]).T
    else:
        X = np.array([x1, x2, x3]).T

    # Make predictions on the test set
    df_test['Probability'] = model.predict_proba(X).T[1]
    df_test.to_csv(f'./data/results/test_coupled_predictions_{year}.csv')
    logger.info(f'Model complete for {year}')
