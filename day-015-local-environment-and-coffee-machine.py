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
    "revenue": 0
}


def is_resource_sufficient(order_ingredients):
    is_enough = True
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"There's not enough {resources[item]}.")
            return False
    return is_enough


def check_price(total_deposited):
    if total_deposited < drink["cost"]:
        print("Not enough money.")
        return False
    else:
        return True


def print_resources(water_amount, milk_amount, coffee_amount, collected_money):
    print(f"Water: {water_amount}ml")
    print(f"Milk: {milk_amount}ml")
    print(f"Coffee: {coffee_amount}g")
    print(f"Money: {collected_money}")


def process_coins():
    print("Please insert coins...")
    quarters = int(input("How many quarters?: ")) * 0.01
    dimes = int(input("How many dimes?: ")) * 0.05
    nickles = int(input("How many nickles?: ")) * 0.1
    pennies = int(input("How many pennies?: ")) * 0.25
    return quarters + dimes + nickles + pennies


def is_wrong_input(choice):
    while not choice == 'cappuccino' and not choice == 'latte' and not choice == 'espresso':
        print("Invalid input.")
        choice = input("What would you like? | Espresso | Latte | Cappuccino (for report type 'report'): ").lower()

# Penny $0.01 | Nickel $0.05 | Dime $0.1 | Quarter $0.25


is_on = True

water = resources["water"]
milk = resources["milk"]
coffee = resources["coffee"]
revenue = resources["revenue"]

while is_on:
    coffee_choice = input("What would you like? (Espresso | Latte | Cappuccino): ").lower()
    if coffee_choice == 'report':
        print_resources(water, milk, coffee, revenue)
    elif coffee_choice == "off":
        is_on = False
    else:
        is_wrong_input(coffee_choice)
        drink = MENU[coffee_choice]
        if is_resource_sufficient(drink["ingredients"]):
            total = process_coins()
            print(f"Your deposit is: {total}")
            while not check_price(total):
                continue_add_money = input("You may want to add more money (yes/no): ").lower()
                if continue_add_money == 'yes':
                    total += process_coins()
            if check_price(total):
                print(f"Here is your {coffee_choice} ☕!")
                money_changes = round(total - 2.5)
                revenue += 2.5
                print(f"And here is your changes: ${money_changes}")




