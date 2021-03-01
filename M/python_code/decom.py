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
result_mul = seasonal_decompose(df, model='multiplicative', period=365)

# Additive Decomposition
result_add = seasonal_decompose(df, model='additive',period=365)

# Plot
result_mul.plot().suptitle('Multiplicative Decompose', fontsize=22)
result_add.plot().suptitle('Additive Decompose', fontsize=22)
plt.show()
