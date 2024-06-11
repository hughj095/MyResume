import csv

# Path to the CSV file
csv_file_path = r'C:\Users\johnm\OneDrive\Desktop\fortune100.csv'

# List to store ticker symbols
ticker_symbols = []

# Open the CSV file and read its contents
with open(csv_file_path, mode='r', newline='') as csvfile:
    csvreader = csv.DictReader(csvfile)
    
    # Loop through each row in the CSV
    for row in csvreader:
        # Extract the ticker symbol and add it to the list
        ticker_symbols.append(row['Ticker'])

with open(csv_file_path, mode='w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    
    # Write the header
    csvwriter.writerow(['Ticker'])
    
    # Write the ticker symbols
    for ticker in ticker_symbols:
        csvwriter.writerow([ticker])