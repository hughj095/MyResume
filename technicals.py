import pandas as pd
import numpy as np
import datetime
from buy import Buy # custom class
import config 
from sell import Sell # custom class
from stoploss import StopLoss # custom class


class Technicals:
    def technicals(df, ib, BUDGET_ib, clock):
        if len(df) > 0:
            df['close'] = df['close'].astype(float)
            df['Resistance/Support'] = ''   # column 9
            # Time the following for loop against a vectorized operation: 
            for i in range(len(df)-1):
                if (
                        i >= 2 and i < len(df)-2 
                        and df.iloc[i - 1,4] >= df.iloc[i - 2,4]
                        and df.iloc[i,4] >= df.iloc[i - 1,4]
                        and df.iloc[i,4] >= df.iloc[i + 1,4]
                        and df.iloc[i + 1,4] >= df.iloc[i + 2,4]
                    ):
                        df.iloc[i, 9] = "resistance"
            for i in range(len(df)-1):   
                if (
                        i >= 2 and i < len(df) - 2
                        and df.iloc[i - 1,4] <= df.iloc[i - 2,4]
                        and df.iloc[i,4] <= df.iloc[i - 1,4]
                        and df.iloc[i,4] <= df.iloc[i + 1,4]
                        and df.iloc[i + 1,4] <= df.iloc[i + 2,4]
                    ):
                        df.iloc[i, 9] = "support"
            df['Break'] = '' # column 9
            count = 0
            for i in range(len(df)-1):
                if df.iloc[i,9] == "resistance":
                    count += 1
                for j in range(i-10,i-1):   ##### 10 minutes back from current i to look for breakthroughs
                    if (
                        df.iloc[i,9] == 'resistance'
                        and df.iloc[j,9] == 'resistance'
                        and df.iloc[i,4] > df.iloc[j,4] 
                        and count > 1
                        and len(df) > 10
                        ):
                            df.iloc[i,9] = "break"
            ## Trailing Stoploss check
            for i in range(len(df)-1, -1, -1):
                if df.loc[i,'Resistance/Support'] == 'support' and len(df) > 15:
                    price_column = df.loc[i:, 'close']
                    highafterbuy_index = price_column.idxmax()
                    highafterbuy = price_column.max()
                    StopLoss.trailingstoploss(positions, df, sell_ticker, highafterbuy, highafterbuy_index, ib, clock, i)
                    break
                break
            df = df[len(df)-5:len(df)]
            df = df.reset_index(drop=True)
            ## Volume indicator check
            df['VMA_20'] = df['volume'].rolling(window=20).mean()
            if len(df) < 5:
                pass
            elif df.iloc[2,11] < 3 * df.iloc[2,5]:
                volume_indic = True
            else: volume_indic = False   
            sell_ticker = df.iloc[0,8]
            current_time = datetime.datetime.now().time()
            clock = 0
            positions = ib.positions()
            for pos in positions:
                if sell_ticker == pos.contract.symbol:
                    owned_shares = pos.position
                else: owned_shares = 0
            owned_tickers = [position.contract.symbol for position in positions]
            ### DONT BUY IF LOWER THAN THE LAST STOP LOSS (HPE)
                ## append to 52weekTrue.csv if stock was stop lossed and clear at end of day
                # loop through csv to check if stock was stop lossed
            if df.iloc[2,9] == 'support' and sell_ticker not in owned_tickers and len(df) > 4:
                config.strike_price = df.iloc[2,4]
                if BUDGET_ib < 100000:
                    print('low on budget')
                SHARES = np.floor(BUDGET_ib/13/config.strike_price)
                Buy.buy_stock(SHARES, df, ib, BUDGET_ib, clock) # goes to buy.py
            elif volume_indic == True and sell_ticker not in owned_tickers: 
                print('high volume flag')
                Buy.buy_stock(SHARES, df, ib, BUDGET_ib, clock) # goes to buy.py
            if current_time > datetime.time(15, 40) and owned_shares > 0:
                Sell.sell_stock(sell_ticker, ib, df, clock) # goes to sell.py
            elif df.iloc[2,9] == 'resistance' and df.iloc[2,10] == '' and owned_shares > 0:
                Sell.sell_stock(sell_ticker, ib, df, clock)
            elif StopLoss.checkforstoploss(ib, sell_ticker):
                Sell.sell_stock(sell_ticker, ib, df, clock)
            return clock
