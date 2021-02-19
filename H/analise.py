import pandas as pd
import matplotlib.pyplot as plt

series = pd.read_csv('2000_2021_Brazilian_North_Region_hourly_MWmed_hydroelectric_power_series_train.csv',
                    index_col='data', parse_dates=['data'],
                  squeeze=True)

series.plot()
plt.show()