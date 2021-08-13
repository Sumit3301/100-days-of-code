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
print(df["temp"].mean()) #mean
print(df["temp"].max()) #max temprature

print(df.condition) #printing out colums

#searching through columns

print(df[df.day=="Monday"]) #specific day

print(df[df.temp==df.temp.max()]) #checking max temprature

dict = {
    "names":["raju","bala","ralo"],
    "class":[10,40,20]
}
data=pd.DataFrame(dict) #dict to dataframe
print(data)


data=pd.read_csv("weather_data.csv")
print(data)
data.to_csv("updated_data.csv") #dataferame to csv


