import requests
import yfinance as yf
import pandas as pd


def screener(ticker, api_key):
    #use response.get() to get the data

    #alphavantage
    # url = f"https://www.alphavantage.co/query?function=INCOME_STATEMENT&symbol={ticker}&apikey={api_key}"
    # response = requests.get(url)

    #yfinance
    data = yf.Ticker(ticker)


    #figure out what form the data comes in/needs to be in
    row = {
        'ticker' : [ticker],
        'sector' : [data.info['sector']],
        'stock_price' : [data.history(period = '1d')["Close"].iloc[-1]],
        'pe_ratio' : [data.info['trailingPE']]
    }

    #run data through the screen  
    df = pd.DataFrame(row)  

    #return the screened data
    return df