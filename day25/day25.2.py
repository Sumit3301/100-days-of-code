import pandas as pd

df=pd.read_csv("squirrel_dataset.csv")

gray_squirrels=len(df[df["Primary Fur Color"]=="Gray"])
print(gray_squirrels)

cinnamon_squirrels=len(df[df["Primary Fur Color"]=="Cinnamon"])
print(cinnamon_squirrels)

dict={
    "Primary Fur Color":["Gray","Cinnamon"],
    "Number":[gray_squirrels,cinnamon_squirrels]
}

data=pd.DataFrame(dict)
print(data)

data.to_csv("Squirrels.csv")

