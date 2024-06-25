import pandas as pd
import config
from ib_insync import *
import time


class Buy:
    def buy_stock(SHARES, df, ib, BUDGET_ib, clock):
        total = df.iloc[2,4]*SHARES
        if total >= BUDGET_ib:
            print('out of money')
            return 'exited early'
        print('start of buy function')
        stock = Stock(f'{df.iloc[2,8]}', 'SMART', 'USD') 
        order = MarketOrder('BUY', SHARES)   
        trade = ib.placeOrder(stock, order)
        print(f'Buying {stock}, ${df.iloc[2,4]}, ${float(SHARES*df.iloc[2,4])}')
        start_time = time.time()
        while not trade.isDone():
            if time.time() - start_time > 30:
                print("Timeout reached, cancelling order")
                ib.cancelOrder(order)
                ## Function to split order into chuncks
                break
            # Sleep briefly to avoid tight loop
            ib.sleep(1)
            clock += 1
        print(f'Order Status: {trade.orderStatus.status}')
        account_summary = ib.accountSummary()
        for item in account_summary:
            if item.tag == 'AvailableFunds':
                print(f'Available Funds = {item.value} {item.currency}')
                BUDGET_ib = item.value
        print('finished buy')
        return clock
    
    def buy_etf(ib, BUDGET_ib, market_bull, market_bear):
        if market_bull == True:
            stock = Stock('SPXL', 'SMART', 'USD')
            order = MarketOrder('BUY', BUDGET_ib/6/146)  #include pull of SPXL price
            trade = ib.placeOrder(stock, order)
            start_time = time.time()
            while not trade.isDone():
                if time.time() - start_time > 20:
                    print("Timeout reached, cancelling order")
                    ib.cancelOrder(order)
                ## Function to split order into chuncks
                ib.sleep(1)
            print('bought SPXL on bull market')
            ## ADD TO 52weekTrue