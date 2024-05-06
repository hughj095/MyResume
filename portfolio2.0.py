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
SHARES = int(4)

def get_ticker_data(TICKER, MULTIPLIER, TIMESPAN, DATESTART, DATEEND, APIKEY):
    url = f'https://api.polygon.io/v2/aggs/ticker/{TICKER}/range/{MULTIPLIER}/{TIMESPAN}/{DATESTART}/{DATEEND}?apiKey={APIKEY}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print('Error:', response.status_code, response.content)
        return None

def buy_stock(TICKER, strike_price, buy_time, SHARES):
    buy_data = {'Ticker': [TICKER],
                'Strike Price': [strike_price],
                'Buy Time': [buy_time],
                'Shares': [SHARES],
                'Total': [strike_price*SHARES]}
    df_transactions = pd.DataFrame(buy_data)
    df_transactions.to_csv(r'C:\Users\johnm\OneDrive\Desktop\MyResume\transactions.csv', mode='a', header=False, index=False)

def sell_stock(TICKER, sell_price, sell_time, SHARES):

### API pull data

data = get_ticker_data(TICKER, MULTIPLIER, TIMESPAN, DATESTART, DATEEND, APIKEY)

'''url = f'https://api.polygon.io/v2/aggs/ticker/{TICKER}/range/{MULTIPLIER}/{TIMESPAN}/{DATESTART}/{DATEEND}?apiKey={APIKEY}'
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    #pprint.pprint(data)
else:
    print('Error:', response.status_code, response.content)'''

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
        buy_stock(TICKER, strike_price, buy_time, SHARES)

sell = False
while buy == True:
    # start timer to match multiplier and interval
    # if nearing timer then:
        # run API and
        for i in range(len(df)):
            if df.iloc[i,8] == 'resistance' and df.iloc[i,9] == '' and buy_time < df.iloc[i,6]:
                sell = True
                sell_price = df.iloc[i,3]
                sell_time = df.iloc[i,6]
                buy = False
                sell_stock(TICKER, sell_stock, sell_time, SHARES)
        break




    






# notifications
df.to_csv(r'C:\Users\johnm\OneDrive\Desktop\MyResume\df.csv')
# testing and alerts