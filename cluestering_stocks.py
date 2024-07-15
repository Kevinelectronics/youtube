import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import numpy as np

# Fetch historical data using yfinance
tickers = ['AAPL', 'MSFT', 'GOOGL', 'AMZN']  # Sample of S&P 500 stocks
data = yf.download(tickers, start="2020-01-01", end="2022-01-01", group_by='ticker')

# Combine data and add Ticker column
data_list = []
for ticker in tickers:
    df = data[ticker].copy()
    df['Ticker'] = ticker
    data_list.append(df)

data = pd.concat(data_list)

# Define functions for computing indicators
def compute_RSI(data, window=14):
    delta = data.diff(1)
    gain = (delta.where(delta > 0, 0)).rolling(window=window).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=window).mean()
    RS = gain / loss
    return 100 - (100 / (1 + RS))

def compute_BB(data, window=20):
    sma = data.rolling(window=window).mean()
    std = data.rolling(window=window).std()
    upper_band = sma + (std * 2)
    lower_band = sma - (std * 2)
    return upper_band, sma, lower_band

def calculate_indicators(df):
    df['SMA_10'] = df['Close'].rolling(window=10).mean()
    df['RSI'] = compute_RSI(df['Close'])
    df['BB_upper'], df['BB_middle'], df['BB_lower'] = compute_BB(df['Close'])
    return df

# Apply the function to our data
data = data.groupby('Ticker').apply(calculate_indicators).dropna()

# Example 1: Clustering with K-Means
indicators = data[['SMA_10', 'RSI', 'BB_upper', 'BB_middle', 'BB_lower']].dropna()
kmeans = KMeans(n_clusters=4)
data['Cluster'] = kmeans.fit_predict(indicators)

# Create a mapping from cluster to company
cluster_map = {i: [] for i in range(4)}
for ticker in tickers:
    ticker_data = data[data['Ticker'] == ticker]
    cluster_num = ticker_data['Cluster'].mode()[0]
    cluster_map[cluster_num].append(ticker)

# Ensure no empty clusters by verifying each cluster has at least one ticker
for cluster in cluster_map:
    if not cluster_map[cluster]:
        print(f"Warning: Cluster {cluster} has no tickers assigned.")

# Visualization of clusters with legend
plt.figure(figsize=(10, 6))
scatter = plt.scatter(data['SMA_10'], data['RSI'], c=data['Cluster'], cmap='viridis', alpha=0.5)
plt.xlabel('SMA_10')
plt.ylabel('RSI')
plt.title('Stock Clusters based on SMA and RSI')

# Add legend with company names
handles, labels = scatter.legend_elements()
legend_labels = []
for i in range(4):
    if cluster_map[i]:
        legend_labels.append(f"Cluster {i}: {', '.join(cluster_map[i])}")
    else:
        legend_labels.append(f"Cluster {i}: No tickers assigned")

plt.legend(handles, legend_labels, title="Clusters")
plt.show()