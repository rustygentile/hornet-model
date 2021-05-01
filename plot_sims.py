import geopandas as geo
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib

__author__ = 'Rusty Gentile'

matplotlib.rcParams.update({'font.size': 8})
states = geo.read_file('./data/states_reduced/states_reduced.shp')
n_sims = 10

for k in range(10):

    df_sim = pd.read_csv(f'./data/results/results_aggr_sim_{k}.csv')
    ax = states.plot(alpha=0.4, edgecolor='black')

    for y in range(2019, 2024):
        df_y = df_sim[df_sim['year'] == y]
        xs = df_y['Longitude']
        ys = df_y['Latitude']
        ax.scatter(xs, ys, s=2, label=f'{y} : N = {len(xs)}')

    plt.title(f'Simulation #: {k}')
    plt.legend()

plt.show()
