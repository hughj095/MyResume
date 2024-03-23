# This program pulls stock data specified in stocks.csv using the Alpha Vantage API.  It then summarizes
#   your full portfolio value in a dataframe and sends a daily text message with the total using the 
#   Twilio API.

import requests
import csv
import pandas as pd
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient
from datetime import datetime

AV_API_KEY = 'LNR6C1L773RCAOFY'
TWILIO_ACCOUNT_SID = 'account sid here'
TWILIO_AUTH_TOKEN = 'token here'
account_sid = TWILIO_ACCOUNT_SID
auth_token = TWILIO_AUTH_TOKEN
proxy_client = TwilioHttpClient()   
client = Client(account_sid, auth_token, http_client=proxy_client) # may not need http_client tag

# function to find slope and intercept of a trend
def calculate_slope_and_intercept(x1, y1, x2, y2):
    # Calculate slope
    x1_minutes = x1.hour * 60 + x1.minute
    x2_minutes = x2.hour * 60 + x2.minute
    slope = (y2 - y1) / (x2_minutes - x1_minutes)
    
    # Calculate y-intercept
    intercept = y1 - slope * x1_minutes
    
    return slope, intercept

# temporarily looking at one stock to test program
ticker = 'DG'
url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={ticker}&interval=5min&apikey={AV_API_KEY}'
r = requests.get(url)
data = r.json()
df = pd.DataFrame(data['Time Series (5min)']).T

# mark stock as in bull territory above a certain price
df['4. close'] = pd.to_numeric(df['4. close'])
df['1. open'] = pd.to_numeric(df['1. open'])
df['2. high'] = pd.to_numeric(df['2. high'])
df['3. low'] = pd.to_numeric(df['3. low'])
marker = []
for close in df['4. close']:
    if close > 155:
        marker.append('bull')
    else: marker.append(0)
df['Marker'] = marker

# mark a stock as having resistance at the peak of a candle's close among four others
df['Resistance'] = ''
df['new_index'] = range(len(df))
for i in df['new_index']:
    if (
            df.iloc[i,4] >= df.iloc[i - 1,4]
            and df.iloc[i,4] >= df.iloc[i - 2,4]
            and df.iloc[i,4] >= df.iloc[i + 1,4]
            and df.iloc[i,4] >= df.iloc[i + 2,4]
        ):
            df.iloc[i, 6] = "resistance"

# convert string time to time time
df['Time'] = ''
for i in df.index:
    date_string = i
    date_format = "%Y-%m-%d %H:%M:%S"
    date_time_obj = datetime.strptime(date_string, date_format)
    time_value = date_time_obj.time()
    df.loc[i,'Time'] = time_value

# mark the slope and intercept of a trendline with resistance at two peaks
df['Slope'] = ''
df['Intercept'] = ''
for i in range(1, len(df['new_index'])):
     if df.iloc[i,6] == 'resistance':
          for x in range(i+1, len(df['Resistance'])):
               if df.iloc[x,6] == 'resistance':
                    slope, intercept = calculate_slope_and_intercept(df.iloc[i,8],i,df.iloc[x,8],x)
                    df.iloc[i,9] = slope
                    df.iloc[i,10] = intercept             

# find support levels using candlesticks
df['Support'] = ''
for i in df['new_index']:
    if (
            i >= 2 and i < len(df) - 2
            and df.iloc[i,4] <= df.iloc[i - 1,4]
            and df.iloc[i,4] <= df.iloc[i - 2,4]
            and df.iloc[i,4] <= df.iloc[i + 1,4]
            and df.iloc[i,4] <= df.iloc[i + 2,4]
        ):
            df.iloc[i, 11] = "support"

# redefine resistance and support using high and low candlesticks
    # shrinking candles and long wicks (bear)
df['Shrink C Long W'] = ''
slope = calculate_slope_and_intercept(df.iloc[i, 8], df.iloc[i, 3], df.iloc[i-1, 8], df.iloc[i-1, 3])[0]
for i in df['new_index']: 
    if (
            i >= 2 
            and i < len(df) - 2
            and (df.iloc[i,3] - df.iloc[i,0] < df.iloc[i-1,3] - df.iloc[i - 1,0])
            and (df.iloc[i-1,3] - df.iloc[i-1,0] < df.iloc[i-2,3] - df.iloc[i-2,0])
            # long wick is high minus abs of close minus open is greater than 2x abs of close minus open
            and df.iloc[i,3] > df.iloc[i,1] 
            and df.iloc[i,1] - df.iloc[i,3] > df.iloc[i,3] - df.iloc[i,0]
            and df.iloc[i-1,1] - df.iloc[i-1,3] > df.iloc[i-1,3] - df.iloc[i-1,0]
            # add reversal trade in uptrend where red candle closes below Slope line (short stock)
            and (df.iloc[i+2,3] < slope or df.iloc[i+2,3] < slope)
        ):
            df.iloc[i, 12] = "shrinking candle, long wick, reversal"

# look at other candlestick indicators
            
# incorporate fibonaci levels at lows and highs
            
# define when is a buy opportunity
            




df.to_csv(r'C:\Users\johnm\OneDrive\Desktop\MyResume\df.csv', index=True)
