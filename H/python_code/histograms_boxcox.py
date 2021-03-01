from dateutil.parser import parse 
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
#plt.rcParams.update({'figure.figsize': (10, 7), 'figure.dpi': 120})

import scipy.stats as stats
from scipy.stats import normaltest
from scipy.stats import kurtosis
from scipy.stats import skew

def check_normalteste(series):
    #calculate
    stat, p = normaltest(series)
    print (f'Statistic={stat}, p={p}')
    print ('--'*25) 

    # interpret
    alpha = 0.05
    if p > alpha:
        print('Sample looks Gaussian (fail to reject H0)')
    else:
        print('Sample does not look Gaussian (reject H0)')

df = pd.read_csv('../timeserie_train.csv'
	, parse_dates=['data']
	, index_col='data'
	,squeeze=True)

def boxcox_series(timeserie):
    fitted_data, fitted_lambda = stats.boxcox(timeserie) 
    box_cox = pd.concat([pd.DataFrame(timeserie.index),pd.DataFrame(fitted_data)],ignore_index=True,axis=1)
    box_cox.rename(columns = {0:'data' ,1:'energia'}, inplace = True)
    box_cox["lambda"] = fitted_lambda
    box_cox.reset_index(drop=True, inplace=True)
    box_cox = box_cox.set_index('data')
    return box_cox


ts_box_cox = boxcox_series(df)

ts_box_cox.to_csv('../timeserie_box_cox_train.csv')


check_normalteste(ts_box_cox.energia)
sns.displot(ts_box_cox.energia, kde=True)
plt.title("Transformada BoxCox")
plt.show()

