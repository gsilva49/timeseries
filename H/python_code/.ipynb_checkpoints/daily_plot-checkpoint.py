import pandas as pd
import matplotlib.pyplot as plt

def data_proportion(series, percent=1.0):
    series = series[-int(percent * len(series)):]
    return series

def daily_plot(serie):
    groups = serie.groupby(pd.Grouper(freq='D'))
    values = list()
    days = list()
    for name, group in groups:
        df = pd.DataFrame(group.values)
        values.append(df)
        days.append(name.day)
    df = pd.concat(values, ignore_index=True, axis=1)
    df.columns = days
    df.plot(subplots=False, legend=True)
    plt.title("Daily Plot")
    plt.show()

df = pd.read_csv('../timeserie_train.csv',
                index_col='data', parse_dates=['data'],
                  squeeze=True)

daily_data = data_proportion(df, percent=0.003)
print(f'Total of Date:{len(daily_data)}')
daily_plot(daily_data)

