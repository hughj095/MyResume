# This program has various pandas and csv functions


# import csv

# with open("./weather_data/weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(row[1])
#     print(temperatures)

import pandas 

#Read and conver to dict
data = pandas.read_csv("./weather_data/weather_data.csv")
data_dict = data.to_dict()
print(data_dict)

#Convert dict to PD Dataframe
data = pandas.DataFrame(data_dict)
print(data)

#Convert df to csv and save
data.to_csv("new_data.csv")

# temp_list = data['temp'].to_list()
# print(temp_list)
# print(data['temp'].mean())
# print(data['temp'].max())
# can print column with column name as data.____
# print(data.condition)
# cel = data[data.temp == data.temp.max()]
# cel.temp = cel.temp * 1.8 + 32
# print(cel)

