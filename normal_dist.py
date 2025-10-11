import matplotlib.pyplot as plt
import pandas as pd
import yfinance as yf
from datetime import date, timedelta
import numpy as np

ticker = 'AAPL'
end_date = date.today()
start_date = end_date - timedelta(days = 365)

data = yf.download(ticker, start = start_date, end = end_date)
returns = data['Close'].pct_change().dropna()

mean_return = np.mean(returns)
std_return = np.std(returns)

plt.hist(returns, bins = 50)
plt.title(f'Distribution of % returns for {ticker.upper()}')
plt.xlabel('% Change')
plt.ylabel('Number of occurences')
plt.show()