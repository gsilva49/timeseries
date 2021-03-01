import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('../timeserie_train.csv',
                index_col='data', parse_dates=['data'])

df['d-semana'] = [d.strftime('%A') for d in df.index]

d = sns.boxplot(x='d-semana', y='energia', data=df)
d.set_xticklabels(d.get_xticklabels(),rotation=90)

plt.show()
