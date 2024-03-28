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

# convert strings to numeric
df['4. close'] = pd.to_numeric(df['4. close'])
df['1. open'] = pd.to_numeric(df['1. open'])
df['2. high'] = pd.to_numeric(df['2. high'])
df['3. low'] = pd.to_numeric(df['3. low'])
df['5. volume'] = pd.to_numeric(df['5. volume'])

# mark stock as in bull territory if current price is daily high
marker = []
max_close = max(df['4. close'])
for close in reversed(df['4. close']):
    if close == max_close:
        marker.insert(0, 'bull')
    else:
        marker.insert(0, 0)
df['Marker'] = marker

# mark a stock as having resistance at the peak of a candle's close among four others
df['Resistance'] = ''
df['new_index'] = range(len(df))
for i in df['new_index']:
    if (
            df.iloc[i,4] >= df.iloc[i - 1,4]
            and df.iloc[i,4] >= df.iloc[i - 2,4]
            and df.iloc[i,4] >= df.iloc[i + 1,4]
            and (i < len(df)-2 and df.iloc[i,4] >= df.iloc[i + 2,4])
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
df['Shrink C Long W bear'] = ''
slope = calculate_slope_and_intercept(df.iloc[i, 8], df.iloc[i, 3], df.iloc[i-1, 8], df.iloc[i-1, 3]) #deleted [0]
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
            # add reversal trade in uptrend where previously was a resistance in last 30 mins (short stock)
            and any(x == 'resistance' for x in df.loc[i:i+6, 'Resistance'])
        ):
            df.iloc[i, 12] = "shrinking candle, long wick, reversal bear"

# Shrinking candle, long wick, bull
df['Shrink C Long W bull'] = ''
slope = calculate_slope_and_intercept(df.iloc[i, 8], df.iloc[i, 3], df.iloc[i-1, 8], df.iloc[i-1, 3]) #deleted [0]
for i in df['new_index']: 
    if (
            i >= 2 
            and i < len(df) - 2
            and (df.iloc[i,0] - df.iloc[i,3] < df.iloc[i-1,0] - df.iloc[i - 1,3])
            and (df.iloc[i-1,0] - df.iloc[i-1,3] < df.iloc[i-2,0] - df.iloc[i-2,3])
            # long wick is low minus (open minus close) is greater than open minus close
            and df.iloc[i,0] > df.iloc[i,3] 
            and df.iloc[i,3] - df.iloc[i,2] > df.iloc[i,0] - df.iloc[i,3]
            and df.iloc[i-1,3] - df.iloc[i-1,2] > df.iloc[i-1,0] - df.iloc[i-1,3]
            # add reversal trade in downtrend where previously was support in last 30 mins (buy stock)
            # and any(x == 'support' for x in df.loc[i:i+6, 'Support'])
        ):      
            df.iloc[i, 13] = "shrinking candle, long wick, reversal bull"

# look at other candlestick indicators
            
# Double bottom momentum: two close prices in a span of twelve are the lowest of twelve AND are similar in price AND flank both 
# sides of the high price of twelve, showing support
df['Double Bottom'] = ''
for i in range(len(df)):
    if i < len(df) - 11:
        window = df['4. close'].iloc[i:i + 12]  # Get the window of 12 values including the current cell
        min_values_indices = window.nsmallest(2).index  # Get indices of two minimum values within the window
        min_value_1, min_value_2 = window[min_values_indices]  # Get the values of the two minimums
        if (
            df.iloc[i,3] == min_value_1 or df.iloc[i,3] == min_value_2
            and df.iloc[i-1,3] > df.iloc[i,3]
        ):
            df.iloc[i, 14] = "double bottom"

# Slope and intercept of a support level
for i in range(1, len(df['new_index'])):
     if df.iloc[i,11] == 'support':
          for x in range(i+1, len(df['Support'])):
               if df.iloc[x,11] == 'support':
                    slope, intercept = calculate_slope_and_intercept(df.iloc[i,8],i,df.iloc[x,8],x)
                    df.iloc[i,9] = slope
                    df.iloc[i,10] = intercept        

# volume indicator
df['volume_indicator'] = ''
for i in range(len(df)):
    if i < 6 or i > len(df) - 7:
        continue  # If the index is too close to the beginning or end, skip
    current_value = df.at[df.index[i], '5. volume']
    surrounding_values = df.iloc[i-6:i+7]['5. volume']  # 6 before and 6 after (total 12)
    if current_value == surrounding_values.max():
        df.at[df.index[i], 'volume_indicator'] = 'high volume'
            
# incorporate fibonaci levels at lows and highs
#   find the low and high of a 4 hour period, and mark the fib levels within that period, if fib levels are a 
#   local low or high, mark as a fib level           


# could incorporate 50 DMA, but need another API pull


# define when is a buy opportunity
            



# build a bank file of buy stocks, prices, shares, times, target and sell prices, executions, and bankroll
        


df.to_csv(r'C:\Users\johnm\OneDrive\Desktop\MyResume\df.csv', index=True)
