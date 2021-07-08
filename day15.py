MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}



latte={
    "water":50,
    "milk":70,
    "coffee":40
}

espresso={
    "water":50,
    "milk":70,
    "coffee":40
}

cappiccino={
    "water":50,
    "milk":70,
    "coffee":40
}
profit=0.00
def check_resources(order_ingredients):
    for item in order_ingredients:
        if(order_ingredients[item]>=resources[item]):
            print(f'Not enough {item}')
            return False
    return True
        
"""def process_coins():
    print("Please insert coins")
    total=int(input("Enter number of quaters?: "))*0.5
    total+=int(input("Enter number of dimes? : "))*0.1
    total+=int(input("Enter many nickels?:"))*0.05
    total+=int(input("how many pennies?:"))*0.01
    return total
"""
def profit(money_recieved,drink_cost):
    if(money_recieved>drink_cost):
        global profit
        profit+=drink_cost
        return profit
    


while(True):
    resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}   
    choice=input("What would you like? (espresso/latte/cappuccino): ") #enter choices
    drink=MENU[choice]
    cost_of_drink=drink["cost"] #money for drink
    money=float(input("Enter your money:"))
    print(f'Your amount = {money}')
    if(choice=='espresso'):   
        if(check_resources(drink["ingredients"])):
            balance_money=money-drink["cost"]
            print(f'Balance left is {balance_money}$')
            print(f'{resources} \n Money:{money}$')  
    if(choice=='latte'):
        if(check_resources(drink["ingredients"])):
            balance_money=money-drink["cost"]
            print(f'Balance left is {balance_money}$')
            print(f'{resources} \n Money:{money}$') 
            profit=profit+drink["cost"]
    if(choice=='cappuccino'):
        if(check_resources(drink["ingredients"])):
            balance_money=money-drink["cost"]
            print(f'Balance left is {balance_money}$')
            print(f'{resources} \n Money:{money}$') 
            profit=profit+drink["cost"]
    if(choice=='report'):
        print(f'Here is a summary of contents {resources}')




