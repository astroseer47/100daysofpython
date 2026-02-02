import csv

import pandas as pd

with open("./weather_data.csv") as file:
    data = csv.reader(file)
    temperatures = []
    for row in data:
        if row[1] == 'temp':
            continue
        temperatures.append((row[1]))
        print(row)

    print(temperatures)

data = pd.read_csv("./weather_data.csv")
print(data)
print(data['temp'])

print(type(data))
print(type(data['temp']))

data_dict = data.to_dict('records')
print(data_dict)


temp_list = data['temp'].to_list()
print(temp_list)

print(data[data.day == "Monday"])
max_temp = data.temp.max()
print(max_temp)
print(data[data.temp == max_temp])

# Create a dataframe

data_dict = {
    "students": ["John"],
    "age": [12]
}
data = pd.DataFrame(data_dict)
data.to_csv("./students_data.csv")
