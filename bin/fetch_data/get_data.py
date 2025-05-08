from datetime import datetime
from io import StringIO

import requests
import yfinance as yf
import pandas as pd
from tqdm import tqdm
import pickle




def create_spy_weights(outdir:str = None ) -> pd.DataFrame:
    headers = {
        'User-Agent': 'Mozilla/5.0'
    }
    res = requests.get("https://www.slickcharts.com/sp500", headers=headers)
    df = pd.read_html(StringIO(res.text))[0]
    df = df[['Symbol', 'Weight']].copy()
    print(df)


    if outdir:
        df.to_csv(outdir, index=False)

    return df
