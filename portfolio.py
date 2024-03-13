# This program pulls stock data specified in stocks.csv using the Alpha Vantage API.  It then summarizes
#   your full portfolio value in a dataframe and sends a daily text message with the total using the 
#   Twilio API.

import requests
import csv
import pandas as pd
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient
import requests

AV_API_KEY = 'LNR6C1L773RCAOFY'
TWILIO_ACCOUNT_SID = 'account sid here'
TWILIO_AUTH_TOKEN = 'token here'
account_sid = TWILIO_ACCOUNT_SID
auth_token = TWILIO_AUTH_TOKEN
proxy_client = TwilioHttpClient()   
client = Client(account_sid, auth_token, http_client=proxy_client)

# Create empty list of csv columns
ticker_column = []
shares_column = []

# Open csv, find the last row, and append values to empty lists
with open('stocks.csv', mode='r') as file:
    reader = csv.reader(file)
    last_used_row = None
    for row in reversed(list(reader)):
        if row[0] != "":
            last_used_row = row
            break
    file.seek(0)
    for row in reader:
        if row[0] != "":
            ticker_column.append(row[0])
            shares_column.append(row[1])

# dataframe the data and loop through each ticker and append to dataframe with closing price
data = {'Ticker':ticker_column[1:], 'Shares':shares_column[1:]}
df = pd.DataFrame(data)
x=0
for ticker in df['Ticker']:
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={ticker}&interval=5min&apikey={AV_API_KEY}'
    r = requests.get(url)
    data = r.json()
    print(data)
    time = data['Time Series (5min)']
    for timestamp, values in time.items():
        if '4. close' in values:
            close = values['4. close']
            break
    df.iloc[x, 2] = close
    x += 1

# Check final df
print(df)

# Calculate total stock value in each row and total portfolio value
stock_value = []
for index in df.iterrows():
    value = row['Shares'] * row['Close']
    stock_value.append(value)
df['Total'] = stock_value
total = df['Total'].sum()
df.loc[len(df)] = total

# Check final df
print(df)

# Twilio info to text me daily updates (using Windows Scheduler for a 4pm Eastern program run and text)
message = client.messages.create(
    body= f"Portfolio total after close today is ${total}",
    from_='+18334029267',
    to='+18453723892'
)
message.sid
