from datetime import datetime

from bin.fetch_data.get_data import create_spy_weights


def initialize_trading():
    weights = create_spy_weights("spy_logs/"+datetime.today().strftime('%Y-%m-%d')+'_spy.csv')

