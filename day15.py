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


while(True):
    resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
    choice=input("What would you like? (espresso/latte/cappuccino): ")
    money=input("Enter your money in $")
    print(f'Your amount = {money}')
    if(choice=='espresso'):   
        resources["water"]=resources["water"]-MENU["espresso"]["ingredients"]["water"]
        resources["milk"]=resources["milk"]-["espresso"]["ingredients"]["milk"]
        resources["coffee"]=resources["coffee"]-["espresso"]["ingredients"]["coffee"]
        money=money-[espresso]["cost"]
        if((resources["water"]>0) and (resources["milk"]>0) and (resources["coffee"]>0)):
            print(f'{resources} \n Money:{money}$')  
    if(choice=='latte'):
        resources["water"]=resources["water"]-latte["water"]
        resources["milk"]=resources["milk"]-latte["milk"]
        resources["coffee"]=resources["coffee"]-latte["coffee"]
        money=money-1.2
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
        print(f'Here is a summary of contents {report}')




