# Finance Project
# pip install pandas_datareader
import pandas_datareader.data as web
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import datetime

start = datetime.datetime(2006, 1, 1)
end = datetime.datetime(2016, 1, 1)
BAC = web.DataReader('BAC', 'yahoo', start, end)
C = web.DataReader('C', 'yahoo', start, end)
GS = web.DataReader('GS', 'yahoo', start, end)
JPM = web.DataReader('JPM', 'yahoo', start, end)
MS = web.DataReader('MS', 'yahoo', start, end)
WFC = web.DataReader('WFC', 'yahoo', start, end)
print(BAC.head())

tickers = ['BAC', 'C', 'GS', 'JPM', 'MS', 'WFC']
banks_stocks = pd.concat([BAC, C, GS, JPM, MS, WFC], axis=1, keys=tickers)
print(banks_stocks.head())

#banks_stocks.columns.names = ['Bank Ticker', 'Stock Info']
# print(banks_stocks.head())

# DF TO CSV
#banks_stocks.to_csv('banks_stocksExport.csv', sep=',')
# print(banks_stocks['BAC']['Close'].max())
# what is the max close price for each bank's stock throughout time period
for tick in tickers:
    print(tick, banks_stocks[tick]['Close'].max())

# altername
max = banks_stocks.xs(key='Close', axis=1, level='Stock Info').max()
print(max)

# Create a new empty DataFrame called returns.
returns = pd.DataFrame()

# pct_change() method
for tick in tickers:
    returns[tick + '_Return'] = banks_stocks[tick]['Close'].pct_change()

print(returns.head())

# create a pairplot using seaborn of the returns dataframe. What stock stands out to you?
# Can you figure out why?
# sns.pairplot(returns[1:])
plt.show(sns.pairplot(returns[1:]))

# what dates each bank stock had the best and worst single day returns
returns['BAC Return'].argmin()

# for all
returns.idxmin()
returns.idxmax()

# look at standard deviation, which stock would you classify as the riskiest over the
# entire time period
returns.std()

# same risks
returns.ix['2015-01-01':'2015-12-31'].std()

# create a distplot
plt.show(sns.distplot(returns.ix['2015-01-01':'2015-12-31']['MS Return'], color='green', bins=50))
plt.show(sns.distplot(returns.ix['2008-01-01':'2008-12-31']['C Return'], color='green', bins=50))
