# Evaluate a univariate persistence model
from pandas import read_csv
from sklearn.metrics import mean_squared_error
from math import sqrt
from matplotlib import pyplot as plt
from pandas import concat
import numpy as np
import scipy.stats as stats
import pandas as pd

plt.rcParams.update({'figure.figsize': (10, 7), 'figure.dpi': 120})

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
        yaxis = [series[off_s]] + forecasts[i]  
        plt.plot(xaxis, yaxis, color='red')
    # Show the final plot
    plt.show()          

# Evaluate the RMSE for each forecast time step
def evaluate_forecasts(test, forecasts, n_steps):
    for i in range(n_steps):
        # Picking the values from multi-step forecasts
        ypred_ts = [forecast[i] for forecast in forecasts]
        # Sliding window on test series
        ytrue_ts = test[i:len(ypred_ts)+i]
        print('t+%d RMSE: %f' % ((i+1), sqrt(mean_squared_error(ytrue_ts, ypred_ts))))


# Make a multi-step persistence forecast
def persistence(last_ob, n_steps):
    return [last_ob for i in range(n_steps)]


# Load data
train = read_csv('../timeserie_train.csv',
                     header=0, index_col=0, parse_dates=True, squeeze=True)
test = read_csv('../timeserie_test.csv',
                     header=0, index_col=0, parse_dates=True, squeeze=True)


# Concatenate train/test series for plotting
series = concat([train, test], axis=0)
# Prepare data
test = test.values
series = series.values
train = [x for x in train]
# Number of multi-step
n_steps = 24
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
# Evaluate the forecasts
evaluate_forecasts(test, forecasts, n_steps)
# Plot the forecasts
#plot_forecasts(series, forecasts, test)


