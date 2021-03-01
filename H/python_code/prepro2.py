from pandas import read_csv
from datetime import datetime

#Split time series into a training/test
def split_to_train_test(series, test_percent=0.50):
    split_point = int(test_percent * len(series))
    return series[:-split_point], series[-split_point:]

#Select a percentage from the time series
def data_proportion(series, percent=1.0, from_end=True):
    if from_end:
        series = series[-int(percent * len(series)):]
    else:
        series = series[:int(percent * len(series))]
    return series

#load data
series = read_csv('../timeserie_prepro.csv', 
                  parse_dates=['data'], 
                  index_col='data',
                  squeeze=True)
print(f'Total data: {len(series)}')

series_per = data_proportion(series, percent=1, from_end=True)

print(f'Percentage data: {len(series_per)}')

#split data
train, test = split_to_train_test(series_per, test_percent=0.25)
print('Training %d, Teste %d' % (len(train), len(test)))

train.to_csv('../timeserie_train.csv')

test.to_csv('../timeserie_test.csv')