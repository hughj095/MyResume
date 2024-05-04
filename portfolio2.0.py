# imports and variables
import requests

TICKER = 'AAPL'
MULTIPLIER = '1'
TIMESPAN = 'day'
DATESTART = '2024-05-02'
DATEEND = '2024-05-02'
APIKEY = 'hldKpOcQ9ago1ZA83XRyRQ1tFG5uokBa'

url = f'https://api.polygon.io/v2/aggs/ticker/{TICKER}/range/{MULTIPLIER}/{TIMESPAN}/{DATESTART}/{DATEEND}?apiKey={APIKEY}'

# get all stock info
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print('Error:', response.status_code)

# API pull data

# indicators and management

# order placement, goal posts and transaction history

# notifications

# testing and alerts