import pandas as pd
import matplotlib.pyplot as plt

def data_proportion(series, percent=1.0):
    series = series[-int(percent * len(series)):]
    return series

def month_plot(serie):
    groups = serie[8:].groupby(pd.Grouper(freq='M'))
    values = list()
    months = list()
    for name, group in groups:
        df = pd.DataFrame(group.values)
        values.append(df)
        months.append(name.month)
    df = pd.concat(values, ignore_index=True, axis=1)
    df.columns = months
    df.plot(subplots=False, legend=True)
    plt.title("Monthly Plot")
    plt.show()
    

df = pd.read_csv('../timeserie_train.csv',
                index_col='data', parse_dates=['data'],
                  squeeze=True)

monthly_data = data_proportion(df, percent=0.02)
print(f'Total of Date:{len(monthly_data)}')
month_plot(monthly_data)

