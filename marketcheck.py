from ib_insync import *
import pandas as pd
ib = IB()
df_market = []
class CheckMarket:
    def check_market():
        market_bull = False
        djia_contract = Index(symbol='DJX', exchange='CBOE')
        ticker = ib.reqMktData(djia_contract, '', False, False)
        ib.sleep(1)
        print(f"DJIA Last Price: {ticker.last}")
        df_market = pd.read_csv(r'C:\Users\johnm\OneDrive\Desktop\MyResume\df.csv')
        df_market.append(ticker.last)
        df_market.to_csv(r'C:\Users\johnm\OneDrive\Desktop\MyResume\df.csv', if_exists = 'append', index=False)
        if len(df_market > 3) and df_market.loc[len(df_market)-1,0] > df_market.loc[len(df_market)-2,0] > df_market.loc[len(df_market)-3,0]:
            market_bull = True
            market_bear = False
            print('Bull Market')
        elif len(df_market > 3) and df_market.loc[len(df_market)-1,0] < df_market.loc[len(df_market)-2,0] < df_market.loc[len(df_market)-3,0]:
            market_bull = False
            market_bear = True
        else: 
            market_bull = False
            market_bear = False
        return market_bull, market_bear
        