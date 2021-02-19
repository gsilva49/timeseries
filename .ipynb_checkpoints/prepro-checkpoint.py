import pandas as pd

df = pd.read_csv('2000_2021_Brazilian_North_Region_hourly_MWmed_hydroelectric_power_series.csv', parse_dates=['Data Escala de Tempo 1 GE Simp 4'], index_col='Data Dica')

df = df.drop(columns=['Data Escala de Tempo 1 GE Simp 4',
                 'dsc_estado', 
                 'id_subsistema', 
                 'nom_tipousinasite', 
                 'nom_usina2', 
                 'Período Exibido GE'])

df.to_csv('2000_2021_Brazilian_North_Region_hourly_MWmed_hydroelectric_power_series_prepro.csv',
         header=0)