from ib_insync import *
from sell import Sell

class StopLoss:
    def checkforstoploss(ib, sell_ticker):
        # loop through each position for avg cost
        positions = ib.positions()
        for pos in positions:
            if sell_ticker == pos.contract.symbol:
                contract = Stock(f'{sell_ticker}', 'SMART', 'USD')
                ticker = ib.reqMktData(contract, '', False, False)
                ib.sleep(2)
                current_price = ticker.last if ticker.last else ticker.close
                if current_price < 0.995*pos.avgCost:
                    print('stop loss order true')
                    return True
    
    def trailingstoploss(ib, sell_ticker, highfrombuy):
        pass
        # avg cost per ticker
        # append high from buy
        # if price is 50% between avg cost and high from buy
        # then sell

