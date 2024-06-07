from ib_insync import *

class Sell:
    def sell_stock(sell_ticker, ib):
        global x, TICKER, df_transactions, SHARES, strike_price, sell_time, current_time, sell_price, held, df_budget, budget, stop_loss
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
        df_budget.iloc[0,0] = item.value
        df_budget.to_csv(r'C:\Users\johnm\OneDrive\Desktop\MyResume\portfolio_budget.csv', index=False)