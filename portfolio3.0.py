# imports and variables
import datetime
import pandas as pd
import numpy as np
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient
from ib_insync import *
from technicals import Technicals  # custom class
import config

ib = IB()
ib.connect('127.0.0.1', 7497, clientId=1)
ib.reqMarketDataType(3)  # Delayed data, change to 1 for live prices
held = False

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
        stock_data = fetch_new_data(symbol)
        stock_dataframes[symbol] = stock_data
    print('starting technicals')
    for ticker, df in stock_dataframes.items():
        Technicals.technicals(df, ib, stock_dataframes)
    print(f'balance ${BUDGET}')
    ib.sleep(60)

# summary and notifications
def send_text():
    account_sid = config.TWILIO_ACCOUNT_SID
    auth_token = config.TWILIO_AUTH_TOKEN
    proxy_client = TwilioHttpClient()   
    client = Client(account_sid, auth_token, http_client=proxy_client) # may not need http_client tag
    account_summary = ib.accountSummary()
    for item in account_summary:
        if item.tag == 'AvailableFunds':
            BUDGET = item.value
    message = client.messages.create(
        body= f"Portfolio total after close today is ${BUDGET}",
        from_='+18334029267',
        to='+18453723892'
        )
    message.sid

# initialize
current_time = datetime.datetime.now().time()
print(current_time)
while current_time < datetime.time(15, 54) and current_time > datetime.time(9, 30):  
    scan()
    current_time = datetime.datetime.now().time()
    print(current_time)
print('out of time')
if current_time >= datetime.time(15,54):
    send_text()