### imports, variables and functions
import requests
import pandas as pd
import datetime
import numpy as np

TICKER = 'AAPL'
MULTIPLIER = '5'
TIMESPAN = 'minute'
DATESTART = '2024-05-03'
DATEEND = '2024-05-03'
APIKEY = 'hldKpOcQ9ago1ZA83XRyRQ1tFG5uokBa'
SHARES = 4

current_time = datetime.datetime.now().time()

def get_ticker_data(TICKER, MULTIPLIER, TIMESPAN, DATESTART, DATEEND, APIKEY):
    url = f'https://api.polygon.io/v2/aggs/ticker/{TICKER}/range/{MULTIPLIER}/{TIMESPAN}/{DATESTART}/{DATEEND}?apiKey={APIKEY}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print('Error:', response.status_code, response.content)
        return None

##### BUY FUNCTION WANTS TO START OVER AGAIN BUT NEEDS TO APPEND TO THE LAST TRANSACTION
##### check the HOLD FUNCTION TO BREAK OUT OF THE WHILE LOOP

def buy_stock(TICKER, strike_price, buy_time, SHARES, current_time):
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
    hold_stock(df_transactions, buy, current_time, SHARES, strike_price)

def hold_stock(df_transactions, buy, current_time, SHARES, strike_price):
    sell = False
    while buy == True:
        # start timer to match multiplier and interval
        current_time = datetime.datetime.now().time()
        # if nearing timer then:
            # run API and
        x=0
        for i in range(len(df)):
            if df.iloc[i,8] == 'resistance' and df.iloc[i,9] == '' and buy_time < df.iloc[i,6]:
                sell_time = df.iloc[i,6]
                sell_price = df.iloc[i,3]
                sell_stock(df_transactions, sell_time, sell_price, SHARES, current_time, strike_price, x)
                x+=1
                sell = True
                buy = False
        current_time = datetime.datetime.now().time()
        if current_time > datetime.time(15, 54):
                sell_stock(TICKER, df_transactions, SHARES, strike_price, sell_time=sell_time,  current_time=current_time, sell_price=df.iloc[i,3])
            
def sell_stock(df_transactions, sell_time, sell_price, SHARES, current_time, strike_price, x):
    df_transactions.iloc[x,5] = sell_price
    df_transactions.iloc[x,6] = sell_time
    df_transactions.iloc[x,7] = sell_price * SHARES
    df_transactions.iloc[x,8] = df_transactions.iloc[x,7] - df_transactions.iloc[x,4]
    df_transactions.iloc[x,9] = current_time
    df_transactions.to_csv(r'C:\Users\johnm\OneDrive\Desktop\MyResume\transactions.csv', mode='a', header=False, index=False)

### API pull data

data = get_ticker_data(TICKER, MULTIPLIER, TIMESPAN, DATESTART, DATEEND, APIKEY)

### indicators and management

# data pre-processing
df = pd.DataFrame(data['results'])
df['c'] = df['c'].astype(float)
for i in range(len(df)):
    df.iloc[i,6] = int(np.int64(df.iloc[i,6]))
    date_time = datetime.datetime.fromtimestamp(df.iloc[i,6]/1000)
    pd.to_datetime(date_time)

# Resistance marker at close
df['Resistance/Support'] = ''   # column 8
for i in range(len(df)):
    if (
            df.iloc[i,3] >= df.iloc[i - 1,3]
            and df.iloc[i,3] >= df.iloc[i - 2,3]
            and df.iloc[i,3] >= df.iloc[i + 1,3]
            and (i < len(df)-2 and df.iloc[i,3] >= df.iloc[i + 2,3])
        ):
            df.iloc[i, 8] = "resistance"

# Support marker at close
for i in range(len(df)):
    if (
            i >= 2 and i < len(df) - 2
            and df.iloc[i,3] <= df.iloc[i - 1,3]
            and df.iloc[i,3] <= df.iloc[i - 2,3]
            and df.iloc[i,3] <= df.iloc[i + 1,3]
            and df.iloc[i,3] <= df.iloc[i + 2,3]
        ):
            df.iloc[i, 8] = "support"

# Did latest resistance break above previous resistance level?
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

# order placement, goal posts and transaction history

# if support then buy, while buy, if resistance + break then hold, if resistance then sell, if support then hold
for i in range(len(df)):
    if df.iloc[i,8] == 'support':
        strike_price = df.iloc[i,3]
        buy = True
        buy_time = df.iloc[i,6]
        buy_stock(TICKER, strike_price, buy_time, SHARES, current_time)






    






# notifications
df.to_csv(r'C:\Users\johnm\OneDrive\Desktop\MyResume\df.csv')
# testing and alerts