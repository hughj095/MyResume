### imports, variables and functions
import requests
import pandas as pd
import datetime
import time
import numpy as np

TICKER = 'AAPL'
MULTIPLIER = '5'
TIMESPAN = 'minute'
DATESTART = '2024-05-03'
DATEEND = '2024-05-03'
APIKEY = 'hldKpOcQ9ago1ZA83XRyRQ1tFG5uokBa'
SHARES = 4

# API DATA PULL
def get_ticker_data(TICKER, MULTIPLIER, TIMESPAN, DATESTART, DATEEND, APIKEY):
    url = f'https://api.polygon.io/v2/aggs/ticker/{TICKER}/range/{MULTIPLIER}/{TIMESPAN}/{DATESTART}/{DATEEND}?apiKey={APIKEY}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print('pulled API')
        return data
    else:
        print('Error:', response.status_code, response.content)
        return None

def timer(minutes):
    seconds = minutes * 60
    print('started timer')
    while seconds:
        mins, secs = divmod(seconds, 60)
        time.sleep(1)
        seconds -= 1
        if seconds == 0: break

# TECHNICALS AND INDICATORS
def technicals(data, held):
    df = pd.DataFrame(data['results'])
    df['c'] = df['c'].astype(float)
    for i in range(len(df)):
        df.iloc[i,6] = int(np.int64(df.iloc[i,6]))
        date_time = datetime.datetime.fromtimestamp(df.iloc[i,6]/1000)
        pd.to_datetime(date_time)

    df['Resistance/Support'] = ''   # column 8
    for i in range(len(df)):
        if (
                df.iloc[i,3] >= df.iloc[i - 1,3]
                and df.iloc[i,3] >= df.iloc[i - 2,3]
                and df.iloc[i,3] >= df.iloc[i + 1,3]
                and (i < len(df)-2 and df.iloc[i,3] >= df.iloc[i + 2,3])
            ):
                df.iloc[i, 8] = "resistance"

    for i in range(len(df)):
        if (
                i >= 2 and i < len(df) - 2
                and df.iloc[i,3] <= df.iloc[i - 1,3]
                and df.iloc[i,3] <= df.iloc[i - 2,3]
                and df.iloc[i,3] <= df.iloc[i + 1,3]
                and df.iloc[i,3] <= df.iloc[i + 2,3]
            ):
                df.iloc[i, 8] = "support"

    df['Break'] = '' # column 9
    x = 0
    count = 0
    for i in range(len(df)):
        if df.iloc[i,8] == "resistance":
            count += 1
        if (
            df.iloc[i,8] == "resistance"
            and df.iloc[i,3] > df.iloc[x,3] 
            and count > 1
            ):
                df.iloc[i,9] = "break"
                x = i
    df.to_csv(r'C:\Users\johnm\OneDrive\Desktop\MyResume\df.csv')
    print('saved df in technicals')
    for i in range(len(df)):
        if df.iloc[i,8] == 'support' and held == False:
            strike_price = df.iloc[i,3]
            buy = True
            buy_time = df.iloc[i,6]
            buy_stock(TICKER, strike_price, buy_time, SHARES, current_time, df)
     
# BUY STOCK WHEN INDICATORS APPROVE
def buy_stock(TICKER, strike_price, buy_time, SHARES, current_time, df):
    total = strike_price*SHARES
    buy_data = {'Ticker': [TICKER],
                'Strike Price': [strike_price],
                'Buy Time': [buy_time],
                'Shares': [SHARES],
                'Buy Total': [total],
                'Sell Price': '',
                'Sell Time': '',
                'Total': '',
                'Net': '',
                'Current Time': ''}
    df_transactions = pd.DataFrame(buy_data)
    held = True
    print('finished buy')
    hold_stock(df_transactions, current_time, SHARES, strike_price, df, buy_time)

# HOLD STOCK AND RE-PULL API DATA.  SELL WHEN NEW INDICATORS APPROVE.
def hold_stock(df_transactions, current_time, SHARES, strike_price, df, buy_time):
    sell = False
    for i in range(len(df)):
        if df.iloc[i,8] == 'resistance' and df.iloc[i,9] == '' and buy_time < df.iloc[i,6]:
            sell_time = df.iloc[i,6]
            sell_price = df.iloc[i,3]
            sell = True
            buy = False
            x=0
            sell_stock(TICKER, df_transactions, SHARES, strike_price, x, sell_time, current_time, sell_price)
            x+=1
            print('returned from selling')
            current_time = datetime.datetime.now().time()
        elif current_time > datetime.time(15, 54) and current_time > datetime.time(9, 30) and sell == False:
            #data = get_ticker_data(TICKER, MULTIPLIER, TIMESPAN, DATESTART, DATEEND, APIKEY)
            #technicals(data)
            df.to_csv(r'C:\Users\johnm\OneDrive\Desktop\MyResume\df.csv')
            print('saved df in hold function')
            timer(5)
            print('finished timer')
            break
        else: # if end of day then sell
            sell_stock(TICKER, df_transactions, SHARES, strike_price, x, current_time, sell_time, sell_price)

# SELL STOCK           
def sell_stock(TICKER, df_transactions, SHARES, strike_price, x, sell_time, current_time, sell_price):
    df_transactions.iloc[x,5] = sell_price
    df_transactions.iloc[x,6] = sell_time
    df_transactions.iloc[x,7] = sell_price * SHARES
    df_transactions.iloc[x,8] = df_transactions.iloc[x,7] - df_transactions.iloc[x,4]
    df_transactions.iloc[x,9] = current_time
    held = False
    df_transactions.to_csv(r'C:\Users\johnm\OneDrive\Desktop\MyResume\transactions.csv', mode='a', header=False, index=False)

### PULL OR RE-PULL API DATA.  EXIT WHEN OUTSIDE OF MARKET OPEN TIME.
current_time = datetime.datetime.now().time()
print(current_time)
while current_time > datetime.time(15, 54) and current_time > datetime.time(9, 30):
    data = get_ticker_data(TICKER, MULTIPLIER, TIMESPAN, DATESTART, DATEEND, APIKEY)
    technicals(data, held)
    


# order placement, goal posts and transaction history

# notifications

# testing and alerts