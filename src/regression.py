import logging
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression

__author__ = 'Rusty Gentile'
logger = logging.getLogger(__name__)


def make_and_run_model(year, use_ts=False):
    """
    Make a simple logistic regression model using coordinate data and
    timestamps. Then run it on the test data sets.
    """

    # Setup
    model = LogisticRegression()
    df_train = pd.read_csv(f'./data/train_{year}.csv')

    # Prepare data
    Y = df_train['ID']
    x1 = np.array(df_train['Latitude'])
    x2 = np.array(df_train['Longitude'])
    x3 = np.array(df_train['ts'])
    if use_ts:
        X = np.array([x1, x2, x3]).T
    else:
        X = np.array([x1, x2]).T

    # Train the model
    model.fit(X, Y)
    logger.info(f'Training complete for {year} model')

    # Make predictions on the training set
    df_train['Probability'] = model.predict_proba(X).T[1]
    df_train.to_csv(f'./data/results/train_predictions_{year}.csv')

    # Read in the test data
    df_test = pd.read_csv(f'./data/test_{year}.csv')
    x1 = np.array(df_test['Latitude'])
    x2 = np.array(df_test['Longitude'])
    x3 = np.array(df_test['ts'])
    if use_ts:
        X = np.array([x1, x2, x3]).T
    else:
        X = np.array([x1, x2]).T

    # Make predictions on the test data
    df_test['Probability'] = model.predict_proba(X).T[1]
    df_train.to_csv(f'./data/results/test_predictions_{year}.csv')
