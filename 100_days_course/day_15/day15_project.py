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
    "water": [300, 'ml'],
    "milk": [200, 'ml'],
    "coffee": [100, 'g'],
}
money = 0


def check_resources(coffee):
    for key, value in (MENU[coffee]["ingredients"]).items():
        if resources[key][0] < value:
            print(f"Sorry there is not enough {key}.")
            return False
    return True


def process_coins():
    global money
    quarters = int(input("How many quarters $0.25?: "))
    dimes = int(input("How many dimes $0.10?: "))
    nickles = int(input("How many nickles $0.05?: "))
    pennies = int(input("How many pennies $0.01?: "))
    sum_of_coins = quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01
    return round(sum_of_coins, 2)


def is_transaction_correct(payment, coffee):
    global money
    if payment >= MENU[coffee]['cost']:
        money += MENU[coffee]['cost']
        change = payment-MENU[coffee]['cost']
        print(f"Here is {round(change, 2)} dollars in change.")
        return True
    else:
        print("Sorry that's not enough money")
        return False


def coffee_process(coffee):
    for key, value in (MENU[coffee]["ingredients"]).items():
        resources[key][0] -= value
    print(f"Here is your {coffee}. Enjoy!")


is_on = True
while is_on:
    coffee_choice = input('What would you like? (espresso/latte/cappuccino): ').lower()
    if coffee_choice == 'off':
        is_on = False
    elif coffee_choice == 'report':
        for key, value in resources.items():
            print(f"{key.capitalize()}: {value[0]} {value[1]}")
        print(f"Money: ${float(money)}")
    elif coffee_choice in list(MENU.keys()):
        print(f"{coffee_choice} costs: ${MENU[coffee_choice]['cost']}")
        if check_resources(coffee_choice):
            payment = process_coins()
            if is_transaction_correct(payment, coffee_choice):
                coffee_process(coffee_choice)
    else:
        print('Wrong command. Try again')
