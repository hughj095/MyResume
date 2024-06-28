import numpy as np
import datetime
from buy import Buy # custom class
from sell import Sell # custom class
from stoploss import StopLoss # custom class


class Technicals:
    def technicals(df, ib, BUDGET_ib, clock, df_stocks, SHARES):
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
                        and len(df) > 10
                        and df.iloc[j,9] == 'resistance'
                        and df.iloc[i,4] > df.iloc[j,4] 
                        and count > 1
                        ):
                            df.iloc[i,10] = "break"
            ## Trailing Stoploss check
            positions = ib.positions()
            sell_ticker = df.iloc[0,8]
            for i in range(len(df)-1, -1, -1):
                if len(df) > 14:
                    price_column = df['close']
                    highafterbuy_index = price_column.idxmax()
                    highafterbuy = price_column.max()
                    StopLoss.trailingstoploss(positions, df, sell_ticker, highafterbuy, highafterbuy_index, ib, clock, i, df_stocks)
                    break
                break
            df['VMA_20'] = df['volume'].rolling(window=20).mean()
            df = df[len(df)-5:len(df)]
            SHARES = np.floor(SHARES/df.iloc[0,4])
            df = df.reset_index(drop=True)
            ## Volume indicator check
            if len(df) < 5:
                volume_indic = False
                pass
            elif df.iloc[2,11] < 3 * df.iloc[2,5]:
                volume_indic = True
                print('volume indicator TRUE')
            else: volume_indic = False
            current_time = datetime.datetime.now().time()
            clock = 0
            for pos in positions:
                if sell_ticker == pos.contract.symbol:
                    owned_shares = pos.position
                else: owned_shares = 0
            owned_tickers = [position.contract.symbol for position in positions]
            # Lookup if stock was stop lossed today
            stop_loss_flag = False
            for index, row in df_stocks.iterrows():
                ticker = row['Stock Symbol']
                stop_loss_today = row['Stop Loss Today']
                if ticker == sell_ticker and stop_loss_today == True:
                    stop_loss_flag = True
                    break
            # BUY criteria
            if sell_ticker not in owned_tickers and len(df) > 4 and df.iloc[2,9] == 'support' and stop_loss_flag == False:
                if BUDGET_ib < 100000:
                    print('low on budget')
                else: clock = Buy.buy_stock(SHARES, df, ib, BUDGET_ib, clock) # goes to buy.py
            elif volume_indic == True and sell_ticker not in owned_tickers and stop_loss_flag == False: 
                print('high volume flag')
                SHARES = np.floor(BUDGET_ib/len(df_stocks)/df.iloc[2,4])
                clock = Buy.buy_stock(SHARES, df, ib, BUDGET_ib, clock) # goes to buy.py
            # SELL Criteria
            if current_time > datetime.time(15, 40) and owned_shares > 0:
                Sell.sell_stock(sell_ticker, ib, df, clock) # goes to sell.py
            elif StopLoss.checkforstoploss(ib, sell_ticker, clock):
                clock = Sell.sell_stock(sell_ticker, ib, df, clock)
                for ticker, stop_loss_today in zip(df_stocks['Stock Symbol'], df_stocks['Stop Loss Today']):
                    if ticker == sell_ticker:
                        # Update the 'Stop Loss Today' column for the row matching sell_ticker
                        df_stocks.loc[df_stocks['Stock Symbol'] == ticker, 'Stop Loss Today'] = True
                        df_stocks.loc[df_stocks['Stock Symbol'] == ticker, 'Stop Price'] = df.iloc[len(df)-1,4]
                df_stocks.to_csv(r'C:\Users\johnm\OneDrive\Desktop\MyResume\52weekTrue.csv', index=False)
            return clock
