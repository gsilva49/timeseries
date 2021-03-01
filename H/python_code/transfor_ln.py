from pandas import read_csv
from sklearn.metrics import mean_absolute_percentage_error
from math import sqrt
from matplotlib import pyplot as plt
from pandas import concat
import numpy as np
import scipy.stats as stats
import pandas as pd

# Load data
train = pd.read_csv('../timeserie_train.csv',
                     header=0, index_col=0, parse_dates=True, squeeze=True)
test = pd.read_csv('../timeserie_test.csv',
                     header=0, index_col=0, parse_dates=True, squeeze=True)


train_log = np.log(train)
test_log = np.log(test)

train_log.to_csv('../timeserie_log_train.csv')
test_log.to_csv('../timeserie_log_test.csv')
