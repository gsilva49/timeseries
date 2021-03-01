from pandas import read_csv
from sklearn.metrics import mean_absolute_percentage_error
from math import sqrt
from matplotlib import pyplot as plt
from pandas import concat
import numpy as np
import scipy.stats as stats
import pandas as pd

def persistence_one_step_ln(train_log, teste_log, 
    show_results=False, plot_result=False):
    # Prepare data
    teste_log = teste_log.values
    train_log = [x for x in train_log]

    # Walk-forward validation
    predictions = list()

    for i in range(len(teste_log)):
        # Predict
        yhat = train_log[-1]
        # Store forecast in list of predictions
        predictions.append(yhat)
        # Add actual observation to train for the next loop
        obs = teste_log[i]
        train_log.append(obs)
        
        if show_results:
            print('>Predicted=%.3f, Expected=%.3f' % (yhat, obs))


    # Report performance
    mape = mean_absolute_percentage_error(np.exp(teste_log), np.exp(predictions))
    print('MAPE: %.3f' % mape)
    # Plot predicted vs expected values
    if plot_result: 
        plt.plot(np.exp(teste_log))
        plt.plot(np.exp(predictions), color='red')
        plt.show()


# Load data
train_log = pd.read_csv('../timeserie_log_train.csv',
                     header=0, index_col=0, parse_dates=True, squeeze=True)
teste_log = pd.read_csv('../timeserie_log_test.csv',
                     header=0, index_col=0, parse_dates=True, squeeze=True)


persistence_one_step_ln(train_log, teste_log, plot_result=True)