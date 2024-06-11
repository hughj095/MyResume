from ib_insync import *

class Sell:
    def sell_stock(sell_ticker, ib, df):
        positions = ib.positions()
        for pos in positions:
            if pos.contract.symbol == sell_ticker:
                print('start of sell function')
                SHARES = pos.position
                stock = Stock(f'{sell_ticker}', 'SMART', 'USD')
                order = MarketOrder('SELL', SHARES)
                trade = ib.placeOrder(stock, order)
                print(f'Selling {stock}, ${SHARES * df.iloc[2,4]}')
                #### timer here to subtract from minute timer after scan
                while not trade.isDone():
                    ib.waitOnUpdate()
                total = SHARES * df.iloc[2,4]
                print(f'sold {sell_ticker}') 
                held = False
            elif len(pos.contract.symbol) == 0:
                print('position not held, tried to sell')
        account_summary = ib.accountSummary()
        for item in account_summary:
            if item.tag == 'AvailableFunds':
                print(f'{item.account}: Available Funds = {item.value} {item.currency}')
                BUDGET_ib = item.value
        print(f'BUDGET_ib is ${BUDGET_ib}.')  