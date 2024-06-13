# imports and variables
import datetime
import pandas as pd
import numpy as np
from ib_insync import *
import time
from twilio.rest import Client
from technicals import Technicals  # custom class
from fifty_two_week import Refresh52Week # custom class
import config

ib = IB()
ib.connect('127.0.0.1', 7497, clientId=2)
ib.reqMarketDataType(3)  # Delayed data, change to 1 for live prices
held = False

# functions

# fetches new data
def fetch_new_data(symbol):
    tickerSymbol = Stock(f'{symbol}', 'SMART', 'USD') 
    ticker = ib.reqHistoricalData(contract = tickerSymbol, endDateTime = '', durationStr='1 D', 
                              barSizeSetting = '1 min', whatToShow='TRADES', useRTH=False, keepUpToDate=True)
    ib.sleep(1)
    ticker = ticker[-15:]
    df = pd.DataFrame([vars(bar) for bar in ticker])
    df['Stock'] = tickerSymbol.symbol
    return df

# calls to fetch data, apply technical analysis, and summarizes total and positions 
    # before and after returning from buy and sell functions 
def scan():
    df_stocks = pd.read_csv(r'C:\Users\johnm\OneDrive\Desktop\MyResume\52weekTrue.csv')
    account_summary = ib.accountSummary()
    for item in account_summary:
        if item.tag == 'AvailableFunds':
            BUDGET_ib = float(item.value)
    stock_dataframes = {}
    print('pulling data')
    for symbol in df_stocks['Stock Symbol']:
        stock_data = fetch_new_data(symbol)
        stock_dataframes[symbol] = stock_data
    print('starting technicals')
    for ticker, df in stock_dataframes.items():
        Technicals.technicals(df, ib, stock_dataframes, BUDGET_ib)  # goes to technicals.py in folder
    for item in account_summary:
        if item.tag == 'AvailableFunds':
            print(f'Available Funds = {item.value} {item.currency}')
            BUDGET_ib = item.value
    positions = ib.positions()
    for pos in positions:
        print(f'Account: {pos.account}, Symbol: {pos.contract.symbol},' +
          f'Position: {round(pos.position,0)}, Average Cost: {round(pos.avgCost,2)},' +
          f'Value: {round(pos.avgCost * pos.position,2)}')
    ib.sleep(60)

# sends text of portfolio sum to my phone
def send_text():
    account_sid = config.TWILIO_ACCOUNT_SID
    auth_token = config.TWILIO_AUTH_TOKEN 
    client = Client(account_sid, auth_token)
    account_summary = ib.accountSummary()
    for item in account_summary:
        if item.tag == 'AvailableFunds':
            BUDGET_ib = float(item.value)
    message = client.messages \
        .create(
        body= f"Total after close today is ${BUDGET_ib:,.2f}",
        from_='+18334029267',
        to='+18453723892'
        )

# initialize
current_time = datetime.datetime.now().time()
print(current_time)
while current_time < datetime.time(15, 50) and current_time >= datetime.time(9, 30):  
    scan()
    current_time = datetime.datetime.now().time()
    print(current_time)

# EOD Sell
if current_time >= datetime.time(15,50):
    positions = ib.positions()
    ## While len(pos) > 0 then keep trying to sell
    for pos in positions:
        stock = Stock(pos.contract.symbol, 'SMART', 'USD')
        order = MarketOrder('SELL', pos.position)
        trade = ib.placeOrder(stock, order)
        start_time = time.time()
        while not trade.isDone():
            if time.time() - start_time > 90:
                print("Timeout reached, cancelling order")
                ib.cancelOrder(order)
                ## Function to split order into chuncks
                break
            ib.sleep(1)
        print(f'sold {pos.contract.symbol}')
current_time = datetime.datetime.now().time()

# Refresh 52 Week list and call send_text()
if current_time >= datetime.time(15,50):
    Refresh52Week.main() # goes to fifty_two_week.py in folder
    send_text()
    print("that's all folks")
elif current_time < datetime.time(9,30):
    print('too early')