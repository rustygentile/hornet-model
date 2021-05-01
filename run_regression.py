import logging
from src.regression import make_and_run_model

__author__ = 'Rusty Gentile'

logger = logging.getLogger(__name__)


if __name__ == '__main__':
    logging.basicConfig(
        format='%(asctime)s %(levelname)-8s %(message)s',
        level=logging.INFO,
        datefmt='%Y-%m-%d %H:%M:%S')

    make_and_run_model(2019)
    make_and_run_model(2020)
