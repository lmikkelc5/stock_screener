import requests
import yfinance as yf
import pandas as pd

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

def screener(ticker, api_key):
    #alphavantage
    # url = f"https://www.alphavantage.co/query?function=INCOME_STATEMENT&symbol={ticker}&apikey={api_key}"
    # response = requests.get(url)

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