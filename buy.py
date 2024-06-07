import pandas as pd
import config
from ib_insync import *


class Buy:
    def buy_stock(SHARES, BUDGET, df, ib, df_budget):
        global x, TICKER, current_time, buy_time, held, stop_loss
        total = config.strike_price*SHARES
        if total > BUDGET:
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
                BUDGET = item.value
        held = True
        df_budget.iloc[0,0] = BUDGET
        df_budget.to_csv(r'C:\Users\johnm\OneDrive\Desktop\MyResume\portfolio_budget.csv', index=False)
        print('finished buy')