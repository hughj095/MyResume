# imports and variables
import datetime
import pandas as pd
from ib_insync import *
import time
from twilio.rest import Client
from technicals import Technicals  # custom class
from fifty_two_week import Refresh52Week # custom class
from sell import Sell # custom class
from report import Report # custom class
import config

ib = IB()
ib.connect('127.0.0.1', 7497, clientId=1)
ib.reqMarketDataType(3)  # Delayed data, change to 1 for live prices

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
    clock = 0
    for ticker, df in stock_dataframes.items():
        Technicals.technicals(df, ib, BUDGET_ib, clock, df_stocks)  # goes to technicals.py in folder
    for item in account_summary:
        if item.tag == 'AvailableFunds':
            print(f'Available Funds = {item.value} {item.currency}')
            BUDGET_ib = item.value
    positions = ib.positions()
    for pos in positions:
        print(f'Account: {pos.account}, Symbol: {pos.contract.symbol},' +
          f'Position: {round(pos.position,0)}, Average Cost: {round(pos.avgCost,2)},' +
          f'Value: {round(pos.avgCost * pos.position,2)}')
    if clock > 0 and clock < 60:  ## TIMER NOT WORKING
        ib.sleep(60-clock)

# sell at end of day
def endOfDaySell(ib):
    positions = ib.positions()
    if len(positions) > 0:
        for pos in positions:
            if pos.position > 0:
                stock = Stock(pos.contract.symbol, 'SMART', 'USD')
                order = MarketOrder('SELL', pos.position)
                trade = ib.placeOrder(stock, order)
                start_time = time.time()
                while not trade.isDone():
                    if time.time() - start_time > 60:
                        print("Timeout reached, cancelling order")
                        ib.cancelOrder(order)
                        #Sell.chuncking_sell(ib, SHARES = pos.position, sell_ticker = pos.contract.symbol)
                        break
                    ib.sleep(1)
                print(f'sold {pos.contract.symbol}')

# sends text of portfolio sum to my phone
def send_text(total_portfolio_value):
    account_sid = config.TWILIO_ACCOUNT_SID
    auth_token = config.TWILIO_AUTH_TOKEN 
    client = Client(account_sid, auth_token)
    account_summary = ib.accountSummary()
    for item in account_summary:
        if item.tag == 'AvailableFunds':
            BUDGET_ib = float(item.value)
    message = client.messages \
        .create(
        body= f"Total after close today is ${total_portfolio_value:,.2f}",
        from_='+18334029267',
        to='+18453723892'
        )

# Refresh 52 Week list and call send_text()
def mopUp():
    current_time = datetime.datetime.now().time()
    date = datetime.date.today()
    if current_time >= datetime.time(15,40):
        Refresh52Week.main() 
        Report.report() # includes upload()
        total_portfolio_value = send_text(total_portfolio_value) ## include total portfolio value from Report
        print("that's all folks")

# initialize
current_time = datetime.datetime.now().time()
print(current_time)
while current_time < datetime.time(15, 40) and current_time >= datetime.time(9, 18):  
    scan()
    current_time = datetime.datetime.now().time()
    print(current_time)
if current_time >= datetime.time(15,40) and current_time < datetime.time(16,00):
    endOfDaySell(ib)
    mopUp()



