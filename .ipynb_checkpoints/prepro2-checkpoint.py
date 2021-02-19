from pandas import read_csv
from datetime import datetime

#Split time series into a training/test
def split_to_train_test(series, test_percent=0.50):
    split_point = int(test_percent * len(series))
    return series[:-split_point], series[-split_point:]


#Select a percentage from the time series
def data_proportion(series, percent=1.0):
    series = series[-int(percent * len(series)):]
    return series

# Specifying data-time order
def parser(x):
    return datetime.strptime(x, '%d/%m/%Y %H:%M')

#load data
series = read_csv('2000_2021_Brazilian_North_Region_hourly_MWmed_hydroelectric_power_series_prepro.csv',
                 header=None, index_col=0, parse_dates=True,
                 date_parser=parser, squeeze=True)
print(f'Total data: {len(series)}')

series_per = data_proportion(series, percent=1)

print(f'Percentage data: {len(series_per)}')

#split data
train, test = split_to_train_test(series_per, test_percent=0.40)
print('Training %d, Teste %d' % (len(train), len(test)))

train.to_csv('2000_2021_Brazilian_North_Region_hourly_MWmed_hydroelectric_power_series_train.csv',
            header=None)

test.to_csv('2000_2021_Brazilian_North_Region_hourly_MWmed_hydroelectric_power_series_test.csv',
            header=None)