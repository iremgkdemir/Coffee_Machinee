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

profit = 0  # there is no money in the safe at first.


#order_ingredients = drink["ingredients"]
def is_resource_sufficient(order_ingredients):
    """Returns True when order make, False if ingredients are insufficient"""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item} ")  # item --> we're currently looping through
            return False  # end of the for loop
    return True


def process_coins():
    """Return the total calculated from coins inserted."""
    print("Please insert coins")
    total = int(input("  how many quarters?($0.25): ")) * 0.25
    total += int(input("  how many dimes?:($0.1) ")) * 0.1
    total += int(input("  how many nickles?:($0.05) ")) * 0.05
    total += int(input("  how many pennies?:($0.01) ")) * 0.01
    return total  # total return as an output and if you use return you should docstring


def is_process_successful(given_money, drink_cost):
    """Return True when the payment is accepted, or False if Money is insufficient"""
    if given_money < drink_cost:
        print("\nSorry that's not enough money. Money refunded.")
        return False
    else:
        change = round(given_money - drink_cost, 2)
        print(f"\nHere is ${change} in change.")
        global profit
        profit += drink_cost
        return True


def make_coffee(drink_name, order_ingredients):
    """reduce ingredients"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]

    print(f"\nHere is your coffee {drink_name}")


is_on = True

# when is_on false over and over again will started
while is_on:
    choice = input("\nWhat would you like? (espresso/latte/cappuccino)  ").lower()
    if choice == "off":
        is_on = False

    elif choice == "report":
        print(f"Water {resources['water']}ml")
        print(f"Milk {resources['milk']}ml")
        print(f"Coffee {resources['coffee']}g")
        print(f"Money: ${profit}")

    else:

        drink = MENU[choice]

        if is_resource_sufficient(drink["ingredients"]):  # ingredients are in MENU and is enough == true
            payment = process_coins()
            if is_process_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
