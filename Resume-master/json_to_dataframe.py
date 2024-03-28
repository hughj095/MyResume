# This file inputs a json file, then converts it to a dataframe and references some value

import pandas as pd
import json

# Load JSON data into dictionary
with open('data.json', 'r') as file:
    data_dict = json.load(file)

# Convert dictionary to DataFrame
df = pd.DataFrame.from_dict(data_dict)

# Reference the value of the 4th row, 3rd column
value = df.iloc[3, 2]
print("Value in the 3rd column and 4th row:", value)

# Convert DataFrame back to JSON
df.to_json('new_data.json', orient='records')
