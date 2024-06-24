# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if not row[1] == "temp":
#             temp = int(row[1])
#             temperatures.append(temp)
#
# print(temperatures)

# import pandas
#
# data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(data["temp"])

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()
# print(temp_list)
#
# average = sum(temp_list)/len(temp_list)
# print(average)

# print(data["temp"].mean())
# print(data["temp"].max()) #caps matter
# print(data.temp.max())

# Get data in rows

# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# print(monday.temp[0]*9/5+32)

# Create a dataframe from scratch

# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
#
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")

import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

gray = len(data[data["Primary Fur Color"] == "Gray"])
black = len(data[data["Primary Fur Color"] == "Black"])
cinnamon = len(data[data["Primary Fur Color"] == "Cinnamon"])

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray, cinnamon, black]
}

data_frame = pandas.DataFrame(data_dict)
data_frame.to_csv("squirrel_count")
