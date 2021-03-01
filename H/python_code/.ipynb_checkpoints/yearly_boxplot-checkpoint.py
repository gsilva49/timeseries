import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('../timeserie_train.csv',
                index_col='data', parse_dates=['data'])

df['ano'] = [d.year for d in df.index]

sns.boxplot(x='ano', y='energia', data=df)

plt.show()