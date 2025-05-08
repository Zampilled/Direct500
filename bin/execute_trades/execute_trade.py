import os
from datetime import datetime

import pandas as pd


def execute_trade(order_name):
    sell_df = None
    buy_df =  None
    if os.path.exists("orders/buy/"+order_name+".csv"):
        buy_df = pd.read_csv("orders/buy/"+order_name+".csv")

    if os.path.exists("orders/buy/"+order_name+".csv"):
        sell_df = pd.read_csv("orders/sell/"+order_name+".csv")
    with pd.option_context('display.max_rows', None, 'display.max_columns', None):
        answer = input(
            "Sell orders: \n\n"+
            sell_df+
            "\n Buy orders: \n\n" +
            buy_df+
            "\n Execute trade? (y/n): "

        )

    if sell_df is not None:
        print("Selling Stage Starting")

        print("Selling Stage Completed Successfully")

    if buy_df is not None:
        print("Buying Stage Starting")

        print("Buying Stage Completed Successfully")


