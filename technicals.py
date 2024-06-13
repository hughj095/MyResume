import pandas as pd
import numpy as np
import datetime
from buy import Buy # custom class
import config 
from sell import Sell # custom class


class Technicals:
    def technicals(df, ib, stock_dataframes, BUDGET_ib):
        if len(df) > 0:
            df['close'] = df['close'].astype(float)
            df['Resistance/Support'] = ''   # column 9
            for i in range(len(df)-1):
                if (
                        i < len(df)-2 
                        and df.iloc[i,4] >= df.iloc[i - 1,4]
                        and df.iloc[i,4] >= df.iloc[i - 2,4]
                        and df.iloc[i,4] >= df.iloc[i + 1,4]
                        and df.iloc[i,4] >= df.iloc[i + 2,4]
                    ):
                        df.iloc[i, 9] = "resistance"
            for i in range(len(df)-1):   
                if (
                        i >= 2 and i < len(df) - 2
                        and df.iloc[i,4] <= df.iloc[i - 1,4]
                        and df.iloc[i,4] <= df.iloc[i - 2,4]
                        and df.iloc[i,4] <= df.iloc[i + 1,4]
                        and df.iloc[i,4] <= df.iloc[i + 2,4]
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
                        and df.iloc[j,9] == ''
                        and df.iloc[i,3] > df.iloc[j,3] 
                        and count > 1
                        ):
                            df.iloc[i,9] = "break"
            df = df[len(df)-5:len(df)]
            df = df.reset_index(drop=True)
            df['volume'] = df['volume']
            df['VMA_20'] = df['volume'].rolling(window=20).mean()    
            sell_ticker = df.iloc[2,8]
            current_time = datetime.datetime.now().time()
            if df.iloc[2,9] == 'support':
                config.strike_price = df.iloc[2,4]
                if BUDGET_ib < 100:
                    print('low on budget')
                SHARES = np.floor(BUDGET_ib/30/config.strike_price)
                Buy.buy_stock(SHARES, df, ib, BUDGET_ib, sell_ticker) # goes to buy.py
            elif current_time > datetime.time(15, 54):
                Sell.sell_stock(sell_ticker, ib, df) # goes to sell.py
            else:
                if df.iloc[2,9] == 'resistance' and df.iloc[2,10] == '':
                    Sell.sell_stock(sell_ticker, ib, df)
