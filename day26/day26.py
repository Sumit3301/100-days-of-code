"""Pandas iteration method
for(index,row) in df.iterrow():
    print(row)"""
import pandas as pd
from pandas.core.frame import DataFrame

#implementation of list comprehension in US State list

df=pd.read_csv("nato_list.csv")

new_dict={row.letter:row.code for (index,row) in df.iterrows()} #reading data and putting it into a dictionary using dictionary
##print(new_dict)
inp= input("Enter your name").upper()
for i in inp:
    print(new_dict[i])



