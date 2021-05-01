import geopandas as geo
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib
from matplotlib import cm

__author__ = 'Rusty Gentile'

matplotlib.rcParams.update({'font.size': 12})
states = geo.read_file('./data/states_reduced/states_reduced.shp')
k = 3

fig, ax = plt.subplots(1, 1)
states.plot(alpha=0.2, edgecolor='black', ax=ax)

df_sim = pd.read_csv(f'./data/results/results_aggr_sim_{k}.csv')
xs = df_sim['Longitude']
ys = df_sim['Latitude']
ax.scatter(xs, ys, c='g', s=2, alpha=0.4, label=f'Simulated Population')

df_model = pd.read_csv(f'./data/results/test_predictions_2020.csv')
x = df_model['Longitude']
y = df_model['Latitude']
p = df_model['Probability']
ax.scatter(x, y, c=p, s=2, label='Unconfirmed Sightings', cmap=cm.get_cmap('hot'))

norm = matplotlib.colors.Normalize(vmin=min(p), vmax=max(p))
m_cmap = cm.ScalarMappable(norm=norm, cmap=cm.get_cmap('hot'))
cb = fig.colorbar(m_cmap, ax=ax, orientation='vertical', fraction=0.046, pad=0.04)
cb.set_label('Probability')

lgnd = plt.legend(loc="lower left", numpoints=1)
lgnd.legendHandles[0]._sizes = [30]
lgnd.legendHandles[1]._sizes = [30]
lgnd.legendHandles[0]._alpha = 1
lgnd.legendHandles[1]._alpha = 1

plt.show()
