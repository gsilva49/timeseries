import numpy as np
import pandas as pd

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

df = pd.read_csv('2000_2021_Brazilian_North_Region_hourly_MWmed_hydroelectric_power_series.csv')
train, test = split_test_train(df, 0.6)

train.to_csv('train.csv') 
test.to_csv('test.csv')