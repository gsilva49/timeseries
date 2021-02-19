from dateutil.parser import parse 
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
#plt.rcParams.update({'figure.figsize': (10, 7), 'figure.dpi': 120})

df = pd.read_csv('2000_2021_Brazilian_North_Region_hourly_MWmed_hydroelectric_power_series_train.csv', 
	parse_dates=['data'], 
	index_col='data')

df['d-semana'] = [d.strftime('%A') for d in df.index]
df['mes'] = [d.strftime('%b') for d in df.index]
df['ano'] = [d.year for d in df.index]

#analise dod dias
b = sns.boxplot(x='d-semana', y='energia', data=df)
b.set_xticklabels(b.get_xticklabels(),rotation=90)

#analise do meses
sns.boxplot(x='mes', y='energia', data=df)

#analise do anos
sns.boxplot(x='ano', y='energia', data=df)