import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv('data.csv')

# Print the DataFrame
print(df)



df['Ice Cream Profits'] = df['Ice Cream Profits'].apply(lambda x: '${:.2f}'.format(x))
print(df)
