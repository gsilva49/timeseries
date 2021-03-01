from statsmodels.tsa.seasonal import seasonal_decompose
from dateutil.parser import parse
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('../timeserie_train.csv', 
	parse_dates=['data'], 
	index_col='data',
	squeeze=True)

# Multiplicative Decomposition 
result_mul = seasonal_decompose(df, model='multiplicative', period=365*24, extrapolate_trend='freq')

# Additive Decomposition
result_add = seasonal_decompose(df, model='additive',period=365*24, extrapolate_trend='freq')


# Extract the Components ----
# Actual Values = Product of (Seasonal * Trend * Resid)
df_reconstructed_mul = pd.concat([result_mul.seasonal, result_mul.trend, result_mul.resid, result_mul.observed], axis=1)
df_reconstructed_mul.columns = ['seas', 'trend', 'resid', 'actual_values']
df_reconstructed_mul.to_csv('timeserie_decom_mul_train.csv')
#df_reconstructed_mul.head()

# Actual Values = Sum of (Seasonal * Trend * Resid)
df_reconstructed_add = pd.concat([result_add.seasonal, result_add.trend, result_add.resid, result_add.observed], axis=1)
df_reconstructed_add.columns = ['seas', 'trend', 'resid', 'actual_values']
df_reconstructed_add.to_csv('timeserie_decom_add_train.csv')
#df_reconstructed_add.head()

# Plot
result_mul.plot().suptitle('Multiplicative Decompose', fontsize=22)
result_add.plot().suptitle('Additive Decompose', fontsize=22)
plt.show()