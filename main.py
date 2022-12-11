import MenuAndResourses
from copy import deepcopy

resources = deepcopy(MenuAndResourses.resources)
MENU = deepcopy(MenuAndResourses.MENU)


def money_inser(price):
    global resources

    print("Please insert coins")
    quarters = int(input('How many quarters? '))
    dimes = int(input('How many dimes? '))
    nickles = int(input('How many nickles? '))
    pennies = int(input('How many pennies? '))
    notenough = None

    total = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
    if total == price:
        resources["money"] += price

    if total > price:
        print(f"Here is your change: {total - price}$")
        resources["money"] += price

    if total < price:
        print("Sorry there's not enough money. Money refunded")
        notenough = 0

    return notenough


def coffee_maker(drink):
    global resources
    global MENU

    if drink == "espresso":
        resources["water"] -= MENU["espresso"]["ingredients"]["water"]
        resources["coffee"] -= MENU["espresso"]["ingredients"]["coffee"]

    elif drink == "latte":
        resources["water"] -= MENU["latte"]["ingredients"]["water"]
        resources["milk"] -= MENU["latte"]["ingredients"]["milk"]
        resources["coffee"] -= MENU["latte"]["ingredients"]["coffee"]

    elif drink == "cappuccino":
        resources["water"] -= MENU["cappuccino"]["ingredients"]["water"]
        resources["milk"] -= MENU["cappuccino"]["ingredients"]["milk"]
        resources["coffee"] -= MENU["cappuccino"]["ingredients"]["coffee"]


def drink_and_resources(answ):
    making = False
    global resources
    global MENU

    if answ == "espresso":
        if resources['water'] >= MENU['espresso']['ingredients']['water'] and resources['coffee'] >= \
                MENU['espresso']['ingredients']['coffee']:
            making = True
        else:
            print("Not enough resources. Sorry")

    elif answ == "latte":
        if resources['water'] >= MENU['latte']['ingredients']['water'] and resources['coffee'] >= \
                MENU['latte']['ingredients']['coffee'] and resources['milk'] >= MENU['latte']['ingredients']['milk']:
            making = True
        else:
            print("Not enough resources. Sorry")

    elif answ == "cappuccino":
        if resources['water'] >= MENU['cappuccino']['ingredients']['water'] and resources['coffee'] >= \
                MENU['cappuccino']['ingredients']['coffee'] and resources['milk'] >= MENU['cappuccino']['ingredients'][
            'milk']:
            making = True
        else:
            print("Not enough resources. Sorry")

    elif answ == "report":
        print(f'Water: {resources["water"]}ml \nMilk {resources["milk"]}ml \nCoffee {resources["coffee"]}g \n'
              f'Money ${resources["money"]} ')

    return making


while True:
    answer = str(input("What would you like? (espresso/latte/cappuccino): "))

    if answer == "off":
        break

    beverage = drink_and_resources(answer)

    if beverage is True:
        price = MENU[answer]["cost"]
        inserting = money_inser(price)
        if inserting == 0:
            continue
        coffee_maker(answer)
        print(f"Here is your {answer}. Enjoy!")

    else:
        continue
