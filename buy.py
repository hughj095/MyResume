import pandas as pd
import config
from ib_insync import *


class Buy:
    def buy_stock(SHARES, df, ib, BUDGET_ib):
        total = config.strike_price*SHARES
        if total >= BUDGET_ib:
            print('out of money')
            return 'exited early'
        print('start of buy function')
        stock = Stock(f'{df.iloc[2,8]}', 'SMART', 'USD') 
        order = MarketOrder('BUY', SHARES)   
        trade = ib.placeOrder(stock, order)
        print(f'Buying {stock}, ${SHARES*config.strike_price}')
        ##### start a timer here, if over 10 seconds then subtract from wait timer at end of scan loop
        while not trade.isDone():
            ib.waitOnUpdate()
        print(f'Order Status: {trade.orderStatus.status}')
        account_summary = ib.accountSummary()
        for item in account_summary:
            if item.tag == 'AvailableFunds':
                print(f'Available Funds = {item.value} {item.currency}')
                BUDGET_ib = item.value
        held = True
        print('finished buy')