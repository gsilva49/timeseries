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


ts_temp_log = np.log(df)
check_normalteste(ts_temp_log)

ts_temp_log.to_csv('../timeserie_log_train.csv')

sns.displot(ts_temp_log, kde=True)
plt.title("Transformada Ln")
plt.show()

#sns.displot(ts_temp_log, kde=True).set(title="Transformada Ln")
plt.show()
