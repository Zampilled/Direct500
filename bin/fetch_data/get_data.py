from datetime import datetime
import yfinance as yf
import pandas as pd
from tqdm import tqdm
import pickle




def create_spy_weights(outdir:str = None ) -> pd.DataFrame:

    #Scrape Wiki for S&P Symbols
    df = pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')[0]
    tickers = df['Symbol'].tolist()

    my_tickers = []

    # Pull data for each ticker
    for x in tqdm(tickers):
        spy = yf.Ticker(x).info
        if "marketCap" in spy:
            my_tickers.append([x, spy['marketCap']])

    # Clean Up Data
    df = pd.DataFrame(my_tickers, columns=['Symbol', 'Market Cap'])

    # Get Market Cap of S&P 500
    cap_sum = df['Market Cap'].sum()

    # Calculate Weight base off ratio
    df["Weight"] = df['Market Cap'] / cap_sum

    # Drop Useless Column
    df.drop(columns=['Market Cap'], inplace=True)

    # Sort Weight for Readability
    df.sort_values(by='Weight', ascending=False, inplace=True)

    # Print and Save
    print("New Weights")
    print(df.head())


    if outdir:
        df.to_csv(outdir, index=False)

    return df
