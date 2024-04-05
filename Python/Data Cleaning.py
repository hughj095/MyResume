# This is a great template for Data Cleaning Operations
#   Specific data is a csv of Netflix data

import pandas as pd

# Import the csv as a df
df = pd.read_csv(r'C:\Users\johnm\OneDrive\Desktop\MyResume\Python\netflix_titles.csv')

# Print view the top 5 rows and all headers and their data types
print(df.head())
print(df.columns)
print(df.dtypes)

# Missing Data (nulls, na's and zeros)
null_values = df.isnull()
print("Count of null values:")
print(df.isnull().sum())

na_values = df.isna()
print("Count of n/a values:")
print(df.isna().sum())

values_0 = df == 0
print("Count of 0 values:")
print(values_0.sum())

# Replace na's and nulls with zero
df.fillna(0, inplace=True)

# Cast certain columns from string to dates and integers to dates
df['date_added'] = pd.to_datetime(df['date_added'], format='mixed')
df['release_year'] = pd.to_datetime(df['release_year'], format='%Y')

df.to_csv(r'C:\Users\johnm\OneDrive\Desktop\MyResume\Python\netflix_titles_cleaned.csv')

print('all set!')