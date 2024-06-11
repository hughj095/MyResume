import csv

# Path to the CSV file
csv_file_path = r'C:\Users\johnm\OneDrive\Desktop\fortune100_stock_symbols.csv'

import pandas as pd

# Load the new CSV file
file_path = r'C:\Users\johnm\OneDrive\Desktop\fortune100_stock_symbols.csv'
df = pd.read_csv(file_path)

# Remove anything right of a comma, including the comma
df['Stock Symbol'] = df['Stock Symbol'].str.split(',').str[0]

# Save the modified DataFrame to a new CSV file
output_path = r'C:\Users\johnm\OneDrive\Desktop\fortune100_stock_symbols.csv'
df.to_csv(output_path, index=False)

print(f"Modified file saved to {output_path}")