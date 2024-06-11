import pandas as pd
import config
from ib_insync import *
import time


class Buy:
    def buy_stock(SHARES, df, ib, BUDGET_ib):
        total = config.strike_price*SHARES
        if total >= BUDGET_ib:
            print('out of money')
            return 'exited early'
        print('start of buy function')
        stock = Stock(f'{df.iloc[2,8]}', 'SMART', 'USD') 
        order = LimitOrder('BUY', SHARES, lmtPrice = config.strike_price*1.003, tif='GTC' )   
        trade = ib.placeOrder(stock, order)
        print(f'Buying {stock}, ${float(SHARES*config.strike_price)}')
        ##### start a timer here, if over 10 seconds then subtract from wait timer at end of scan loop
        start_time = time.time()
        while not trade.isDone():
            if time.time() - start_time > 90:
                print("Timeout reached, cancelling order")
                ib.cancelOrder(order)
                break
            # Sleep briefly to avoid tight loop
            ib.sleep(1)
        print(f'Order Status: {trade.orderStatus.status}')
        account_summary = ib.accountSummary()
        for item in account_summary:
            if item.tag == 'AvailableFunds':
                print(f'Available Funds = {item.value} {item.currency}')
                BUDGET_ib = item.value
        held = True
        print('finished buy')