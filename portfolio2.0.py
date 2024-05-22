### imports, variables and functions
import requests
import pandas as pd
import datetime
import time
import numpy as np
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient
from PreviousWeekday import PreviousWeekday  # custom Class in folder


MULTIPLIER = '1'
TIMESPAN = 'minute'
APIKEY = 'hldKpOcQ9ago1ZA83XRyRQ1tFG5uokBa'
SHARES = 4
DATESTART = str(PreviousWeekday().get_yesterday())
DATEEND = DATESTART

TWILIO_ACCOUNT_SID = 'account sid here'
TWILIO_AUTH_TOKEN = 'token here'
account_sid = TWILIO_ACCOUNT_SID
auth_token = TWILIO_AUTH_TOKEN
proxy_client = TwilioHttpClient()   
client = Client(account_sid, auth_token, http_client=proxy_client) # may not need http_client tag

buy_data = {'Ticker': '',
            'Strike Price': '',
            'Buy Time': '',
            'Shares': '',
            'Buy Total': '',
            'Sell Price': '',
            'Sell Time': '',
            'Total': '',
            'Net': '',
            'Current Time': '',
            'Stop Loss': ''}
df_transactions = pd.DataFrame(buy_data, index=[0])
df_transactions.to_csv(r'C:\Users\johnm\OneDrive\Desktop\MyResume\transactions.csv', index=False)

held = False
buy_time = ''

# API DATA PULL
def get_ticker_data(MULTIPLIER, TIMESPAN, DATESTART, DATEEND, APIKEY):
    global TICKER, data
    url = f'https://api.polygon.io/v2/aggs/ticker/{TICKER}/range/{MULTIPLIER}/{TIMESPAN}/{DATESTART}/{DATEEND}?apiKey={APIKEY}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print('pulled API')
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
def technicals(data):
    global x, held, df, buy_time
    df = pd.DataFrame(data['results'])
    df['c'] = df['c'].astype(float)
    for i in range(len(df)):  ##### DOESNT WORK, TRY CHANGING ENTIRE COLUMN TO DATETIME
        df.iloc[i,6] = int(np.int64(df.iloc[i,6]))
        date_time = datetime.datetime.fromtimestamp(df.iloc[i,6]/1000)
        df.iloc[i,6] = pd.to_datetime(date_time)

    df['Resistance/Support'] = ''   # column 8
    for i in range(len(df)-1):
        if (
                df.iloc[i,3] >= df.iloc[i - 1,3]
                and df.iloc[i,3] >= df.iloc[i - 2,3]
                and df.iloc[i,3] >= df.iloc[i + 1,3]
                and (i < len(df)-2 and df.iloc[i,3] >= df.iloc[i + 2,3])
            ):
                df.iloc[i, 8] = "resistance"

    for i in range(len(df)-1):   #### MAY NEED TO INDENT AGAIN
        if (
                i >= 2 and i < len(df) - 2
                and df.iloc[i,3] <= df.iloc[i - 1,3]
                and df.iloc[i,3] <= df.iloc[i - 2,3]
                and df.iloc[i,3] <= df.iloc[i + 1,3]
                and df.iloc[i,3] <= df.iloc[i + 2,3]
            ):
                df.iloc[i, 8] = "support"

    df['Break'] = '' # column 9
    count = 0
    for i in range(len(df)-1):
        if df.iloc[i,8] == "resistance":
            count += 1
        for j in range(i-10,i-1):   ##### 10 minutes back from current i to look for breakthroughs
            if (
                df.iloc[i,8] == 'resistance'
                and df.iloc[j,8] == 'resistance'
                and df.iloc[j,9] == ''
                and df.iloc[i,3] > df.iloc[j,3] 
                and count > 1
                ):
                    df.iloc[i,9] = "break"
    df.to_csv(r'C:\Users\johnm\OneDrive\Desktop\MyResume\df.csv', index=False)      
    print('saved df in technicals')
    df = df[len(df)-5:len(df)]
    if held == True:
        hold_stock()
    elif df.iloc[len(df)-3,8] == 'support' and held == False:
        strike_price = df.iloc[len(df)-3,3]
        buy = True
        buy_time = df.iloc[len(df)-3,6] 
        buy_stock(strike_price)
    else:
        pass
     
# BUY STOCK WHEN INDICATORS APPROVE
def buy_stock(strike_price):
    global x, TICKER, SHARES, current_time, df, buy_time, budget, df_budget
    df_transactions = pd.read_csv(r'C:\Users\johnm\OneDrive\Desktop\MyResume\transactions.csv') #### NEED SOMETHING TO DETERMINE IF DF_TRANSACTIONS SHOULD READ FROM SAVED OR SHOULD BE BLANK AT BEGINNING OF DAY
    total = strike_price*SHARES
    if total > budget:
        print('out of money')
        ###### BREAK OUT OF A FUNCTION HERE AND GO BACK TO START
    x = len(df_transactions)
    df_transactions.loc[x, 'Ticker'] = TICKER
    df_transactions.loc[x, 'Strike Price'] = strike_price
    df_transactions.loc[x, 'Buy Time'] = buy_time
    df_transactions.loc[x, 'Shares'] = SHARES
    df_transactions.loc[x, 'Buy Total'] = total
    held = True
    df_transactions.to_csv(r'C:\Users\johnm\OneDrive\Desktop\MyResume\transactions.csv', index=False)
    df_budget.iloc[0,0] = df_budget.iloc[0,0].astype(float) - total
    budget = df_budget.iloc[0,0]
    df_budget.to_csv(r'C:\Users\johnm\OneDrive\Desktop\MyResume\portfolio_budget.csv', index=False)
    print('finished buy')
    print(f'balance ${budget}')

# HOLD STOCK AND RE-PULL API DATA.  SELL WHEN NEW INDICATORS APPROVE.
def hold_stock():
    global x, df_transactions, current_time, SHARES, strike_price, df, buy_time, held, stop_loss
    sell = False
    for i in range(len(df)):  #### ONLY NEED TO LOOK AT THE THIRD ROW IN THE DATAFRAME
        if df.iloc[i,8] == 'resistance' and df.iloc[i,9] == '' and buy_time < df.iloc[i,6]:  ### BUY TIME MAY NOT BE NECESSARY
            sell_time = df.iloc[i,6]
            sell_price = df.iloc[i,3]
            sell = True
            buy = False
            sell_stock()
            current_time = datetime.datetime.now().time()
        elif df.iloc[i,3] < 0.99 * strike_price:
            print('stop loss')
            stop_loss = True
            sell_stock()
        elif current_time < datetime.time(15, 54) and current_time > datetime.time(9, 30) and sell == False:
            data = get_ticker_data(TICKER, MULTIPLIER, TIMESPAN, DATESTART, DATEEND, APIKEY)
            technicals(data)
            df.to_csv(r'C:\Users\johnm\OneDrive\Desktop\MyResume\df.csv', index = False)
        else: # if end of day then sell
            sell_time = df.iloc[i,6]
            sell_price = df.iloc[i,3]
            sell_stock()

# SELL STOCK           
def sell_stock():
    global x, TICKER, df_transactions, SHARES, strike_price, sell_time, current_time, sell_price, held, df_budget, budget, stop_loss
    print('start of sell function')
    df_transactions.iloc[x,5] = sell_price
    df_transactions.iloc[x,6] = sell_time
    df_transactions.iloc[x,7] = sell_price * SHARES
    df_transactions.iloc[x,8] = df_transactions.iloc[x,7] - df_transactions.iloc[x,4]
    df_transactions.iloc[x,9] = current_time
    if stop_loss == True:
        df_transactions.iloc[x,10] = 'stop loss'
    print(f'sold {TICKER}')
    held = False
    df_transactions.to_csv(r'C:\Users\johnm\OneDrive\Desktop\MyResume\transactions.csv', mode='a', header=False, index=False)
    budget = budget + sell_price * SHARES
    df_budget.iloc[0,0] = budget
    df_budget.to_csv(r'C:\Users\johnm\OneDrive\Desktop\MyResume\portfolio_budget.csv', index=False)

### PULL OR RE-PULL API DATA.  EXIT WHEN OUTSIDE OF MARKET OPEN TIME.
def scan():
    global x, held, TICKER, budget, df_budget, data
    #data = pd.read_csv(r'C:\Users\johnm\OneDrive\Desktop\MyResume\df.csv')
    df_stocks = pd.read_csv(r'C:\Users\johnm\OneDrive\Desktop\MyResume\stocks.csv')
    df_budget = pd.read_csv(r'C:\Users\johnm\OneDrive\Desktop\MyResume\portfolio_budget.csv')
    budget = df_budget.iloc[0,0]
    for stock in df_stocks['stocks']:
        TICKER = stock
        print(TICKER)
        get_ticker_data(MULTIPLIER, TIMESPAN, DATESTART, DATEEND, APIKEY)
        print('starting technicals')
        technicals(data)
    if held == True:
        # start on 2nd df to ask if stock should sell
        pass
    print(f'balance ${budget}')
    timer(1)


current_time = datetime.datetime.now().time()
print(current_time)
while current_time > datetime.time(15, 54) and current_time > datetime.time(9, 30):  
    scan()

print('out of time')

# Daily Balance Summary
if current_time > datetime.time(16,00):
    df_dailyhistory = pd.read_csv(r'C:\Users\johnm\OneDrive\Desktop\MyResume\portfolio_dailyhistory.csv')
    if df_dailyhistory[len(df_dailyhistory),0] == datetime.date.today():
    # notifications
        message = client.messages.create(
            body= f"Portfolio total after close today is ${budget}",
            from_='+18334029267',
            to='+18453723892'
            )
        message.sid

# testing and alerts