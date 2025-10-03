from apikey import api_key
import screen
import pandas as pd

def main():
    ticks = pd.read_csv('data/SP500.csv')['Symbol'].tolist()
    new_df = pd.DataFrame()

    for item in ticks:
        new_df = pd.concat([new_df, screen.screener('AAPL', api_key)], ignore_index=True)

    print(new_df)
        
if __name__ == "__main__":
    main()
