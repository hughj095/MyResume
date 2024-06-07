# imports and variables
import datetime
import requests
import pandas as pd
import time
import numpy as np
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient
from ib_insync import *
from technicals import Technicals  # custom class
from hold import Hold # custom class
from buy import Buy # custom class
from sell import Sell # custom class
import config

ib = IB()
ib.connect('127.0.0.1', 7497, clientId=1)  # Change clientId if needed 
ib.reqMarketDataType(3)  # Live data, change to 3 for delayed prices
held = False
df_transactions = pd.DataFrame()

# functions

# fetch new data
def fetch_new_data(symbol):
    global held, BUDGET
    tickerSymbol = Stock(f'{symbol}', 'SMART', 'USD') 
    ticker = ib.reqHistoricalData(contract = tickerSymbol, endDateTime = '', durationStr='1 D', 
                              barSizeSetting = '1 min', whatToShow='TRADES', useRTH=False, keepUpToDate=True)
    ib.sleep(1)
    ticker = ticker[-15:]
    df = pd.DataFrame([vars(bar) for bar in ticker])
    df['Stock'] = tickerSymbol.symbol
    return df
# technicals

# buy

# hold

# sell

# scan
def scan():
    global x, held, TICKER, budget, data, df, df_transactions, stop_loss
    #data = pd.read_csv(r'C:\Users\johnm\OneDrive\Desktop\MyResume\df.csv')
    df_stocks = pd.read_csv(r'C:\Users\johnm\OneDrive\Desktop\MyResume\stocks.csv')
    account_summary = ib.accountSummary()
    for item in account_summary:
        if item.tag == 'AvailableFunds':
            BUDGET = item.value
    stock_dataframes = {}
    for symbol in df_stocks['stocks']:
        # Fetch new data for the stock
        stock_data = fetch_new_data(symbol)
        stock_dataframes[symbol] = stock_data
    print('starting technicals')
    for ticker, df in stock_dataframes.items():
        Technicals.technicals(df, ib)
    if held == True:
        pass
    df_transactions = pd.read_csv(r'C:\Users\johnm\OneDrive\Desktop\MyResume\transactions.csv')
    print(f'balance ${BUDGET}')
    ib.sleep(60)
    # delete after go live with IB
    if len(df_transactions) > 0:
        # start on 2nd df to ask if stock should sell
        for ticker, df in stock_dataframes.items():
            print(df)
            if df.iloc[12,9] == 'resistance' and df.iloc[12,9] == '':
                pass
                sell_ticker = df.iloc[12,8]
                # Sell.sell_stock(sell_ticker)
            else:
                pass
                #Hold.hold_stock()
# summary and notifications

# initialize

current_time = datetime.datetime.now().time()
print(current_time)
while current_time > datetime.time(15, 54) and current_time > datetime.time(9, 30):  
    scan()
    current_time = datetime.datetime.now().time()
    print(current_time)

print('out of time')