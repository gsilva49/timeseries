from pandas import read_csv
from sklearn.metrics import mean_absolute_percentage_error
from math import sqrt
from matplotlib import pyplot as plt
from pandas import concat
import numpy as np
import scipy.stats as stats
import pandas as pd
import scipy.special as special 

def persistence_one_step_box_cox(train_box_cox, test_box_cox, 
    show_results=False, plot_result=False):
    # Prepare data
    lbda = train_box_cox["lambda"][0]
    test_box_cox = test_box_cox.energia.values
    train_box_cox = [x for x in train_box_cox.energia]

    # Walk-forward validation
    predictions = list()

    for i in range(len(test_box_cox)):
        # Predict
        yhat = train_box_cox[-1]
        # Store forecast in list of predictions
        predictions.append(yhat)
        # Add actual observation to train for the next loop
        obs = test_box_cox[i]
        train_box_cox.append(obs)
        
        if show_results:
            print('>Predicted=%.3f, Expected=%.3f' % (yhat, obs))

    # Report performance
    test = special.inv_boxcox(test_box_cox, lbda)
    pred = special.inv_boxcox(predictions, lbda)
    mape = mean_absolute_percentage_error(test, pred)
    print('MAPE: %.3f' % mape)
    # Plot predicted vs expected values
    if plot_result: 
        plt.plot(special.inv_boxcox(test_box_cox, lbda))
        plt.plot(special.inv_boxcox(predictions, lbda), color='red')
        plt.show()


# Load data
train_box_cox = pd.read_csv('../timeserie_box_cox_train.csv',
                     header=0, index_col=0, parse_dates=True, squeeze=True)
test_box_cox = pd.read_csv('../timeserie_box_cox_test.csv',
                     header=0, index_col=0, parse_dates=True, squeeze=True)


persistence_one_step_box_cox(train_box_cox, test_box_cox, plot_result=True)