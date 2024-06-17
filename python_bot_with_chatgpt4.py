import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import alpaca_trade_api as tradeapi
import mplfinance as mpf

def get_stock_data(tickers, period='1mo'):
    data = {}
    for ticker in tickers:
        stock_data = yf.download(ticker, period=period)
        data[ticker] = stock_data
    return pd.concat(data, axis=1)

tickers = ['AAPL', 'MSFT', 'GOOG']
stock_data = get_stock_data(tickers)
print(stock_data)

def calculate_pivot_points(data):
    pivot_points = {}
    for ticker in data.columns.levels[0]:
        df = data[ticker]
        pivot = (df['High'] + df['Low'] + df['Close']) / 3
        resistance1 = (2 * pivot) - df['Low']
        support1 = (2 * pivot) - df['High']
        resistance2 = pivot + (df['High'] - df['Low'])
        support2 = pivot - (df['High'] - df['Low'])
        pivot_points[ticker] = pd.DataFrame({
            'Pivot': pivot,
            'Resistance1': resistance1,
            'Support1': support1,
            'Resistance2': resistance2,
            'Support2': support2
        })
    return pivot_points

pivot_points = calculate_pivot_points(stock_data)
for ticker, points in pivot_points.items():
    print(f"\n{ticker}\n", points)

def plot_stock_data(data, pivot_points, ticker):
    mpf.plot(data[ticker], type='candle', style='charles', 
             title=ticker, 
             hlines=dict(hlines=[pivot_points[ticker]['Resistance1'].iloc[-1], 
                                 pivot_points[ticker]['Support1'].iloc[-1]], 
                         colors=['g', 'r'], linestyle='-'))

plot_stock_data(stock_data, pivot_points, 'AAPL')
import alpaca_trade_api as tradeapi

API_KEY = 'your_api_key'
API_SECRET = 'your_api_secret'
BASE_URL = 'https://paper-api.alpaca.markets'

api = tradeapi.REST(API_KEY, API_SECRET, BASE_URL, api_version='v2')

def place_order(ticker, qty, order_type):
    api.submit_order(
        symbol=ticker,
        qty=qty,
        side=order_type,
        type='market',
        time_in_force='gtc'
    )

def trading_bot(data, pivot_points, ticker):
    for index, row in data[ticker].iterrows():
        if row['Close'] < pivot_points[ticker]['Support1'].iloc[index]:
            place_order(ticker, 10, 'buy')
        elif row['Close'] > pivot_points[ticker]['Resistance1'].iloc[index]:
            place_order(ticker, 10, 'sell')

trading_bot(stock_data, pivot_points, 'AAPL')