import pandas as pd
import config
from ib_insync import *


class Buy:
    def buy_stock(SHARES, BUDGET, df, ib, df_budget):
        global x, TICKER, current_time, buy_time, held, stop_loss
        df_transactions = pd.read_csv(r'C:\Users\johnm\OneDrive\Desktop\MyResume\transactions.csv') #### NEED SOMETHING TO DETERMINE IF DF_TRANSACTIONS SHOULD READ FROM SAVED OR SHOULD BE BLANK AT BEGINNING OF DAY
        total = config.strike_price*SHARES
        if total > BUDGET:
            print('out of money')
            return 'exited early'
            ###### BREAK OUT OF A FUNCTION HERE AND GO BACK TO START
        ### ACTUAL BUY HERE
        stock = Stock(f'{df.iloc[0,8]}', 'SMART', 'USD') 
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
        x = len(df_transactions)
        df_transactions.loc[x, 'Ticker'] = df.iloc[0,8]
        df_transactions.loc[x, 'Strike Price'] = config.strike_price
        df_transactions.loc[x, 'Stop Loss'] = 0.99 * config.strike_price
        df_transactions.loc[x, 'Buy Time'] = df.iloc[2,0]
        df_transactions.loc[x, 'Shares'] = SHARES
        df_transactions.loc[x, 'Buy Total'] = total
        held = True
        df_transactions.to_csv(r'C:\Users\johnm\OneDrive\Desktop\MyResume\transactions.csv', index=False)
        df_budget.iloc[0,0] = BUDGET
        df_budget.to_csv(r'C:\Users\johnm\OneDrive\Desktop\MyResume\portfolio_budget.csv', index=False)
        print('finished buy')