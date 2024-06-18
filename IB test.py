### MUST BE LOGGED ONTO THE IB GETWAY ON THE DESKTOP

from ib_insync import *
import pandas as pd
import time

# Connect to Interactive Brokers TWS or IB Gateway
ib = IB()
ib.connect('127.0.0.1', 7497, clientId=1)  # Change port for real money and clientId if needed  

# Define the stock you want to trade
#positions = ib.positions()
'''for pos in positions:'''

stock = Stock('COST', 'SMART', 'USD')

# Define the order
order = MarketOrder('BUY', 80)

# Place the order
trade = ib.placeOrder(stock, order)

# Wait for the order to be filled
start_time = time.time()
while not trade.isDone():
    if time.time() - start_time > 20:
        print("Timeout reached, cancelling order")
        ib.cancelOrder(order)
    ## Function to split order into chuncks
    ib.sleep(1)
'''for fill in trade.fills:
    print(f"Selling {pos.contract.symbol}, Net: {(fill.execution.price - pos.avgCost)*pos.position}")
print(f'sold {pos.contract.symbol}')'''

open_orders = ib.reqOpenOrders()
for order in open_orders:
     print(order)

#df = pd.DataFrame(columns=['Time','Ticker','Bid','Close','Ask'])
#ib.reqMarketDataType(3)

'''ticker = ib.reqMktData(stock, '', False, False)
ib.sleep(1)
data = [datetime.datetime.now().time(), ticker.contract.symbol, ticker.bid, ticker.close, ticker.ask]
df.loc[len(df)] = data
print(df)'''

'''ticker = ib.reqHistoricalData(contract = stock, endDateTime = '', durationStr='1 D', 
                              barSizeSetting = '1 min', whatToShow='TRADES', useRTH=False, keepUpToDate=True)
ticker = ticker[-5:]
df = pd.DataFrame([vars(bar) for bar in ticker])
df['Stock'] = stock.symbol
print(df)'''

'''# Print order status
print(f'Order Status: {trade.orderStatus.status}')'''

# Request account summary
'''account_summary = ib.accountSummary()
# Print available funds (TotalCashValue)
for item in account_summary:
    if item.tag == 'AvailableFunds':
        print(f'{item.account}: Available Funds = {item.value} {item.currency}')'''

### CURRENT POSITIONS
positions = ib.positions()
for pos in positions:
    print(f'Account: {pos.account}, Symbol: {pos.contract.symbol},' +
          f'Position: {round(pos.position,0)}, Average Cost: {round(pos.avgCost,2)},' +
          f'Value: {round(pos.avgCost * pos.position,2)}')

### TRANSACTION DETAIL
'''executions = ib.reqExecutions(ExecutionFilter())
for e in executions:
    print(f'Account: {e.execution.acctNumber}, Symbol: {e.contract.symbol}, '
          f'Side: {e.execution.side}, Shares: {e.execution.shares}, '
          f'Price: {e.execution.price}, Time: {e.execution.time}')'''
    
'''def onTick(ticker):
    print(f"Bid: {ticker.bid}, Ask: {ticker.ask}, Last: {ticker.last}")''''''

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


