# Alpha Vantage API

import requests
import csv
import pandas as pd

API_KEY = 'LNR6C1L773RCAOFY'

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

# dataframe the data and loop for each ticker and append to dataframe with close and total
data = {'Ticker':ticker_column[1:], 'Shares':shares_column[1:]}
df = pd.DataFrame(data)
x=0
for ticker in df['Ticker']:
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={ticker}&interval=5min&apikey={API_KEY}'
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

# Calculate total in each row and total portfolio

# Twilio info to text me daily updates

