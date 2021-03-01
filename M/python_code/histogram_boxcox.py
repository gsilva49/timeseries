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

test = pd.read_csv('../timeserie_test.csv'
    , parse_dates=['data']
    , index_col='data'
    ,squeeze=True)


fitted_data, fitted_lambda = stats.boxcox(df) 
print("fitted_lambda")

bc_test = pd.DataFrame(stats.boxcox(test)[0])
bc_test.to_csv('../bc_data_test.csv', header=None)

print(fitted_lambda)
print(stats.boxcox(test)[1])



check_normalteste(fitted_data)

bc = pd.DataFrame(fitted_data)
bc.to_csv('../bc_data.csv', header=None)

sns.kdeplot(df, shade=True, label='Dado')
sns.kdeplot(fitted_data, shade=True, label='Box-Cox')
plt.legend(loc='upper right')
plt.title("Transfor Box-Cox")
plt.show()
