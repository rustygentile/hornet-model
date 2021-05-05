import geopandas as geo
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib
from matplotlib import cm

__author__ = 'Rusty Gentile'
matplotlib.rcParams.update({'font.size': 14})


def plot_models(sim_year=None, sim_k=None):
    """
    Plots the regression model and simulation results together.
    """

    fig, ax = plt.subplots(1, 2, figsize=(14, 5))

    # Plot the geography
    states = geo.read_file('./data/states_reduced/states_reduced.shp')
    states.plot(alpha=0.2, edgecolor='black', ax=ax[0])
    states.plot(alpha=0.2, edgecolor='black', ax=ax[1])

    if sim_year:
        # Plot the simulation data
        df_sim = pd.read_csv(f'./data/results/results_aggr_sim_{sim_k-1}.csv')
        df_sim = df_sim[df_sim['year'] == sim_year]
        xs = df_sim['Longitude']
        ys = df_sim['Latitude']
        ax[0].scatter(xs, ys, c='g', s=2, alpha=0.4, label=f'Simulated Population')
        ax[1].scatter(xs, ys, c='g', s=2, alpha=0.4, label=f'Simulated Population')

    # Plot the regression model results
    if sim_year:
        df_model_2019 = pd.read_csv('./data/results/test_coupled_predictions_2019.csv')
        df_model_2020 = pd.read_csv('./data/results/test_coupled_predictions_2020.csv')
    else:
        df_model_2019 = pd.read_csv('./data/results/test_predictions_2019.csv')
        df_model_2020 = pd.read_csv('./data/results/test_predictions_2020.csv')

    df_train_2019 = pd.read_csv('./data/train_2019.csv')
    df_train_2020 = pd.read_csv('./data/train_2020.csv')

    x_unvf_2019 = df_model_2019['Longitude']
    y_unvf_2019 = df_model_2019['Latitude']
    p_unvf_2019 = df_model_2019['Probability']

    x_unvf_2020 = df_model_2020['Longitude']
    y_unvf_2020 = df_model_2020['Latitude']
    p_unvf_2020 = df_model_2020['Probability']

    x_conf_2019 = df_train_2019[df_train_2019['ID'] == 1]['Longitude']
    y_conf_2019 = df_train_2019[df_train_2019['ID'] == 1]['Latitude']
    x_conf_2020 = df_train_2020[df_train_2020['ID'] == 1]['Longitude']
    y_conf_2020 = df_train_2020[df_train_2020['ID'] == 1]['Latitude']

    ax[0].scatter(x_unvf_2019, y_unvf_2019, c=p_unvf_2019, s=2,
                  label=f'Unconfirmed Sightings',
                  cmap=cm.get_cmap('plasma'))
    ax[0].scatter(x_conf_2019, y_conf_2019, s=15, marker='o', c='w',
                  edgecolor='black', label='Positive IDs')
    ax[0].set_xlim(left=-126, right=-116)
    ax[0].set_ylim(bottom=44, top=50)

    ax[1].scatter(x_unvf_2020, y_unvf_2020, c=p_unvf_2020, s=2,
                  label=f'Unconfirmed Sightings',
                  cmap=cm.get_cmap('plasma'))
    ax[1].scatter(x_conf_2020, y_conf_2020, s=15, marker='o', c='w',
                  edgecolor='black', label='Positive IDs')
    ax[1].set_xlim(left=-126, right=-116)
    ax[1].set_ylim(bottom=44, top=50)

    # Add the colorbars
    norm_2019 = matplotlib.colors.Normalize(vmin=min(p_unvf_2019),
                                            vmax=max(p_unvf_2019))
    cb19 = fig.colorbar(cm.ScalarMappable(norm=norm_2019,
                                          cmap=cm.get_cmap('plasma')),
                        ax=ax[0], orientation='vertical', fraction=0.046, pad=0.04)
    cb19.set_label('Probability')

    norm_2020 = matplotlib.colors.Normalize(vmin=min(p_unvf_2020),
                                            vmax=max(p_unvf_2020))
    cb20 = fig.colorbar(cm.ScalarMappable(norm=norm_2020,
                                          cmap=cm.get_cmap('plasma')),
                        ax=ax[1], orientation='vertical', fraction=0.046, pad=0.04)
    cb20.set_label('Probability')

    # Add the legend and adjust the size of its points
    legend_2019 = ax[0].legend(loc="lower left", numpoints=1)
    legend_2020 = ax[1].legend(loc="lower left", numpoints=1)
    legend_2019.legendHandles[0]._sizes = [30]
    legend_2019.legendHandles[1]._sizes = [30]
    legend_2019.legendHandles[0]._alpha = 1
    legend_2019.legendHandles[1]._alpha = 1
    legend_2020.legendHandles[0]._sizes = [30]
    legend_2020.legendHandles[1]._sizes = [30]
    legend_2020.legendHandles[0]._alpha = 1
    legend_2020.legendHandles[1]._alpha = 1
    if sim_year:
        legend_2019.legendHandles[2]._sizes = [30]
        legend_2019.legendHandles[2]._alpha = 1
        legend_2020.legendHandles[2]._sizes = [30]
        legend_2020.legendHandles[2]._alpha = 1

    ax[0].set_title('2019')
    ax[1].set_title('2020')
    return fig


if __name__ == '__main__':
    plot_models().savefig('./images/regression_results.png')
    plot_models(sim_k=9, sim_year=2023).savefig('./images/feature_generation.png')
    plt.show()
