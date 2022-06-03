from coffee_art import logo
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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

print(logo)
profit = 0

def report():
    """Function that prints the report, when the user enters report in the prompt"""
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    print(f" Water: {water} \n Milk: {milk} \n Coffee: {coffee} \n Money: ${profit}")

def type_of_coffee(amount, coffee):
    """Function that updates the resources after a user enters a coffee choice, checks if the amount of money
    entered is enough for the amount of coffee chosen, and calculates the change if user enters more money
    that needed."""
    cost = MENU[coffee]["cost"]
    new_water = int(resources["water"]) - int(MENU[coffee]["ingredients"]["water"])
    resources["water"] = new_water
    new_coffee = int(resources["coffee"]) - int(MENU[coffee]["ingredients"]["coffee"])
    resources["coffee"] = new_coffee
    if coffee == "latte" or coffee == "cappuccino":
        new_milk = int(resources["milk"]) - int(MENU[coffee]["ingredients"]["milk"])
        resources["milk"] = new_milk
    if amount < cost:
        print("Sorry that's not enough money. Money refunded." )
    else:
        change = amount - cost
        print(f"Here is ${round(change, 2)} in change.")
        print(f"Here is your {coffee}. Enjoy!")

#Function that calculates the amount of money the user inputs
def money():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickels = int(input("how many nickels?: "))
    pennies = int(input("how many pennies?: "))
    total = (quarters * .25) + (dimes * .10) + (nickels * .05) + (pennies * .01)
    return total

def resources_sufficient(coffee):
    """Returns True when order can be made, False if ingredients are insufficient"""
    if resources["water"] < MENU[coffee]["ingredients"]["water"]:
        print("Sorry there is not enough water.")
        return False
    elif resources["coffee"] < MENU[coffee]["ingredients"]["coffee"]:
        print("Sorry there is not enough coffee.")
        return False
    elif coffee == "latte" or coffee == "cappuccino":
        if resources["milk"] < MENU[coffee]["ingredients"]["milk"]:
            print("Sorry there is not enough milk.")
            return False
#While loop boolean
continue_program = True

while continue_program:
    prompt = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if prompt == "off":
        continue_program = False
    elif prompt == "report":
        report()
    elif resources_sufficient(prompt) == False:
        continue
    if prompt == "espresso":
        type_of_coffee(money(), "espresso")
        profit += 1.5
    elif prompt == "latte":
        type_of_coffee(money(), "latte")
        profit += 2.5
    elif prompt == "cappuccino":
        type_of_coffee(money(), "cappuccino")
        profit += 3.0








