import pandas as pd
import numpy as np
#import matplotlib.pylab as plt 
#%matplotlib inline
#from matplotlib.pylab import rcParams
#rcParams['figure.figsize'] = 15, 6

## Primeiro tenho que limpar as colunas
## Segundo - Pegar uma parte dos dados para:% dos dados e  % de teste
## 40 para teste, 60 para treinamento 

data = pd.read_csv('AirPassengers.csv') 
print(data.head())
print('\n Data Types:')
print(data.dtypes)

dateparse = lambda dates: pd.datetime.strptime(dates, '%Y-%m') 
data = pd.read_csv('AirPassengers.csv', parse_dates=['Month'], 
	index_col='Month',date_parser=dateparse) 
print(data.head())

def plot_df(df, x, y, title="", xlabel='Date', ylabel='Value', dpi=100):
    plt.figure(figsize=(16,5), dpi=dpi)
    plt.plot(x, y, color='tab:red')
    plt.gca().set(title=title, xlabel=xlabel, ylabel=ylabel)
    plt.show()

def percentage_data(df, percent, upside_down=False):
	columns = df.shape[0]
	length = round(columns*percent)
	if upside_down:
		return df.iloc[-length:]
	else:
		return df.iloc[:length]

def split_test_train(df, train_size):
	train = percentage_data(df, train_size)
	test_size = 1-train_size
	test = percentage_data(df, test_size, True)
	return train, test


fig, ax = plt.subplots(1, 1, figsize=(16,5), dpi= 120)
plt.fill_between(x, y1=y1, y2=-y1, alpha=0.5, linewidth=2, color='seagreen')
plt.ylim(-800, 800)
plt.title('Air Passengers (Two Side View)', fontsize=16)
plt.hlines(y=0, xmin=np.min(df.date), xmax=np.max(df.date), linewidth=.5)
plt.show()