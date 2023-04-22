# 1
# with open('weather_data.csv', 'r') as file:
#     data = file.readlines()
#     print(data)

# 2
# import csv
#
# with open('weather_data.csv', 'r') as file:
#     data = csv.reader(file)
#     temperatures = []
#     for ind, row in enumerate(data):
#         if ind > 0:
#             temperatures.append(int(row[1]))
#     print(temperatures)

# 3
import pandas as pd

data = pd.read_csv('weather_data.csv')
data_dict = data.to_dict()
temp_list = data['temp'].to_list()
avg_temp = sum(temp_list)/len(temp_list)

print(data_dict)
print(temp_list)

# Avg
print(f"Avg temp is: {round(avg_temp, 2)}{chr(176)}C")
print(f"Avg temp is: {pd.Series.mean(data['temp'])}")
print(f"Avg: {data['temp'].mean()}")
# Max
print(f"Max temp is: {pd.Series.max(data['temp'])}")
print(f"Max: {data['temp'].max()}")

# Get data in Columns
condition1 = data['condition']
print(condition1)

condition2 = data.condition
print(condition2)

# Get data in Rows
monday_row = data[data.day == 'Monday']
print(monday_row)

# Row with max temp
row_with_max_temp = data[data.temp == data.temp.max()]
print(row_with_max_temp)

# Monday's temperature in Fahrenheit
monday = data[data.day == "Monday"]
monday_temp = int(monday.temp)
monday_temp_F = monday_temp * 9/5 + 32
print(f"Monday's temp in Fahrenheit: {monday_temp_F}")

# Creating a dataframe from scratch
data_dict1 = {
    "students": ["Amy", "Stan", "Angel"],
    "score": [76, 56, 65]
}
data1 = pd.DataFrame(data_dict1)
print(data1)
