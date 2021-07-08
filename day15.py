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
def check_resources(order_ingredients):
    for item in order_ingredients:
        if(order_ingredients[item]>=resources[item]):
            print(f'Not enough {item}')
            return False
    return True
        
def process_coins():
    print("Please insert coins")
    total=int(input("Enter number of quaters?: "))*0.5
    total+=int(input("Enter number of dimes? : "))*0.1
    total+=int(input("Enter many nickels?:"))*0.05
    total+=int(input("how many pennies?:"))*0.01
    return total

def profit(money_recieved,drink_cost):
    if(money_recieved>drink_cost):
        return True
    


while(True):
    resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
    profit=0
    choice=input("What would you like? (espresso/latte/cappuccino): ") #enter choices
    drink=MENU[choice] 
    type(drink["cost"])
    money=process_coins() #money entered
    print(f'Your amount = {money}')
    if(choice=='espresso'):   
        if(check_resources(drink["ingredients"])):
            print(f'Balance left is {total_money}$')
            print(f'{resources} \n Money:{total_money}$')  
    if(choice=='latte'):
        resources["water"]=resources["water"]-MENU["latte"]["ingredients"]["water"]
        resources["milk"]=resources["milk"]-MENU["latte"]["ingredients"]["milk"]
        resources["coffee"]=resources["coffee"]-MENU["latte"]["ingredients"]["coffee"]
        money=money-MENU[latte]["cost"]
        if((resources["water"]>=0) and (resources["milk"]>=0) and (resources["coffee"]>=0)):
            print(f'{resources} \n Money:{money}$')
            
    if(choice=='cappuccino'):
        resources["water"]=resources["water"]-cappiccino["water"]
        resources["milk"]=resources["milk"]-cappiccino["milk"]
        resources["coffee"]=resources["coffee"]-cappiccino["coffee"]
        money=money-1.5
        if((resources["water"]>=0) and (resources["milk"]>=0) and (resources["coffee"]>=0)):
            print(f'{resources} \n Money:{money}$')
            
    if(choice=='report'):
        print(f'Here is a summary of contents {resources}')




