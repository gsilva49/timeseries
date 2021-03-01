from pandas import read_csv
from sklearn.metrics import mean_absolute_percentage_error
from math import sqrt
from matplotlib import pyplot as plt
from pandas import concat
import numpy as np
import scipy.stats as stats
import pandas as pd
from pandas import Series

plt.rcParams.update({'figure.figsize': (10, 7), 'figure.dpi': 120})


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


def invert_diff_predicions(test, forecasts, n_steps):
    output = list()
    for i in range (len(forecasts)+1):
        output.append(np.zeros(n_steps))


    for i in range(n_steps):
        # Picking the values from multi-step forecasts
        ypred_ts = [forecast[i] for forecast in forecasts]
        # Sliding window on test series
        ytrue_ts = test[:len(ypred_ts)+1]
        ypred_ts = invert_difference(ytrue_ts,ypred_ts)

        for j in range(len(ypred_ts)):
            output[j][i] = ypred_ts[j]

    return output


# Plot the forecasts in the context of the original dataset
def plot_forecasts(series, forecasts, test):
    # Plot the entire dataset in blue
    plt.plot(series)
    # Plot the forecasts in red
    for i in range(len(forecasts)):
        # Start offset for x-axis
        off_s = len(series) - len(test) + i - 1
        # End offset for x-axis
        off_e = off_s + len(forecasts[i]) + 1
        # Indexes of x-axis for multi-step forecasts
        xaxis = [x for x in range(off_s, off_e)]
        # Values of muti-step fotecasts
        yaxis = forecasts[i]  
        yaxis = np.insert(yaxis,0,[series[off_s]])

        #print(len(forecasts[i]))
        #print((yaxis))
        #break

        plt.plot(xaxis, yaxis, color='red')

    # Show the final plot
    plt.show()  

def persistence_multi_step(train,test, train_orig, test_orig, steps=24, plot_result=False):

    # Concatenate train/test series for plotting
    series = concat([train_orig, test_orig], axis=0)
    # Prepare data
    test = test.values
    series = series.values
    train = [x for x in train]
    # Number of multi-step
    n_steps = steps
    # Store multi-step forecasts
    forecasts = list()
    # Number of multi-step forecasts
    n_forecasts = len(test) - n_steps + 1
    # Walk-forward validation
    for i in range(n_forecasts):
        # Make a multi-step forecast
        last_ob = train[-1]
        yhat = persistence(last_ob, n_steps)
        # Store the multi-step forecast
        forecasts.append(yhat)
        # Add actual observation to train for the next loop
        obs = test[i]
        train.append(obs)
    # Evaluate the 
    evaluate_forecasts(test_orig, forecasts, n_steps)
    # Plot the forecasts
    if plot_result:
        forecasts = invert_diff_predicions(test_orig, forecasts, n_steps)
        plot_forecasts(series, forecasts, test_orig)


# Evaluate the MAPE for each forecast time step
def evaluate_forecasts(test, forecasts, n_steps):
    for i in range(n_steps):
        # Picking the values from multi-step forecasts
        ypred_ts = [forecast[i] for forecast in forecasts]
        # Sliding window on test series
        ytrue_ts = test[i:len(ypred_ts)+i+1]
        ypred_ts = invert_difference(ytrue_ts,ypred_ts)
        print('t+%d MAPE: %f' % ((i+1), (mean_absolute_percentage_error(ytrue_ts, ypred_ts))))


# Make a multi-step persistence forecast
def persistence(last_ob, n_steps):
    return [last_ob for i in range(n_steps)]


# Load data
train = pd.read_csv('../timeserie_train.csv',
                     header=0, index_col=0, parse_dates=True, squeeze=True)
test = pd.read_csv('../timeserie_test.csv',
                     header=0, index_col=0, parse_dates=True, squeeze=True)

ts_diff_train = difference(train)
ts_diff_test = difference(test)


persistence_multi_step(ts_diff_train, ts_diff_test, train, test, steps=24, 
    plot_result=True)