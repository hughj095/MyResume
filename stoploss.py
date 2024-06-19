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
    
    def trailingstoploss(positions, df, sell_ticker, highafterbuy, highafterbuy_index, ib, clock, i):
        # get current price
        current_price = df.iloc[len(df)-1,4]
        # avg cost
        for pos in positions:
            if (
                sell_ticker == pos.contract.symbol
                and highafterbuy - current_price > 0
                and current_price - pos.avgCost > 0
                and (highafterbuy - current_price) > (current_price - pos.avgCost)
                and highafterbuy_index > i + 15  # trailing stoploss starts 15 mins after buy, this is new
                ):
                    print('Trailing Stoploss activated')
                    Sell.sell_stock(sell_ticker, ib, df, clock)
            

