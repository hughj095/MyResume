# This program uses Pandas to read csv squirrel data, then filter and count
# and create a new dataframe and csv from the filtered data

import csv
import pandas

data = pandas.read_csv("./squirrel data/data.csv")
grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
cin_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])

print(grey_squirrels_count,cin_squirrels_count,black_squirrels_count)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrels_count, cin_squirrels_count,black_squirrels_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("./squirrel data/squirrel_count.csv")

# data_df = pandas.DataFrame(data_csv)
# data_csv2 = data_df.to_csv("new_csv.csv")