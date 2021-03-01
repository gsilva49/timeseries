from pandas import read_csv
from sklearn.metrics import mean_absolute_percentage_error
from math import sqrt
from matplotlib import pyplot as plt
from pandas import concat
import numpy as np
import scipy.stats as stats
import pandas as pd


def boxcox_series(timeserie):
    fitted_data, fitted_lambda = stats.boxcox(timeserie) 
    box_cox = pd.concat([pd.DataFrame(timeserie.index),pd.DataFrame(fitted_data)],ignore_index=True,axis=1)
    box_cox.rename(columns = {0:'data' ,1:'energia'}, inplace = True)
    box_cox["lambda"] = fitted_lambda
    box_cox.reset_index(drop=True, inplace=True)
    box_cox = box_cox.set_index('data')
    return box_cox

#Split time series into a training/test
def split_to_train_test(series, test_percent=0.50):
    split_point = int(test_percent * len(series))
    return series[:-split_point], series[-split_point:]

# Load data
df = pd.read_csv('../timeserie_prepro.csv',
                     header=0, index_col=0, parse_dates=True, squeeze=True)

ts_box_cox = boxcox_series(df)

train_box_cox, test_box_cox = split_to_train_test(ts_box_cox, test_percent=0.25)

train_box_cox.to_csv('../timeserie_box_cox_train.csv')
test_box_cox.to_csv('../timeserie_box_cox_test.csv')
