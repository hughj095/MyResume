# This program inputs the response from the Mashvisor apartment rate API per state, city and zip (traditional and airbnb)
#   and outputs an organized dataframe

import requests
import pandas as pd
import openpyxl

url = "https://mashvisor-api.p.rapidapi.com/rental-rates"

# PARAMETERS (enter parameters here)
STATE = 'RI'
SOURCE = 'traditional'   #traditional or airbnb
CITY = 'CUMBERLAND'
ZIP = '02864'
API_KEY = 'YOUR KEY HERE'

# request info in json
querystring = {"state":STATE,"source":SOURCE,"city":CITY,"zip_code":ZIP}
headers = {
	"X-RapidAPI-Key": API_KEY,
	"X-RapidAPI-Host": "mashvisor-api.p.rapidapi.com"
}
response = requests.get(url, headers=headers, params=querystring)
print(response.json())
data_list = response.json()

# Drill down the json to the rental rates level
rental_rates = data_list['content']['retnal_rates']

# Create empty lists
room_types = []
values = []

# Loop through rental rates and append to empty lists 
for room_type, value in rental_rates.items():
    room_types.append(room_type)
    values.append(value)

# Create a DataFrame from the lists by zipping the lists as columns
df = pd.DataFrame(list(zip(room_types, values)), columns=['Room Type', 'Value'])

print(df)