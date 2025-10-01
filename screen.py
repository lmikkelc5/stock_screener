import requests



def screener_stock(ticker, api_key):
    #use response.get() to get the data
    url = f"https://www.alphavantage.co/query?function=INCOME_STATEMENT&symbol={ticker}&apikey={api_key}"
    response = requests.get(url)

    #figure out what form the data comes in/needs to be in

    #run data through the screen    

    #return the screened data
    return url