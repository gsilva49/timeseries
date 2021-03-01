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
df = pd.read_csv('../Northeast_daily_MW_instantaneous_maximum_demand_series.csv', 
                 parse_dates=['Data Escala de Tempo 1 DM Simp 4'],
                 index_col='Data Escala de Tempo 1 DM Simp 4')

#removing some columns 
df = df.drop(columns=['Data do Incio da Semana Din Instante DM Simp 4',
                 'Data Escala de Tempo 1 DM Simp 4.1', 
                 'Din Instante', 
                 'Período Exibido DM Simp 4', 
                 'Subsistema', 
                     'Texto Data Incio da Semana Din Instante DM'])

df.rename(columns = {'Selecione Tipo de DM Simp 4':'energia'}, inplace = True)
df.index.names = ['data']
df = format_data(df.energia)

#saving the dataframe as csv
df.to_csv('../timeserie_prepro.csv')