import logging
from src.regression import make_and_run_model as run_model
from src.coupled import make_and_run_model as run_coupled


__author__ = 'Rusty Gentile'

logger = logging.getLogger(__name__)


if __name__ == '__main__':
    logging.basicConfig(
        format='%(asctime)s %(levelname)-8s %(message)s',
        level=logging.INFO,
        datefmt='%Y-%m-%d %H:%M:%S')

    run_model(2019)
    run_model(2020)

    run_coupled(2019, './data/results/results_aggr_sim_1.csv', 2023)
    run_coupled(2020, './data/results/results_aggr_sim_1.csv', 2023)
