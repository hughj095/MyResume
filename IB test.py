### MUST BE LOGGED ONTO THE IB GETWAY ON THE DESKTOP


import time
from ib_insync import *

# Connect to Interactive Brokers TWS or IB Gateway
ib = IB()
ib.connect('127.0.0.1', 7497, clientId=1)  # Change clientId if needed

# Define the stock you want to trade
stock = Stock('IBM', 'NYSE', 'USD')

# Define the order
'''order = MarketOrder('BUY', 10)  # Buy 10 shares

# Place the order
trade = ib.placeOrder(stock, order)

# Wait for the order to be filled
while not trade.isDone():
    ib.waitOnUpdate()

# Print order status
print(f'Order Status: {trade.orderStatus.status}')'''

# Request account summary
'''account_summary = ib.accountSummary()

# Print available funds (TotalCashValue)
for item in account_summary:
    if item.tag == 'AvailableFunds':
        print(f'{item.account}: Available Funds = {item.value} {item.currency}')'''



# Disconnect from IB
ib.disconnect()


