# This program pulls stock data specified in stocks.csv using the Alpha Vantage API.  It then summarizes
#   your full portfolio value in a dataframe and sends a daily text message with the total using the 
#   Twilio API.

import requests
import csv
import pandas as pd
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

AV_API_KEY = 'LNR6C1L773RCAOFY'
TWILIO_ACCOUNT_SID = 'account sid here'
TWILIO_AUTH_TOKEN = 'token here'
account_sid = TWILIO_ACCOUNT_SID
auth_token = TWILIO_AUTH_TOKEN
proxy_client = TwilioHttpClient()   
client = Client(account_sid, auth_token, http_client=proxy_client) # may not need http_client tag

url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={ticker}&interval=5min&apikey={AV_API_KEY}'
r = requests.get(url)
data = r.json()
df = pd.DataFrame(data['Time Series (5min)'])

print(df)


