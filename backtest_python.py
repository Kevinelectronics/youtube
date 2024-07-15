from backtesting import Backtest, Strategy
from backtesting.lib import crossover
from backtesting.test import SMA
import yfinance as yf
import pandas as pd
import datetime as dt
import openpyxl

class MySmaStrategy(Strategy):
    def init(self):
        price = self.data.Close
        self.sma1 = self.I(SMA, price, 10)
        self.sma2 = self.I(SMA, price, 20)

    def next(self):
        if crossover(self.sma1, self.sma2):
            self.buy()
        elif crossover(self.sma2, self.sma1):
            self.sell()

# Fetch historical data using yfinance
start = dt.datetime(2020, 1, 1)
end = dt.datetime(2022, 1, 1)
data = yf.download('TSLA', start=start, end=end)

# Prepare data for backtesting
data = data[['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']]
data.columns = ['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']

# Run the backtest
bt = Backtest(data, MySmaStrategy, commission=0.002, exclusive_orders=True)
stats = bt.run()

# Extract main metrics
metrics = {
    "Start": [stats['Start']],
    "End": [stats['End']],
    "Duration": [stats['Duration']],
    "Equity Final [$]": [stats['Equity Final [$]']],
    "Equity Peak [$]": [stats['Equity Peak [$]']],
    "Return [%]": [stats['Return [%]']],
    "Buy & Hold Return [%]": [stats['Buy & Hold Return [%]']],
    "Max. Drawdown [%]": [stats['Max. Drawdown [%]']],
    "Avg. Drawdown [%]": [stats['Avg. Drawdown [%]']],
    "Max. Drawdown Duration": [stats['Max. Drawdown Duration']],
    "Trades": [stats['# Trades']],
    "Win Rate [%]": [stats['Win Rate [%]']],
    "Best Trade [%]": [stats['Best Trade [%]']],
    "Worst Trade [%]": [stats['Worst Trade [%]']],
    "Avg. Trade [%]": [stats['Avg. Trade [%]']],
    "Max. Trade Duration": [stats['Max. Trade Duration']],
    "Avg. Trade Duration": [stats['Avg. Trade Duration']],
    "Profit Factor": [stats['Profit Factor']],
    "Expectancy [%]": [stats['Expectancy [%]']],
    "Sharpe Ratio": [stats['Sharpe Ratio']],
    "Sortino Ratio": [stats['Sortino Ratio']],
}

# Convert to DataFrame
metrics_df = pd.DataFrame(metrics)

# Save to Excel
metrics_df.to_excel("strategy_metrics.xlsx", index=False)

print(stats)
