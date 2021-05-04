import geopandas as geo
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib
import matplotlib.ticker as ticker

__author__ = 'Rusty Gentile'

matplotlib.rcParams.update({'font.size': 10})


def plot_all():
    states = geo.read_file('./data/states_reduced/states_reduced.shp')
    n_sims = 10

    for k in range(n_sims):

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


def plot_selected():
    states = geo.read_file('./data/states_reduced/states_reduced.shp')
    fig, ax = plt.subplots(1, 2, figsize=(10, 4))

    states.plot(alpha=0.4, edgecolor='black', ax=ax[0])
    states.plot(alpha=0.4, edgecolor='black', ax=ax[1])

    # Selected simulations
    cons_k = 9
    agg_k = 4

    df_agg = pd.read_csv(f'./data/results/results_aggr_sim_{agg_k-1}.csv')
    df_cons = pd.read_csv(f'./data/results/results_cons_sim_{cons_k-1}.csv')

    for y in range(2019, 2024):
        df_y_cons = df_cons[df_cons['year'] == y]
        xs_cons = df_y_cons['Longitude']
        ys_cons = df_y_cons['Latitude']
        ax[0].scatter(xs_cons, ys_cons, s=2, label=f'{y} : N = {len(xs_cons)}')
        ax[0].set_title(f'Conservative Simulation #: {cons_k}')
        ax[0].set_xlim(left=-125, right=-121)
        ax[0].set_ylim(bottom=47.5, top=50)
        ax[0].xaxis.set_major_formatter(ticker.FormatStrFormatter('%d'))
        ax[0].legend()

        df_y_agg = df_agg[df_agg['year'] == y]
        xs_agg = df_y_agg['Longitude']
        ys_agg = df_y_agg['Latitude']
        ax[1].scatter(xs_agg, ys_agg, s=2, label=f'{y} : N = {len(xs_agg)}')
        ax[1].set_title(f'Aggressive Simulation #: {agg_k}')
        ax[1].set_xlim(left=-125, right=-121)
        ax[1].set_ylim(bottom=47.5, top=50)
        ax[1].xaxis.set_major_formatter(ticker.FormatStrFormatter('%d'))
        ax[1].legend()

    fig.savefig('./images/simulation_results_geo.png')
    plt.show()


plot_selected()
