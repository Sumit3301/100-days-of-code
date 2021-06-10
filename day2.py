print("Welcome to the tip calculator.")
total=float(input("What was the total bill $"))
split=float(input("How many people to split the bill? "))
percentage=float(input("What percentage would you like to tip? 10, 12 or 15? "))
person=total*percentage/100+total
each_person=person/split
each_person=str(each_person)
print("Each person should pay: $"+ each_person)
