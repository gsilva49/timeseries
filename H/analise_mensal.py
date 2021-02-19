from dateutil.parser import parse 
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
#plt.rcParams.update({'figure.figsize': (10, 7), 'figure.dpi': 120})

def monthly_lineplot(series, months):
    series['dia'] = [d.strftime('%d') for d in series.index]
    series['dia hora'] = [d.strftime('%d-%H') for d in series.index]
    series['mes_ano'] = [d.strftime('%b-%Y') for d in series.index]

    meses = series['mes_ano'].unique()
    diah = series['dia hora'].unique()
    dia = series['dia'].unique()

    count = 0
    for i, m in enumerate(meses):

        plt.plot('dia hora','energia', data=series.loc[series.mes_ano==m,:], label=m)
        plt.legend(bbox_to_anchor=(1,1), loc="upper left")
        count = count + 1
        if count == months:
            break
    
    plt.xticks(diah[::120], dia[::5], rotation='vertical')
    
    plt.show()

df = pd.read_csv('2000_2021_Brazilian_North_Region_hourly_MWmed_hydroelectric_power_series_train.csv', 
	parse_dates=['data'], 
	index_col='data')

monthly_lineplot(df, 3)