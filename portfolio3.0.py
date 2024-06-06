# imports and variables
import datetime
import requests
import pandas as pd
import time
import numpy as np
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient
from ib_insync import *

ib = IB()
ib.connect('127.0.0.1', 7497, clientId=1)  # Change clientId if needed 

df1 = pd.DataFrame(columns=['Time','Ticker','Bid','Close','Ask'])
df2 = pd.DataFrame(columns=['Time','Ticker','Bid','Close','Ask'])
df3 = pd.DataFrame(columns=['Time','Ticker','Bid','Close','Ask'])
df4 = pd.DataFrame(columns=['Time','Ticker','Bid','Close','Ask'])
df5 = pd.DataFrame(columns=['Time','Ticker','Bid','Close','Ask'])
df6 = pd.DataFrame(columns=['Time','Ticker','Bid','Close','Ask'])

dfs = [df1, df2, df3, df4, df5, df6]
ib.reqMarketDataType(3)  # Delayed market data 15 mins, change to 1 for live data

# functions

# fetch new data
def fetch_new_data(symbol):
    tickerSymbol = Stock(f'{symbol}', 'SMART', 'USD') 
    ticker = ib.reqHistoricalData(contract = tickerSymbol, endDateTime = '', durationStr='1 D', 
                              barSizeSetting = '1 min', whatToShow='TRADES', useRTH=False, keepUpToDate=True)
    ticker = ticker[-5:]
    df = pd.DataFrame([vars(bar) for bar in ticker])
    df['Stock'] = tickerSymbol.symbol
    return df
# technicals

# buy

# hold

# sell

# scan
def scan():
    global x, held, TICKER, budget, df_budget, data, df, df_transactions, stop_loss
    #data = pd.read_csv(r'C:\Users\johnm\OneDrive\Desktop\MyResume\df.csv')
    df_stocks = pd.read_csv(r'C:\Users\johnm\OneDrive\Desktop\MyResume\stocks.csv')
    df_budget = pd.read_csv(r'C:\Users\johnm\OneDrive\Desktop\MyResume\portfolio_budget.csv')
    budget = df_budget.iloc[0,0]
    stock_dataframes = {}
    for symbol in df_stocks['stocks']:
        # Fetch new data for the stock
        stock_data = fetch_new_data(symbol)
        stock_dataframes[symbol] = stock_data
    print('starting technicals')
    for each df in stock_dataframes:
        technicals(df)
    if held == True:
        pass
    print(f'balance ${budget}')
    ib.sleep(60)
    # delete after go live with IB
    if len(df_transactions) > 0:
        # start on 2nd df to ask if stock should sell
        df.reset_index(drop=True, inplace=True)
        if df.iloc[1,8] == 'resistance' and df.iloc[1,9] == '':
            sell_stock()
        else:
            hold_stock()
# summary and notifications

# initialize

current_time = datetime.datetime.now().time()
print(current_time)
while current_time > datetime.time(15, 54) and current_time > datetime.time(9, 30):  
    scan()
    current_time = datetime.datetime.now().time()
    print(current_time)

print('out of time')