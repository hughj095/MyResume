import pandas as pd
import numpy as np
import datetime
from buy import Buy # custom class
import config 
from sell import Sell # custom class
from stoploss import StopLoss # custom class


class Technicals:
    def technicals(df, ib, BUDGET_ib):
        if len(df) > 0:
            df['close'] = df['close'].astype(float)
            df['Resistance/Support'] = ''   # column 9
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
                        ):
                            df.iloc[i,9] = "break"
            df = df[len(df)-5:len(df)]
            df = df.reset_index(drop=True)
            df['volume'] = df['volume']
            df['VMA_20'] = df['volume'].rolling(window=20).mean()    
            sell_ticker = df.iloc[2,8]
            current_time = datetime.datetime.now().time()
            clock = 0
            if df.iloc[2,9] == 'support':
                config.strike_price = df.iloc[2,4]
                if BUDGET_ib < 100:
                    print('low on budget')
                SHARES = np.floor(BUDGET_ib/13/config.strike_price)
                Buy.buy_stock(SHARES, df, ib, BUDGET_ib, clock) # goes to buy.py
            positions = ib.positions()
            for pos in positions:
                if sell_ticker == pos.contract.symbol:
                    owned_shares = pos.position
            if current_time > datetime.time(15, 50) and owned_shares > 0:
                Sell.sell_stock(sell_ticker, ib, df, clock) # goes to sell.py
            if df.iloc[2,9] == 'resistance' and df.iloc[2,10] == '' and owned_shares > 0:
                Sell.sell_stock(sell_ticker, ib, df, clock)
            if StopLoss.checkforstoploss(ib, sell_ticker):
                Sell.sell_stock(sell_ticker, ib, df, clock)
            return clock
