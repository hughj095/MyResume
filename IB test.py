### MUST BE LOGGED ONTO THE IB GETWAY ON THE DESKTOP

from ib_insync import *
import pandas as pd

# Connect to Interactive Brokers TWS or IB Gateway
ib = IB()
ib.connect('127.0.0.1', 7497, clientId=1)  # Change port for real money and clientId if needed  

# Define the stock you want to trade
'''positions = ib.positions()
for pos in positions:

        stock = Stock({pos.contract.symbol}, 'SMART', 'USD')

        # Define the order
        order = MarketOrder('SELL', pos.position)

        # Place the order
        trade = ib.placeOrder(stock, order)

        # Wait for the order to be filled
        while not trade.isDone():
            ib.waitOnUpdate()

        print(f'sold {pos.contract.symbol}')'''

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
account_summary = ib.accountSummary()
# Print available funds (TotalCashValue)
for item in account_summary:
    if item.tag == 'AvailableFunds':
        print(f'{item.account}: Available Funds = {item.value} {item.currency}')

### CURRENT POSITIONS
positions = ib.positions()
for pos in positions:
    print(f'Account: {pos.account}, Symbol: {pos.contract.symbol},' +
          f'Position: {round(pos.position,0)}, Average Cost: {round(pos.avgCost,2)},' +
          f'Value: {round(pos.avgCost * pos.position,2)}')

### TRANSACTION DETAIL
executions = ib.reqExecutions(ExecutionFilter())
for e in executions:
    print(f'Account: {e.execution.acctNumber}, Symbol: {e.contract.symbol}, '
          f'Side: {e.execution.side}, Shares: {e.execution.shares}, '
          f'Price: {e.execution.price}, Time: {e.execution.time}')
    
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


