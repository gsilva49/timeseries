from dateutil.parser import parse 
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
#plt.rcParams.update({'figure.figsize': (10, 7), 'figure.dpi': 120})


def daily_lineplot(series, days):
    series['hora'] = [h.strftime('%H') for h in series.index]
    series['dia'] = [h.strftime('%x') for h in series.index]
    dias = series['dia'].unique()
    count = 0
    
    for i, d in enumerate(dias):
        plt.plot('hora','energia', data=df.loc[df.dia==d,:], label=d)
        plt.legend(bbox_to_anchor=(1,1), loc="upper left")
        count = count + 1
        if count == days:
            break
            
    plt.show()

df = pd.read_csv('2000_2021_Brazilian_North_Region_hourly_MWmed_hydroelectric_power_series_train.csv', 
	parse_dates=['data'], 
	index_col='data')

daily_lineplot(df, 20)
