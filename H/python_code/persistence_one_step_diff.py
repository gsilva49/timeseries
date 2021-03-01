from pandas import read_csv
from sklearn.metrics import mean_absolute_percentage_error
from math import sqrt
from matplotlib import pyplot as plt
from pandas import concat
import numpy as np
import scipy.stats as stats
import pandas as pd
from pandas import Series

# difference a series
def difference(train):
    diff = list()
    # lose first value
    for i in range(1, len(train)):
        # substract the current value and its prior value 
        value = train[i] - train[i - 1]
        diff.append(value)
    diff = Series(diff)
    diff.index = train.index[1:]
    return diff


# invert a differenced series 
def invert_difference(train, diff):
    series = []
    # add first value
    series.append(train[0])
    for idx in range(len(diff)):
        # sum the current value and its prior value 
        series.append(diff[idx] + train[idx])
    series = Series(series)
    series.index = train.index
    return series


def persistence_one_step_diff(ts_diff_train, ts_diff_test, 
	test, show_results=False, plot_result=False):

    # Prepare data
    ts_diff_test = ts_diff_test.values
    ts_diff_train = [x for x in ts_diff_train]

    # Walk-forward validation
    predictions = list()

    for i in range(len(ts_diff_test)):
        # Predict
        yhat = ts_diff_train[-1]
        # Store forecast in list of predictions
        predictions.append(yhat)
        # Add actual observation to train for the next loop
        obs = ts_diff_test[i]
        ts_diff_train.append(obs)
        
        if show_results:
            print('>Predicted=%.3f, Expected=%.3f' % (yhat, obs))


    # Report performance
    mape = mean_absolute_percentage_error(test, invert_difference(test, predictions))
    print('MAPE: %.3f' % mape)
    # Plot predicted vs expected values
    if plot_result: 
        plt.plot(test)
        plt.plot(invert_difference(test, predictions), color='red')
        plt.show()


# Load data
train = pd.read_csv('../timeserie_train.csv',
                     header=0, index_col=0, parse_dates=True, squeeze=True)
test = pd.read_csv('../timeserie_test.csv',
                     header=0, index_col=0, parse_dates=True, squeeze=True)

ts_diff_train = difference(train)
ts_diff_test = difference(test)


persistence_one_step_diff(ts_diff_train, ts_diff_test, test)

