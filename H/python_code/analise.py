import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('../timeserie_prepro.csv',
                index_col='data', parse_dates=['data'],
                  squeeze=True)

print(" Média: %f " %(df.mean()))
print(" Variância: %f " %(df.var()))

df.plot()
plt.title("Série Temporal - Power Series")
plt.show()