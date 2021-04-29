import pandas as pd
import numpy as np
import datetime as dt


def clean_date(s, year=None):
    """Used to filter the data only for the selected year"""
    try:
        d = dt.datetime.strptime(str(s), '%Y-%m-%d %H:%M:%S')
        if d.year == year:
            return d.timestamp()
        else:
            return np.nan
    except ValueError:
        return np.nan


def make_training_set(year):
    df = pd.read_excel('../data/2021MCMProblemC_DataSet.xlsx', engine='openpyxl')

    # We are only interested in data that has been ID'd
    df_train = df[df['Lab Status'].str.endswith('ID')]

    # Add a column based on the lab results: 1=positive, 0=negative
    df_train['ID'] = df_train['Lab Status'].apply(lambda s: int(s.startswith('P')))

    df_train['ts'] = df_train['Detection Date'].apply(clean_date, year=year)
    return df_train.dropna()


def main():
    df_19 = make_training_set(2019)
    df_20 = make_training_set(2020)

    df_19.to_csv('../data/train_2019.csv')
    df_20.to_csv('../data/train_2020.csv')


if __name__ == '__main__':
    main()
