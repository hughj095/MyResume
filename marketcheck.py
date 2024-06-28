from ib_insync import *
import pandas as pd
df_market = []
class CheckMarket:
    def check_market(ib):
        market_bull = False
        tickerSymbol = Stock('DIA', 'SMART', 'USD') 
        ticker = ib.reqHistoricalData(contract = tickerSymbol, endDateTime = '', durationStr='1 D', 
                              barSizeSetting = '1 min', whatToShow='TRADES', useRTH=False, keepUpToDate=True)
        ib.sleep(1)
        df = pd.DataFrame([vars(bar) for bar in ticker])
        df_market = pd.read_csv(r'C:\Users\johnm\OneDrive\Desktop\MyResume\df.csv')
        new_index = len(df_market)
        df_market.loc[new_index,'DJIA'] = df.iloc[len(df)-1,4]
        tickerSymbol = Stock('QQQ', 'SMART', 'USD') 
        ticker = ib.reqHistoricalData(contract = tickerSymbol, endDateTime = '', durationStr='1 D', 
                              barSizeSetting = '1 min', whatToShow='TRADES', useRTH=False, keepUpToDate=True)
        ib.sleep(1)
        df = pd.DataFrame([vars(bar) for bar in ticker])
        df_market.loc[new_index,'NASDAQ'] = df.iloc[len(df)-1,4]
        df_market = df_market.tail(3)
        df_market.to_csv(r'C:\Users\johnm\OneDrive\Desktop\MyResume\df.csv', mode='w', index=False)
        if (
            len(df_market) > 2 
            and df_market.iloc[len(df_market)-1,0] > df_market.iloc[len(df_market)-2,0] > df_market.iloc[len(df_market)-3,0]
            and df_market.iloc[len(df_market)-1,1] > df_market.iloc[len(df_market)-2,1] > df_market.iloc[len(df_market)-3,1]
            ):
            market_bull = True
            market_bear = False
            print('Bull Market')
        elif (
            len(df_market) > 2 
            and df_market.iloc[len(df_market)-1,0] < df_market.iloc[len(df_market)-2,0] < df_market.iloc[len(df_market)-3,0]
            and df_market.iloc[len(df_market)-1,1] < df_market.iloc[len(df_market)-2,1] < df_market.iloc[len(df_market)-3,1]
            ):
            market_bull = False
            market_bear = True
            print('Bear Market')
        else: 
            market_bull = False
            market_bear = False
        return market_bull, market_bear
        