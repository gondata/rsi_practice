# RSI-Plotter

This script imports financial data using pandas_datareader and yfinance libraries, calculates the relative strength index (RSI) and plots the stock price and RSI graph using matplotlib.

## Prerequisites

- pandas_datareader
- yfinance
- matplotlib

## Usage

1. Set the ticker symbol you want to download data for, start date and end date in the following variables:
```
ticker = ['TICKER']
startdate = 'YYYY-MM-DD'
enddate = 'YYYY-MM-DD'
```

2. Run the script, the output should be a graph with the stock price and RSI.

## Conclusion

The relative strength index (RSI) is a commonly used technical indicator to evaluate the strength of a stock's price action. The graph produced by this script allows you to visually track the RSI over time to help make informed trading decisions.
