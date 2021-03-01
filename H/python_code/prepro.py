import pandas as pd

def changing_to_float(string): 
    try: 
        return float(string)
    except: 
        return float(string.replace('.','',1))


def format_data(series):
    series = series.apply(lambda x: changing_to_float(x))
    series = series.apply(lambda x: (x/10) if (x>20000) else x) ##retira alguns erros
    series = series.astype('float')
    return series


#load de data
df = pd.read_csv('../2000_2021_Brazilian_North_Region_hourly_MWmed_hydroelectric_power_series.csv', 
    parse_dates=['Data Escala de Tempo 1 GE Simp 4'], 
    index_col='Data Escala de Tempo 1 GE Simp 4')

#removing some columns 
df = df.drop(columns=['Data Dica',
                 'dsc_estado', 
                 'id_subsistema', 
                 'nom_tipousinasite', 
                 'nom_usina2', 
                 'Período Exibido GE'])

df.rename(columns = {'Selecione Tipo de GE Simp 4':'energia'}, 
    inplace = True)
df.index.names = ['data']
df = format_data(df.energia)

#saving the dataframe as csv
df.to_csv('../timeserie_prepro.csv')