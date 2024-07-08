import pandas as pd
import numpy as np
import yfinance as yf

# Function to fetch historical price data from Yahoo Finance
def get_historical_data(symbol, start_date, end_date):
    data = yf.download(symbol, start=start_date, end=end_date)
    return data

# List of stock symbols
symbols = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'FB','NVDA','TSLA']
start_date = '2024-01-01'
end_date = '2024-08-07'

# Fetch historical price data for each stock
price_data = {}
for symbol in symbols:
    price_data[symbol] = get_historical_data(symbol, start_date, end_date)

# Function to calculate momentum
def calculate_momentum(data):
    returns = data['Close'].pct_change()
    total_return = (1 + returns).prod() - 1
    return total_return

# Calculate momentum scores for each stock
momentum_scores = {}
for symbol in symbols:
    momentum_scores[symbol] = calculate_momentum(price_data[symbol])

momentum_scores = pd.Series(momentum_scores)

# Select the top 3 stocks with the highest momentum
top_momentum_stocks = momentum_scores.nlargest(3)
print("Top Momentum Stocks:")
print(top_momentum_stocks)

# Build an equally weighted portfolio
portfolio = pd.DataFrame(columns=['Symbol', 'Momentum Score', 'Weight'])
total_stocks = len(top_momentum_stocks)
weight = 1 / total_stocks

for symbol, momentum_score in top_momentum_stocks.items():
    portfolio = portfolio._append({'Symbol': symbol, 'Momentum Score': momentum_score, 'Weight': weight}, ignore_index=True)

print("\nPortfolio:")
print(portfolio)
