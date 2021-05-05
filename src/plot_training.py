import geopandas as geo
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib

__author__ = 'Rusty Gentile'
matplotlib.rcParams.update({'font.size': 14})

fig, ax = plt.subplots(1, 2, figsize=(14, 5))

states = geo.read_file('./data/states_reduced/states_reduced.shp')
states.plot(alpha=0.2, edgecolor='black', ax=ax[0])
states.plot(alpha=0.2, edgecolor='black', ax=ax[1])

df_train_2019 = pd.read_csv('./data/train_2019.csv')
df_test_2019 = pd.read_csv('./data/test_2019.csv')
df_train_2020 = pd.read_csv('./data/train_2020.csv')
df_test_2020 = pd.read_csv('./data/test_2020.csv')

pos_x_2019 = df_train_2019[df_train_2019['ID'] == 1]['Longitude']
pos_y_2019 = df_train_2019[df_train_2019['ID'] == 1]['Latitude']
neg_x_2019 = df_train_2019[df_train_2019['ID'] == 0]['Longitude']
neg_y_2019 = df_train_2019[df_train_2019['ID'] == 0]['Latitude']
unv_x_2019 = df_test_2019['Longitude']
unv_y_2019 = df_test_2019['Latitude']

pos_x_2020 = df_train_2020[df_train_2020['ID'] == 1]['Longitude']
pos_y_2020 = df_train_2020[df_train_2020['ID'] == 1]['Latitude']
neg_x_2020 = df_train_2020[df_train_2020['ID'] == 0]['Longitude']
neg_y_2020 = df_train_2020[df_train_2020['ID'] == 0]['Latitude']
unv_x_2020 = df_test_2020['Longitude']
unv_y_2020 = df_test_2020['Latitude']

ax[0].scatter(unv_x_2019, unv_y_2019, s=10, label='Unverified')
ax[0].scatter(neg_x_2019, neg_y_2019, s=5, label='Negative IDs')
ax[0].scatter(pos_x_2019, pos_y_2019, s=15, marker='o', c='w', edgecolor='black', label='Positive IDs')
ax[0].set_title('2019 Sightings')
ax[0].set_xlim(left=-126, right=-116)
ax[0].set_ylim(bottom=44, top=50)
ax[0].legend()

ax[1].scatter(unv_x_2020, unv_y_2020, s=10, label='Unverified')
ax[1].scatter(neg_x_2020, neg_y_2020, s=5, label='Negative IDs')
ax[1].scatter(pos_x_2020, pos_y_2020, s=15, marker='o', c='w', edgecolor='black', label='Positive IDs')
ax[1].set_title('2020 Sightings')
ax[1].set_xlim(left=-126, right=-116)
ax[1].set_ylim(bottom=44, top=50)
ax[1].legend()

legend_2019 = ax[0].legend(loc="lower left", numpoints=1)
legend_2019.legendHandles[0]._sizes = [30]
legend_2019.legendHandles[1]._sizes = [30]
legend_2019.legendHandles[2]._sizes = [30]
legend_2019.legendHandles[0]._alpha = 1
legend_2019.legendHandles[1]._alpha = 1
legend_2019.legendHandles[2]._alpha = 1

legend_2020 = ax[1].legend(loc="lower left", numpoints=1)
legend_2020.legendHandles[0]._sizes = [30]
legend_2020.legendHandles[1]._sizes = [30]
legend_2020.legendHandles[2]._sizes = [30]
legend_2020.legendHandles[0]._alpha = 1
legend_2020.legendHandles[1]._alpha = 1
legend_2020.legendHandles[2]._alpha = 1

fig.savefig('./images/training_data.png')

if __name__ == '__main__':
    plt.show()
