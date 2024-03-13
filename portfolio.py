# Alpha Vantage API

import requests

stock1 = 'MCD'
stock2 = 'DG'
stock3 = 'COIN'
stock4 = 'HD'
stock5 = 'NVDA'

API_KEY = 'LNR6C1L773RCAOFY'

# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={stock1}&interval=5min&apikey={API_KEY}'
r = requests.get(url)
data = r.json()

# need only the first value here open and close
print(data['Time Series (5min)'][0])

