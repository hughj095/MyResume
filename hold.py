import pandas as pd
import datetime
from sell import Sell # custom class

class Hold:
    def hold_stock():
        global x, df_transactions, current_time, SHARES, strike_price, df, buy_time, held, stop_loss, sell_price, sell_time
        sell = False
        df_transactions = pd.read_csv(r'C:\Users\johnm\OneDrive\Desktop\MyResume\transactions.csv')
        if df.iloc[1,8] == 'resistance' and df.iloc[1,9] == '' and buy_time < df.iloc[1,6]:  ### BUY TIME MAY NOT BE NECESSARY
            sell_time = df.iloc[1,6]
            sell_price = df.iloc[1,3]
            sell = True
            buy = False
            Sell.sell_stock()
            current_time = datetime.datetime.now().time()
        elif df.iloc[1,3] < 0.99 * df_transactions.iloc[1,1]:
            print('stop loss')
            stop_loss = True
            Sell.sell_stock()
        elif current_time < datetime.time(15, 54) and current_time > datetime.time(9, 30) and sell == False:
            data = get_ticker_data(TICKER, MULTIPLIER, TIMESPAN, DATESTART, DATEEND, APIKEY)
            df.to_csv(r'C:\Users\johnm\OneDrive\Desktop\MyResume\df.csv', index = False)
            pass
        else: # if end of day then sell
            sell_time = df.iloc[1,6]
            sell_price = df.iloc[1,3]
            Sell.sell_stock()
