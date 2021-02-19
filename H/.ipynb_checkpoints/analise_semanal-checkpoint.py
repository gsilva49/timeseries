from dateutil.parser import parse 
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def weekly_lineplot(series, weeks):
    series['hora'] = [d.strftime('%H') for d in series.index]
    series['d_semana'] = [d.strftime('%w') for d in series.index]
    series['semana'] = [d.strftime('%U') for d in series.index]
    series['ano'] = [d.strftime('%Y') for d in series.index]
    series['semana_ano'] = series['ano'] + ' - semana ' + series['semana']

    series['d_semana hora'] = [d.strftime('%w-%H') for d in series.index] 
    series['d_semana hora ano'] = [d.strftime('%Y-%w-%H') for d in series.index] 
    series['semana_ext'] = [d.strftime('%A') for d in series.index]

    series['semana_ano'] = series['ano'] + ' - semana ' + series['semana']
    
    semanas =series['semana_ano'].unique()
    dsemana = series['d_semana hora'].unique()
    dsemana_ext = series['semana_ext'].unique()
    
    count = 0
    for i, s in enumerate(semanas):

        #checar se é o começo da semana
        if int(series.loc[series.semana_ano==s,:].iloc[0].d_semana) != 0:
            continue

        plt.plot('d_semana hora','energia', data=series.loc[series.semana_ano==s,:], label=s)
        plt.legend(bbox_to_anchor=(1,1), loc="upper left")
        count = count + 1
        if count == weeks:
            break
    plt.xticks(dsemana[::24], dsemana_ext[::1], rotation='vertical')
    
    plt.show()

df = pd.read_csv('2000_2021_Brazilian_North_Region_hourly_MWmed_hydroelectric_power_series_train.csv', 
	parse_dates=['data'], 
	index_col='data')

weekly_lineplot(df, 3)