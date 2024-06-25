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
        df_market = pd.read_csv(r'C:\Users\johnm\OneDrive\Desktop\MyResume\52weekTrue.csv')
        df_market.append(ticker.last)
        df_market.to_csv(r'C:\Users\johnm\OneDrive\Desktop\MyResume\52weekTrue.csv', if_exists = 'append', index=False)
        if df_market.loc[len(df_market)-1,0] > df_market.loc[len(df_market)-2,0]:
            market_bull = True
            print('Bull Market')
        return market_bull
        