#Coffee Mchine Program 😁
#It serves Espresso, Latte and Cappuccino
#User can see report of available resources and profit by typing 'report' as input
#Maintainers can turn the program of by typing 'off' as input
#The machine checks for sufficient ingredients and processes coin inputs

#Menu with recipes and cost for each drink
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

#Initial resources available
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def return_bill(q,d,n,p,choice):
    '''Calculates the change after payment and returns it'''
    #q=quarters, d=dimes, n=nickles, p=pennies
    return round((q*0.25+d*0.1+n*0.05+p*0.01)-MENU[choice]["cost"],2)

#Report keeps track of resources and profit
report={
    "water":300,
    "milk":200,
    "coffee":100,
    "money":0,
}

#Main function to run the coffee machine
def machine():
    choice=input("\nWhat would you like?😊 (espresso/latte/cappuccino): ").lower()
    #Option to turn off the machine
    if choice=="off":
        return ""
    #Displays the current resources and money collected
    if choice=="report":
        print(f"Water: {report['water']}ml")
        print(f"Milk: {report['milk']}ml")
        print(f"Coffee: {report['coffee']}g")
        print(f"Money: ${report['money']}")
        machine()
    elif choice=="espresso" or "latte" or "cappuccino":
        for item in MENU[choice]["ingredients"]: #Checks if the ingredients are sufficient for the chosen drink
            if report[item] < MENU[choice]["ingredients"][item]:
                print(f"Sorry there is not enough {item}")
                machine()
        else:
            #Asks the user to insert coins
            print("Please insert coins")
            quarters = int(input("How many quarters?: "))
            dimes = int(input("How many dimes?: "))
            nickles = int(input("How many nickles?: "))
            pennies = int(input("How many pennies?: "))
            #Calculates change
            change=return_bill(quarters,dimes,nickles,pennies,choice)
            if change<0:
                print("Sorry. That's not enough money. Money refunded. ")
                machine()
            elif change>0 and report["water"]>0:
                #Deduct the used ingredients
                report["water"]-=MENU[choice]["ingredients"]["water"]
                report["milk"] -= MENU[choice]["ingredients"].get("milk",0)
                report["coffee"] -= MENU[choice]["ingredients"]["coffee"]
                report["money"] += MENU[choice]["cost"]
                #Provide the drink and change
                print(f"Here is ${change} in change.")
                print(f"Here is your {choice}.☕ Enjoy!")
                machine()

#Start the coffee machine
machine()