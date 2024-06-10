import pandas as pd
import config
from ib_insync import *


class Buy:
    def buy_stock(SHARES, BUDGET_df, df, ib, df_budget):
        global x, TICKER, current_time, buy_time, held, stop_loss
        total = config.strike_price*SHARES
        if total > BUDGET_df:
            print('out of money')
            return 'exited early'
        stock = Stock(f'{df.iloc[2,8]}', 'SMART', 'USD') 
        order = MarketOrder('BUY', SHARES)  
        trade = ib.placeOrder(stock, order)
        while not trade.isDone():
            ib.waitOnUpdate()
        print(f'Order Status: {trade.orderStatus.status}')
        account_summary = ib.accountSummary()
        for item in account_summary:
            if item.tag == 'AvailableFunds':
                print(f'{item.account}: Available Funds = {item.value} {item.currency}')
                BUDGET_ib = item.value
        held = True
        print(f'BUDGET_ib is {BUDGET_ib}.  BUDGET_df is {BUDGET_df}.')
        print('finished buy')