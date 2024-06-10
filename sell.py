from ib_insync import *

class Sell:
    def sell_stock(sell_ticker, ib, df_budget, BUDGET_df):
        print('start of sell function')
        positions = ib.positions()
        for pos in positions:
            if pos.contract.symbol == sell_ticker:
                SHARES = pos.position
        stock = Stock(f'{sell_ticker}', 'SMART', 'USD')
        order = MarketOrder('SELL', SHARES)
        trade = ib.placeOrder(stock, order)
        while not trade.isDone():
            ib.waitOnUpdate()
        print(f'sold {sell_ticker}') 
        held = False
        account_summary = ib.accountSummary()
        for item in account_summary:
            if item.tag == 'AvailableFunds':
                print(f'{item.account}: Available Funds = {item.value} {item.currency}')
                BUDGET_ib = item.value
        print(f'BUDGET_ib is {BUDGET_ib}.  BUDGET_df is {BUDGET_df}.')