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

# functions

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
    for stock in df_stocks['stocks']:
        TICKER = stock
        print(TICKER)
        get_ticker_data(MULTIPLIER, TIMESPAN, DATESTART, DATEEND, APIKEY)
        print('starting technicals')
        technicals(data)
        if held == True:
            break
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
while current_time < datetime.time(15, 54) and current_time > datetime.time(9, 30):  
    scan()
    current_time = datetime.datetime.now().time()
    print(current_time)

print('out of time')