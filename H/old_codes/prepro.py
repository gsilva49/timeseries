import pandas as pd

#evitar erros tipo 1.215.215 -> 1215.215
def rreplace(s, old, new, occurrence):
    li = s.rsplit(old, occurrence)
    return new.join(li)

def format_data(series):
    series = series.apply(lambda x: rreplace(x, '.',',',1))
    series = series.apply(lambda x: x.replace('.',''))
    series = series.apply(lambda x: x.replace(',','.'))
    series = series.astype('float')
    return series

#load de data
df = pd.read_csv('2000_2021_Brazilian_North_Region_hourly_MWmed_hydroelectric_power_series.csv', 
	parse_dates=['Data Escala de Tempo 1 GE Simp 4'], 
	index_col='Data Escala de Tempo 1 GE Simp 4')

#removing some columns 
df = df.drop(columns=['Data Dica',
                 'dsc_estado', 
                 'id_subsistema', 
                 'nom_tipousinasite', 
                 'nom_usina2', 
                 'Período Exibido GE'])


df.rename(columns = {'Selecione Tipo de GE Simp 4':'energia'}, inplace = True)
df.index.names = ['data']
df = format_data(df.energia)

#saving the dataframe as csv
df.to_csv('2000_2021_Brazilian_North_Region_hourly_MWmed_hydroelectric_power_series_prepro.csv')