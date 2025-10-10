import pandas as pd
import yfinance as yf
import numpy as np
from datetime import date, timedelta
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

def sharpe(ticker):
    #set values
    end_date = date.today()
    start_date = end_date - timedelta(days = 5 * 365)
    data = yf.download(ticker.upper(), start = start_date, end = end_date, interval = '1d')
    returns = data['Close'].pct_change().dropna()

    # calculate mean return and the standard deviation/volatility
    mean_return = returns.mean() *252
    volatility = returns.std() * np.sqrt(252)

    #use a base risk free rate
    risk_free = 0.04

    #compute the sharpe ratio
    sharpe = (mean_return-risk_free)/volatility

    return float(sharpe)