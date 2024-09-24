"""import csv

with open("t20worldwinner.csv") as data_file:

    data = csv.reader(data_file)
    year = []
    for row in data:
        if row[0] != "Year":
            year.append(int(row[0]))
    print(row) """

import pandas


data = pandas.read_csv("t20worldwinner.csv")
print(data["Year"])
print(data)
data_d = data["Year"].to_dict()
print(data_d)
print(data[data.Winner =="India"])
print(data[data.Runners_Up == "Pakistan"])

print(123_344_349)
    