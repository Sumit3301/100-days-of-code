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
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

while(True):
    choice=input("What would you like? (espresso/latte/cappuccino): ")
    if(choice=='espresso'):
        if((resources["water"]>espresso["water"]) and (resources["milk"]>espresso["milk"]) and (resources["coffee"]>espresso["coffee"])):
            print(cappiccino)
             
        


