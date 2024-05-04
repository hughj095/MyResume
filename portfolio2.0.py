# imports and variables
import requests
import pprint

TICKER = 'AAPL'
MULTIPLIER = '1'
TIMESPAN = 'hour'
DATESTART = '2024-05-03'
DATEEND = '2024-05-03'
APIKEY = 'hldKpOcQ9ago1ZA83XRyRQ1tFG5uokBa'

# API pull data

url = f'https://api.polygon.io/v2/aggs/ticker/{TICKER}/range/{MULTIPLIER}/{TIMESPAN}/{DATESTART}/{DATEEND}?apiKey={APIKEY}'
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    #pprint.pprint(data)
else:
    print('Error:', response.status_code, response.content)

# indicators and management

    # CONVERT TO PD DATAFRAME
data['Resistance'] = ''
for row in data['results']:
    row['c'] = float(row['c'])
for c in data['results']:
    if (
            c >= c-1
            and df.iloc[i,4] >= df.iloc[i - 2,4]
            and df.iloc[i,4] >= df.iloc[i + 1,4]
            and (i < len(df)-2 and df.iloc[i,4] >= df.iloc[i + 2,4])
        ):
            df.iloc[i, 6] = "resistance"

# order placement, goal posts and transaction history

# notifications

# testing and alerts