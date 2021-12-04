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
VALID_CHOICES = ['espresso', 'latte', 'cappuccino', 'report', 'off']

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}


def get_user_choice():
    """ Gets and returns the user's' valid choice from the menu. """

    choice = input("What would you like? (espresso/latte/cappuccino):").lower()
    if valid_choice(choice):
        return choice
    else:
        print("I'm sorry that's not a valid choice.")
        return get_user_choice()


def valid_choice(choice):
    """ Makes sure that the choice the user selected is valid. Returns True or False based
    on if the user choice is in a predefined set of choices."""

    if choice in VALID_CHOICES:
        return True
    else:
        return False


def check_ingredients(choice):
    """ Checks the user choice against the current amount of ingredients available,
    printing an error message and returning the list of insufficient ingredients.
    Returns an empty list if there are enough ingredients."""

    whats_lacking = []
    for ingredient in MENU[choice]["ingredients"]:
        if MENU[choice]["ingredients"][ingredient] > resources[ingredient]:
            whats_lacking.append(ingredient)

    if len(whats_lacking) == 1:
        print(f"Sorry there is not enough {whats_lacking[0]}.")
        coffee_machine()
    elif len(whats_lacking) == 2:
        print(f"Sorry there is not enough {whats_lacking[0]} or {whats_lacking[1]}.")
        coffee_machine()
    elif len(whats_lacking) == 3:
        print(f"Sorry there is not enough {whats_lacking[0]}, {whats_lacking[1]} or {whats_lacking[2]}.")
        coffee_machine()



def print_report():
    """ Prints a report of the resources the machine has on hand."""

    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']}")


def accept_coins():
    """Asks user to input the number of quarters, dimes, nickles, and pennies to deposit, and
    returns the monetary total in dollars."""

    quarters = int(input("How many quarters are you putting in? "))
    dimes = int(input("How many dimes are you putting in? "))
    nickles = int(input("How many dimes are you putting in? "))
    pennies = int(input("How many pennies are you putting in? "))

    amount_deposited = (25 * quarters + 10 * dimes + 5 * nickles + pennies)/100
    return amount_deposited


def handle_money(choice, amount_deposited):
    """Compares the amount of money deposited against the cost of the drink.  If enough
    money was deposited, gives appropriate change and credits the machine resources with the cost.
    If insufficient amount deposited, states that money is being refunded and does not change
    resource balance."""

    global resources
    drink_cost = MENU[choice]["cost"]

    if amount_deposited == drink_cost:
        print("Thank you for using exact change.")
        resources['money'] += drink_cost
        return True
    elif amount_deposited > drink_cost:
        refund_amount = "{:.2f}".format(amount_deposited - drink_cost)
        print(f"Here is ${refund_amount} in change.")
        resources['money'] += drink_cost
    else:
        print("Sorry that's not enough money. Money refunded.")
        coffee_machine()


def remove_ingredients(choice):
    """Deducts the ingredients used to make the user's choice from the machine resources."""
    global resources
    for ingredient in MENU[choice]["ingredients"]:
        resources[ingredient] -= MENU[choice]["ingredients"][ingredient]



def coffee_machine():
    power_on = True
    while power_on:
        choice = get_user_choice()
        if choice == "report":
            print_report()
        elif choice == 'off':
            power_on = False
        else:
            check_ingredients(choice)
            amount_deposited = accept_coins()
            handle_money(choice, amount_deposited)
            remove_ingredients(choice)



coffee_machine()

"""
stopping point:  buy a drink, buy a drink, buy a drink, type off.  off is not recognized, asks for coins.

7. Make Coffee.
a. If the transaction is successful and there are enough resources to make the drink the
user selected, then the ingredients to make the drink should be deducted from the
coffee machine resources.
E.g. report before purchasing latte:
Water: 300ml
Milk: 200ml
Coffee: 100g
Money: $0
Report after purchasing latte:
Water: 100ml
Milk: 50ml
Coffee: 76g
Money: $2.5
b. Once all resources have been deducted, tell the user “Here is your latte. Enjoy!”. If
latte was their choice of drink.
"""
