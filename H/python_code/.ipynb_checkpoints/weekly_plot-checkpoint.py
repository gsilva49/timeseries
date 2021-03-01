import pandas as pd
import matplotlib.pyplot as plt

def data_proportion(series, percent=1.0):
    series = series[-int(percent * len(series)):]
    return series

def weekly_plot(serie):
    groups = serie.groupby(pd.Grouper(freq='W'))
    values = list()
    weeks = list()
    for name, group in groups:
        df = pd.DataFrame(group.values)
        values.append(df)
        weeks.append(name.week)
    df = pd.concat(values, ignore_index=True, axis=1)
    df.plot(subplots=False, legend=True)
    plt.title("Weekly Plot")
    plt.show()

df = pd.read_csv('../timeserie_train.csv',
                index_col='data', parse_dates=['data'],
                  squeeze=True)

weekly_data = data_proportion(df, percent=0.01)
print(f'Total of Date:{len(weekly_data)}')
weekly_plot(weekly_data)

