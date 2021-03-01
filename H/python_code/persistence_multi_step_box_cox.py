from pandas import read_csv
from sklearn.metrics import mean_absolute_percentage_error
from math import sqrt
from matplotlib import pyplot as plt
from pandas import concat
import numpy as np
import scipy.stats as stats
import pandas as pd
import scipy.special as special 


plt.rcParams.update({'figure.figsize': (10, 7), 'figure.dpi': 120})

# Plot the forecasts in the context of the original dataset
def plot_forecasts(series, forecasts, test, lbda):
    # Plot the entire dataset in blue
    plt.plot(special.inv_boxcox(series, lbda))
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
        plt.plot(xaxis, special.inv_boxcox(yaxis, lbda), color='red')
    # Show the final plot
    plt.show()      

def persistence_multi_step(train,test, steps=24, plot_result=False):

    # Concatenate train/test series for plotting
    series = concat([train.energia, test.energia], axis=0)
    # Prepare data
    lbda = train["lambda"][0]
    test = test.energia.values
    series = series.values
    train = [x for x in train.energia]
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
    # Evaluate the forecasts
    evaluate_forecasts(special.inv_boxcox(test, lbda), 
        special.inv_boxcox(forecasts, lbda), n_steps)
    # Plot the forecasts
    if plot_result:
        plot_forecasts(series, forecasts, test, lbda)


# Evaluate the MAPE for each forecast time step
def evaluate_forecasts(test, forecasts, n_steps):
    for i in range(n_steps):
        # Picking the values from multi-step forecasts
        ypred_ts = [forecast[i] for forecast in forecasts]
        # Sliding window on test series
        ytrue_ts = test[i:len(ypred_ts)+i]
        print('t+%d MAPE: %f' % ((i+1), (mean_absolute_percentage_error(ytrue_ts, ypred_ts))))


# Make a multi-step persistence forecast
def persistence(last_ob, n_steps):
    return [last_ob for i in range(n_steps)]

# Load data
train_box_cox = pd.read_csv('../timeserie_box_cox_train.csv',
                     header=0, index_col=0, parse_dates=True, squeeze=True)
test_box_cox = pd.read_csv('../timeserie_box_cox_test.csv',
                     header=0, index_col=0, parse_dates=True, squeeze=True)


persistence_multi_step(train_box_cox, test_box_cox, steps=24, plot_result=True)