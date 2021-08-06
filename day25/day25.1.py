"""
import csv
tempratures=[]
with open("weather_data.csv") as data_file:
    data=csv.reader(data_file)
    tempratures=[]
    for row in data:
        if(row[1]) != "temp":
            tempratures.append(int(row[1]))
print(tempratures)

"""

import pandas as pd

df=pd.read_csv("weather_data.csv")
print(df["temp"].mean())
print(df["temp"].max())

print(df.condition)



