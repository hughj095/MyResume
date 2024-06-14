from ib_insync import *
import time

class Sell:
    def sell_stock(sell_ticker, ib, df, clock):
        positions = ib.positions()
        for pos in positions:
            if pos.contract.symbol == sell_ticker:
                print('start of sell function')
                SHARES = pos.position
                stock = Stock(f'{sell_ticker}', 'SMART', 'USD')
                order = MarketOrder('SELL', SHARES)
                trade = ib.placeOrder(stock, order)
                start_time = time.time()
                while not trade.isDone():
                    if time.time() - start_time > 90:
                        print("Timeout reached, cancelling order")
                        ib.cancelOrder(order)
                        ## Function to split order into chuncks
                        break
                    ib.sleep(1)
                    clock += 1
                for fill in trade.fills:
                    print(f"Selling {sell_ticker}, Net: {(fill.execution.price - pos.avgCost)*SHARES}")
                    print(f'sold {sell_ticker}') 
            elif len(pos.contract.symbol) == 0:
                print('position not held, tried to sell')
        account_summary = ib.accountSummary()
        for item in account_summary:
            if item.tag == 'AvailableFunds':
                print(f'{item.account}: Available Funds = {item.value} {item.currency}')
                BUDGET_ib = item.value
        return clock