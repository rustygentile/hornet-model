import matplotlib.pyplot as plt
import pandas as pd
import matplotlib
import matplotlib.ticker as ticker

__author__ = 'Rusty Gentile'

matplotlib.rcParams.update({'font.size': 10})
n_sims = 10
n_years = 5

fig, ax = plt.subplots(1, 2, figsize=(10, 4))

for k in range(n_sims):
    df_sim = pd.read_csv(f'./data/results/results_cons_sim_{k}.csv')
    gb_sim = df_sim.groupby('year')
    ax[0].plot(gb_sim['year'].count(), label=f'sim #{k+1}')


ax[0].xaxis.set_major_locator(ticker.MaxNLocator(n_years))
ax[0].xaxis.set_major_formatter(ticker.FormatStrFormatter('%d'))
ax[0].set_xlabel('Year')
ax[0].set_ylabel('N Hives')
ax[0].set_title('Conservative Assumptions')
ax[0].legend()


for k in range(n_sims):
    df_sim = pd.read_csv(f'./data/results/results_aggr_sim_{k}.csv')
    gb_sim = df_sim.groupby('year')
    ax[1].plot(gb_sim['year'].count(), label=f'sim #{k+1}')

ax[1].xaxis.set_major_locator(ticker.MaxNLocator(n_years))
ax[1].xaxis.set_major_formatter(ticker.FormatStrFormatter('%d'))
ax[1].set_xlabel('Year')
ax[1].set_ylabel('N Hives')
ax[1].set_title('Aggressive Assumptions')
ax[1].legend()

fig.savefig('./images/simulation_results.png')
plt.show()
