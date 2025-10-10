import yfinance as yf
import pandas as pd
import numpy as np
from datetime import date, timedelta
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

#go through a list of tickers and remove those that arent working
def check_list(ticker_lst, verbose = True):
    valid = []
    invalid = []

    for sym in ticker_lst:
        try:
            t = yf.Ticker(sym)
            hist = t.history(period = '1d')

            if hist.empty:
                invalid.append(sym)
                if verbose:
                    print(f"{sym}: Possibly delisted")
            else:
                valid.append(sym)
                if verbose:
                    print(f"{sym}: Valid")
        except Exception as e:
            invalid.append(sym)
            if verbose:
                print(f"{sym}: Error fetching ({e})")

    if verbose:
        print("\nSummary")
        print(f"Valid tickers: {len(valid)}")
        print(f"Invalid Tickers: {len(valid)}")

    return valid, invalid

#main screener to check for and return df(1 row at a time) of wanted data
def screener(ticker, api_key):
    #yfinance
    data = yf.Ticker(ticker)
    hist = data.history(period = '1d')

    #get data
    try:
        stock_price = data.history(period = '1d')["Close"].iloc[-1]
    except Exception:
        stock_price = None
    sector = data.info.get('sector', None)
    trailing_PE = data.info.get('trailingPE', None)

    #make the df
    row = {
        'ticker' : [ticker],
        'sector' : [sector],
        'stock_price' : [stock_price],
        'pe_ratio' : [trailing_PE]
    }

    #create df  
    df = pd.DataFrame(row) 

    #return the data
    return df

#return the sharpe ratio for a given ticker
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