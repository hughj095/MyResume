### imports and variables
import requests
import pandas as pd

TICKER = 'AAPL'
MULTIPLIER = '5'
TIMESPAN = 'minute'
DATESTART = '2024-05-03'
DATEEND = '2024-05-03'
APIKEY = 'hldKpOcQ9ago1ZA83XRyRQ1tFG5uokBa'

### API pull data

url = f'https://api.polygon.io/v2/aggs/ticker/{TICKER}/range/{MULTIPLIER}/{TIMESPAN}/{DATESTART}/{DATEEND}?apiKey={APIKEY}'
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    #pprint.pprint(data)
else:
    print('Error:', response.status_code, response.content)

### indicators and management

# data pre-processing
df = pd.DataFrame(data['results'])
df['c'] = df['c'].astype(float)

# Resistance marker at close
df['Resistance/Support'] = ''   # column 8
for i in range(len(df)):
    if (
            df.iloc[i,3] >= df.iloc[i - 1,3]
            and df.iloc[i,3] >= df.iloc[i - 2,3]
            and df.iloc[i,3] >= df.iloc[i + 1,3]
            and (i < len(df)-2 and df.iloc[i,3] >= df.iloc[i + 2,3])
        ):
            df.iloc[i, 8] = "resistance"

# Support marker at close
for i in range(len(df)):
    if (
            i >= 2 and i < len(df) - 2
            and df.iloc[i,3] <= df.iloc[i - 1,3]
            and df.iloc[i,3] <= df.iloc[i - 2,3]
            and df.iloc[i,3] <= df.iloc[i + 1,3]
            and df.iloc[i,3] <= df.iloc[i + 2,3]
        ):
            df.iloc[i, 8] = "support"

# Did latest resistance break above previous resistance level?
df['Break'] = '' # column 9
x = 0
count = 0
for i in range(len(df)):
    if df.iloc[i,8] == "resistance":
        count += 1
    if (
        df.iloc[i,8] == "resistance"
        and df.iloc[i,3] > df.iloc[x,3] 
        and count > 1
        ):
            df.iloc[i,9] = "break"
            x = i

# order placement, goal posts and transaction history

# if support then buy, while buy, if resistance + break then hold, if resistance then sell, if support then hold




# notifications
df.to_csv(r'C:\Users\johnm\OneDrive\Desktop\MyResume\df.csv')
# testing and alerts