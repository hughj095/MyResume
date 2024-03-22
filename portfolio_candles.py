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

def calculate_slope_and_intercept(x1, y1, x2, y2):
    # Calculate slope
    x1_minutes = x1.hour * 60 + x1.minute
    x2_minutes = x2.hour * 60 + x2.minute
    slope = (y2 - y1) / (x2_minutes - x1_minutes)
    
    # Calculate y-intercept
    intercept = y1 - slope * x1_minutes
    
    return slope, intercept


ticker = 'DG'
url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={ticker}&interval=5min&apikey={AV_API_KEY}'
r = requests.get(url)
data = r.json()
df = pd.DataFrame(data['Time Series (5min)']).T

#print(df)
df['4. close'] = pd.to_numeric(df['4. close'])
marker = []
for close in df['4. close']:
    if close > 155:
        marker.append('bull')
    else: marker.append(0)
df['Marker'] = marker

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

df['Time'] = ''
for i in df.index:
    date_string = i
    date_format = "%Y-%m-%d %H:%M:%S"
    date_time_obj = datetime.strptime(date_string, date_format)
    time_value = date_time_obj.time()
    df.loc[i,'Time'] = time_value
     
df['Resistance Trend'] = ''
for i in range(1, len(df['Resistance'])):
     if df.iloc[i,6] == 'resistance':
          for x in range(i+1, len(df['Resistance'])):
               if df.iloc[x,6] == 'resistance':
                    slope, intercept = calculate_slope_and_intercept(df.iloc[i,8],i,df.iloc[x,8],x)
                    df.loc[i,"Resistance Trend"] = (slope, intercept)                    


df.to_csv(r'C:\Users\johnm\OneDrive\Desktop\MyResume\df.csv', index=True)
