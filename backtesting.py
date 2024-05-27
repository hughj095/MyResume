# Imports and Custom Classes
from timer import Timer # timer.py in folder
from PreviousWeekday import PreviousWeekday # PreviousWeekday.py in folder
import requests
import pandas as pd

# Variables
TIMER_INTERVAL = 1
MULTIPLIER = '1'
TIMESPAN = 'minute'
APIKEY = 'hldKpOcQ9ago1ZA83XRyRQ1tFG5uokBa' #Polygon API key
SHARES = 4
DATESTART = str(PreviousWeekday().get_yesterday())
DATEEND = DATESTART

# Timer
# Timer().timer(TIMER_INTERVAL)

# Get Historical Day Prices for df
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
# Blank df to append minute by minute
df_ticker = pd.read_csv(r'C:\Users\johnm\OneDrive\Desktop\MyResume\stocks.csv')
for TICKER in df_ticker['stocks']:
    get_ticker_data(MULTIPLIER, TIMESPAN, DATESTART, DATEEND, APIKEY)
    df_hist = pd.DataFrame(data['results'])
    df_hist = df_hist.iloc[0]  #### take first index 0 but maintain number format
    df_hist['Ticker'] = TICKER
    df_hist = df_hist[['Ticker', 'v', 'vw', 'o', 'c', 'h', 'l', 't', 'n']]
    continue
# Take first minute
Timer.timer(TIMER_INTERVAL)
# Add next minute to df

# Add third minute

# Technicals function

# Buy

# Hold

# Sell

# Record 
    # Cumulative transactions and sum of net profits


