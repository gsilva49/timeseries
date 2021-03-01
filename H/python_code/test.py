from dateutil.parser import parse 
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
#plt.rcParams.update({'figure.figsize': (10, 7), 'figure.dpi': 120})

from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.stattools import kpss

def ADF_test(timeseries):
	print('Results of Dickey-Fuller Test:')
	result = adfuller(timeseries, autolag='AIC')
	print(f'ADF Statistic: {result[0]}')
	print(f'p-value: {result[1]}')
	for key, value in result[4].items():
		print('Critial Values:')
		print(f'   {key}, {value}')


def KPSS(timeseries):
	print('\nResults of KPSS Test:')
	result = kpss(timeseries, regression='c')
	print('KPSS Statistic: %f' % result[0])
	print('p-value: %f' % result[1])
	for key, value in result[3].items():
		print('Critial Values:')
		print(f'   {key}, {value}')

df = pd.read_csv('../timeserie_train.csv'
	, parse_dates=['data']
	, index_col='data')

ADF_test(df)
KPSS(df)

#timeserie_box_cox_train
#timeserie_log_train




