from datetime import datetime
import yfinance as yf
import pandas as pd
from tqdm import tqdm
import pickle
from bin.fetch_data.get_data import create_spy_weights

from config import MONTH_DELAY



MONTH_DELAY

create_spy_weights("spy_logs/"+datetime.today().strftime('%Y-%m-%d')+'_spy.csv')
