from datetime import datetime
import yfinance as yf
import pandas as pd
from pandas.io.formats.format import return_docstring
from tqdm import tqdm
import pickle

import config
from bin.fetch_data.get_data import create_spy_weights

from alpaca.trading.client import TradingClient


from config import MONTH_DELAY
if __name__ == "__main__":
    api_key = config.ALPACA_API_KEY
    secret_key = config.ALPACA_API_SECRET


    if api_key is None or secret_key is None :
        print("Alpaca API key or secret key are not set")
        exit(1)


    client = TradingClient(api_key, secret_key, paper=True)
    account = client.get_account()
    print(account.cash)
