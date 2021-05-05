import pandas as pd
import numpy as np
import logging
from src.simulate import simulate

__author__ = 'Rusty Gentile'

logger = logging.getLogger(__name__)


def run_conservative_sim():

    df = pd.read_csv('./data/train_2019.csv')
    df = df[df['ID'] == 1]

    lats = df['Latitude']
    longs = df['Longitude']
    coords = [(lats.iloc[i], longs.iloc[i]) for i in range(len(longs))]
    n_sim = 10

    conservative_parameters = {
        'p_survival': 0.4,
        'p_queen_survival': 0.1,
        'new_queens': 30,
        'dispersal_range': 5e3
    }

    for i in range(n_sim):
        logger.info(f'Starting conservative simulation: {i}')
        results = simulate(coords, 2019, 5,
                           hive_parameters=conservative_parameters,
                           shape_file='./data/states_reduced/states_reduced.shp')
        results.to_csv(f'./data/results/results_cons_sim_{i}.csv')


def run_aggressive_sim():

    df1 = pd.read_csv('./data/train_2019.csv')
    df1 = df1[df1['ID'] == 1]

    df2 = pd.read_csv('./data/train_2020.csv')
    df2 = df2[df2['ID'] == 1]

    df = pd.concat([df1, df2])

    lats = df['Latitude']
    longs = df['Longitude']
    coords = [(lats.iloc[i], longs.iloc[i]) for i in range(len(longs))]
    n_sim = 10

    aggressive_parameters = {
        'p_survival': 0.6,
        'p_queen_survival': 0.15,
        'new_queens': 30,
        'dispersal_range': 10e3
    }

    for i in range(n_sim):
        logger.info(f'Starting aggressive simulation: {i}')
        results = simulate(coords, 2019, 5,
                           hive_parameters=aggressive_parameters,
                           shape_file='./data/states_reduced/states_reduced.shp')

        results.to_csv(f'./data/results/results_aggr_sim_{i}.csv')


if __name__ == '__main__':
    logging.basicConfig(
        format='%(asctime)s %(levelname)-8s %(message)s',
        level=logging.INFO,
        datefmt='%Y-%m-%d %H:%M:%S')

    run_conservative_sim()
    run_aggressive_sim()
