import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('../timeserie_train.csv',
                index_col='data', parse_dates=['data'],
                  squeeze=True)

df.plot()
plt.title("Série Temporal - Power Series")
plt.show()