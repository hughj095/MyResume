### MUST BE LOGGED ONTO THE IB GETWAY ON THE DESKTOP


import time
from ib_insync import *
import pandas as pd
import datetime

# Connect to Interactive Brokers TWS or IB Gateway
ib = IB()
ib.connect('127.0.0.1', 7497, clientId=1)  # Change clientId if needed  

# Define the stock you want to trade
stock = Stock('AAPL', 'SMART', 'USD') 

# Define the order
'''order = MarketOrder('BUY', 10)  # Buy 10 shares 

# Place the order
trade = ib.placeOrder(stock, order)

# Wait for the order to be filled
while not trade.isDone():
    ib.waitOnUpdate()'''

df = pd.DataFrame(columns=['Time','Ticker','Bid','Close','Ask'])
ib.reqMarketDataType(3)

ticker = ib.reqMktData(stock, '', False, False)
ib.sleep(1)
data = [datetime.datetime.now().time(), ticker.contract.symbol, ticker.bid, ticker.close, ticker.ask]
df.loc[len(df)] = data
print(df)

'''# Print order status
print(f'Order Status: {trade.orderStatus.status}')'''

# Request account summary
'''account_summary = ib.accountSummary()

# Print available funds (TotalCashValue)
for item in account_summary:
    if item.tag == 'AvailableFunds':
        print(f'{item.account}: Available Funds = {item.value} {item.currency}')'''
'''def onTick(ticker):
    print(f"Bid: {ticker.bid}, Ask: {ticker.ask}, Last: {ticker.last}")

# Request real-time market data
ticker = ib.reqMktData(stock, '', False, False)
ticker.updateEvent += onTick

# Keep the script running to continuously receive data
try:
    while True:
        ib.sleep(1)
except KeyboardInterrupt:
    print("Interrupted by user")


# Disconnect from IB
ib.disconnect()'''


