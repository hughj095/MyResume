import requests
import pandas as pd

API_KEY = 'hldKpOcQ9ago1ZA83XRyRQ1tFG5uokBa'
ticker = 'AAPL'
multiplier = '1'
timespan = 'day'
start = '2023-01-09'
end = '2023-01-09'
split_adjust = 'true'
sort = 'asc'
limit = '120'


url = f'https://api.polygon.io/v2/aggs/ticker/{ticker}/range/{multiplier}/{timespan}/{start}/{end}?adjusted={split_adjust}&' \
        f'sort={sort}&limit={limit}&apiKey={API_KEY}'
r = requests.get(url)
data = r.json()
df = pd.json_normalize(data['results'])
df.insert(0,'Ticker',ticker)
print(df)



