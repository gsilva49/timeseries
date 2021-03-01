# Evaluate a univariate persistence model
import pandas as pd
from pandas import read_csv
from sklearn.metrics import mean_squared_error
from math import sqrt
from matplotlib import pyplot as plt
import scipy.stats as stats
from scipy.special import inv_boxcox

plt.rcParams.update({'figure.figsize': (10, 7), 'figure.dpi': 120})


#Split time series into a training/test
def split_to_train_test(series, test_percent=0.50):
    split_point = int(test_percent * len(series))
    return series[:-split_point], series[-split_point:]

#Select a percentage from the time series
def data_proportion(series, percent=1.0, from_end=True):
    if from_end:
        series = series[-int(percent * len(series)):]
    else:
        series = series[:int(percent * len(series))]
    return series

#load data
series = read_csv('../timeserie_prepro.csv', 
                  parse_dates=['data'], 
                  index_col='data',
                  squeeze=True)
print(f'Total data: {len(series)}')

series_per = data_proportion(series, percent=.5, from_end=True)
print(f'Percentage data: {len(series_per)}')

series_per_bc , series_per_lambda = stats.boxcox(series_per) 

for i in range(series_per.size):
     series_per[i] = series_per_bc[i]


#split data
train_bc, test_bc = split_to_train_test(series_per, test_percent=0.40)
print('Training %d, Teste %d' % (len(train_bc), len(test_bc)))

# Prepare data
test_bc = test_bc.values
train_bc = [x for x in train_bc]

# Walk-forward validation
predictions = list()

for i in range(len(test_bc)):
    # Predict
    yhat = train_bc[-1]
    # Store forecast in list of predictions
    predictions.append(yhat)
    # Add actual observation to train for the next loop
    obs = test_bc[i]
    train_bc.append(obs)
    #print('>Predicted=%.3f, Expected=%.3f' % (yhat, obs))

test = inv_boxcox(test_bc, series_per_lambda)
predictions = inv_boxcox(predictions, series_per_lambda)

# Report performance
rmse = sqrt(mean_squared_error(test, predictions))
print('RMSE: %.3f' % rmse)
# Plot predicted vs expected values
plt.plot(test)
plt.plot(predictions, color='red')
plt.show()

#RMSE: 494.274 boxcox





