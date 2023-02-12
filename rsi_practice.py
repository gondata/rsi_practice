# First of all we have to import the libraries that we are going to use

from pandas_datareader import data as pdr
import yfinance as yf
import matplotlib.pyplot as plt

yf.pdr_override()

# Then we have to download the data

ticker = ['GOOG']
startdate = '2018-01-01'
enddate = '2023-02-02'

data = pdr.get_data_yahoo(ticker, start=startdate, end=enddate)['Adj Close']

returns = data.pct_change()

# Variables

up = returns.clip(lower=0) # numbers>0
down = returns.clip(upper=0) # numbers<0

ema_up = up.ewm(com=14, adjust=False).mean()
ema_down = down.ewm(com=14, adjust=False).mean()

rs = -(ema_up / ema_down)

# Formula

datarsi = 100 - (100/(1+rs))

# Graphs

fig, (ax1, ax2) = plt.subplots(2)
ax1.get_xaxis().set_visible(False)
fig.suptitle(ticker)

# 1

data.plot(ax=ax1)
ax1.set_ylabel('Price')

# 2

datarsi.plot(ax=ax2)
ax2.set_ylim(0, 100)
ax2.set_ylabel('RSI')
ax2.axhline(70, color='r', linestyle='--')
ax2.axhline(30, color='r', linestyle='--')

plt.show()
