### imports, variables and functions
import datetime
import requests
import pandas as pd
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
IB_USER = 'algodaddy08'
IB_PASS = 'xLsW_EyDgxDL8gD'

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
df_dailyhistory = pd.read_csv(r'C:\Users\johnm\OneDrive\Desktop\MyResume\portfolio_dailyhistory.csv')
budget = df_dailyhistory.iloc[len(df_dailyhistory)-1,1] # yesterday's ending balance
buy_time = ''

# API DATA PULL
def get_ticker_data(MULTIPLIER, TIMESPAN, DATESTART, DATEEND, APIKEY):
    global TICKER, data, strike_price
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
    global x, held, df, buy_time, stop_loss, strike_price
    df = pd.DataFrame(data['results'])
    df['c'] = df['c'].astype(float)
    for i in range(len(df)):  ##### DOESNT WORK, TRY CHANGING ENTIRE COLUMN TO DATETIME
        df.iloc[i,6] = int(np.int64(df.iloc[i,6]))
        date_time = datetime.datetime.fromtimestamp(df.iloc[i,6]/1000)
        pd.to_datetime(date_time)

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
    elif df.iloc[len(df)-5,8] == 'support' and held == False:
        strike_price = df.iloc[len(df)-3,3]
        buy = True
        buy_time = df.iloc[len(df)-3,6] 
        buy_stock()
    else:
        pass
     
# BUY STOCK WHEN INDICATORS APPROVE
def buy_stock():
    global x, TICKER, SHARES, current_time, df, buy_time, budget, df_budget, held, stop_loss, strike_price
    df_transactions = pd.read_csv(r'C:\Users\johnm\OneDrive\Desktop\MyResume\transactions.csv') #### NEED SOMETHING TO DETERMINE IF DF_TRANSACTIONS SHOULD READ FROM SAVED OR SHOULD BE BLANK AT BEGINNING OF DAY
    total = strike_price*SHARES
    if total > budget:
        print('out of money')
        ###### BREAK OUT OF A FUNCTION HERE AND GO BACK TO START
    x = len(df_transactions)
    df_transactions.loc[x, 'Ticker'] = TICKER
    df_transactions.loc[x, 'Strike Price'] = strike_price
    df_transactions.loc[x, 'Stop Loss'] = 0.99 * strike_price
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
    global x, df_transactions, current_time, SHARES, strike_price, df, buy_time, held, stop_loss, sell_price, sell_time
    sell = False
    df_transactions = pd.read_csv(r'C:\Users\johnm\OneDrive\Desktop\MyResume\transactions.csv')
    if df.iloc[1,8] == 'resistance' and df.iloc[1,9] == '' and buy_time < df.iloc[1,6]:  ### BUY TIME MAY NOT BE NECESSARY
        sell_time = df.iloc[1,6]
        sell_price = df.iloc[1,3]
        sell = True
        buy = False
        sell_stock()
        current_time = datetime.datetime.now().time()
    elif df.iloc[1,3] < 0.99 * df_transactions.iloc[1,1]:
        print('stop loss')
        stop_loss = True
        sell_stock()
    elif current_time < datetime.time(15, 54) and current_time > datetime.time(9, 30) and sell == False:
        data = get_ticker_data(TICKER, MULTIPLIER, TIMESPAN, DATESTART, DATEEND, APIKEY)
        df.to_csv(r'C:\Users\johnm\OneDrive\Desktop\MyResume\df.csv', index = False)
        pass
    else: # if end of day then sell
        sell_time = df.iloc[1,6]
        sell_price = df.iloc[1,3]
        sell_stock()

# SELL STOCK           
def sell_stock():
    global x, TICKER, df_transactions, SHARES, strike_price, sell_time, current_time, sell_price, held, df_budget, budget, stop_loss
    print('start of sell function')
    ### ADD TRANSACTION_ID HERE
    df_transactions.iloc[x,5] = sell_price
    df_transactions.iloc[x,6] = sell_time
    df_transactions.iloc[x,7] = sell_price * SHARES
    df_transactions.iloc[x,8] = df_transactions.iloc[x,7] - df_transactions.iloc[x,4]
    df_transactions.iloc[x,9] = current_time
    if sell_price < 0.99 * strike_price:
        df_transactions.iloc[x,10] = 'stop loss'
        stop_loss = True
    print(f'sold {TICKER}') 
    held = False
    df_transactions.to_csv(r'C:\Users\johnm\OneDrive\Desktop\MyResume\transactions.csv', mode='a', header=False, index=False)
    budget = budget + sell_price * SHARES
    df_budget.iloc[0,0] = budget
    df_budget.to_csv(r'C:\Users\johnm\OneDrive\Desktop\MyResume\portfolio_budget.csv', index=False)

### PULL OR RE-PULL API DATA.  EXIT WHEN OUTSIDE OF MARKET OPEN TIME.
def scan():
    global x, held, TICKER, budget, df_budget, data, df, df_transactions, stop_loss
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
            break
    print(f'balance ${budget}')
    timer(1)
    # delete after go live with IB
    if len(df_transactions) > 0:
        # start on 2nd df to ask if stock should sell
        df.reset_index(drop=True, inplace=True)
        if df.iloc[1,8] == 'resistance' and df.iloc[1,9] == '':
            sell_stock()
        else:
            hold_stock()


current_time = datetime.datetime.now().time()
print(current_time)
while current_time < datetime.time(15, 54) and current_time > datetime.time(9, 30):  
    scan()
    current_time = datetime.datetime.now().time()
    print(current_time)

print('out of time')

# Daily Balance Summary
if current_time > datetime.time(16,00):
    df_dailyhistory = pd.read_csv(r'C:\Users\johnm\OneDrive\Desktop\MyResume\portfolio_dailyhistory.csv')
    if df_dailyhistory.iloc[len(df_dailyhistory)-1,0] != datetime.date.today().strftime('%Y-%m-%d'):
        df_dailyhistory.loc[len(df_dailyhistory),0] = [datetime.date.today(), None]
        df_dailyhistory.iloc[len(df_dailyhistory)-1,1] = budget
        df_dailyhistory.to_csv(r'C:\Users\johnm\OneDrive\Desktop\MyResume\portfolio_dailyhistory.csv', index=False)
    # notifications
    message = client.messages.create(
        body= f"Portfolio total after close today is ${budget}",
        from_='+18334029267',
        to='+18453723892'
        )
    message.sid