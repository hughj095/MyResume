import pandas as pd
import numpy as np
from buy import Buy # custom class
import config # config file for global variables
from sell import Sell # custom class

class Technicals:
    def technicals(df, ib, stock_dataframes):
        global held
        df['close'] = df['close'].astype(float)
        df['Resistance/Support'] = ''   # column 9
        for i in range(len(df)-1):
            if (
                    df.iloc[i,4] >= df.iloc[i - 1,4]
                    and df.iloc[i,4] >= df.iloc[i - 2,4]
                    and df.iloc[i,4] >= df.iloc[i + 1,4]
                    and (i < len(df)-2 and df.iloc[i,4] >= df.iloc[i + 2,4])
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
        df.to_csv(r'C:\Users\johnm\OneDrive\Desktop\MyResume\df.csv', index=False)      
        print('saved df in technicals')
        df = df[len(df)-5:len(df)]
        df = df.reset_index(drop=True)
        #### IDENTIFY HERE WHICH STOCK ARE HELD
        if df.iloc[2,9] == 'support' and config.held == False:
            config.strike_price = df.iloc[2,4]
            df_budget = pd.read_csv(r'C:\Users\johnm\OneDrive\Desktop\MyResume\portfolio_budget.csv')
            BUDGET = df_budget.iloc[0,0]
            SHARES = np.floor(BUDGET/6/config.strike_price)
            buy = True
            buy_time = df.iloc[len(df)-3,0] 
            Buy.buy_stock(SHARES, BUDGET, df, ib, df_budget)
        else:
            for ticker, df in stock_dataframes.items():
                print(df)
                if df.iloc[12,9] == 'resistance' and df.iloc[12,9] == '':
                    sell_ticker = df.iloc[12,8]
                    Sell.sell_stock(sell_ticker)
