from pandas import read_csv
from sklearn.metrics import mean_absolute_percentage_error
from math import sqrt
from matplotlib import pyplot as plt
from pandas import concat
import numpy as np
import scipy.stats as stats
import pandas as pd

def persistence_one_step(train, test, show_results=False, plot_result=False):
    # Prepare data
    test = test.values
    train = [x for x in train]
    
    # Walk-forward validation
    predictions = list()
    
    for i in range(len(test)):
        # Predict
        yhat = train[-1]
        # Store forecast in list of predictions
        predictions.append(yhat)
        # Add actual observation to train for the next loop
        obs = test[i]
        train.append(obs)
        if show_results:
            print('>Predicted=%.3f, Expected=%.3f' % (yhat, obs))
        
    # Report performance
    mape = mean_absolute_percentage_error(test, predictions)
    print('MAPE: %.3f' % mape)
    # Plot predicted vs expected values
    if plot_result: 
        plt.plot(test)
        plt.plot(predictions, color='red')
        plt.show()


# Load data
train = pd.read_csv('../timeserie_train.csv',
                     header=0, index_col=0, parse_dates=True, squeeze=True)
test = pd.read_csv('../timeserie_test.csv',
                     header=0, index_col=0, parse_dates=True, squeeze=True)

persistence_one_step(train, test, plot_result=True)