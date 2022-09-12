"""
Transition from Replit to Pycharm

What is Pycharm?
- It is a coding IDE for professional developers tailored specifically for Python development. It has:
    - Spell Check
    - Refactor Code Made Easy
    - View Structures
    - Built-in Linters
    - More Space  
"""

water = 5000
milk = 2000
coffee = 500
money = 0


def check_resource(choice):
    if choice == 'cappuccino':
        if water < 250:
            print("There's not enough water.")
            return False
        elif coffee < 24:
            print("There's not enough coffee.")
            return False
        elif milk < 100:
            print("There's not enough milk.")
            return False
        else:
            return True
    elif choice == 'latte':
        if water < 200:
            print("There's not enough water.")
            return False
        elif coffee < 24:
            print("There's not enough coffee.")
            return False
        elif milk < 150:
            print("There's not enough milk.")
            return False
        else:
            return True
    elif choice == 'espresso':
        if water < 50:
            print("There's not enough water.")
            return False
        elif coffee < 18:
            print("There's not enough coffee.")
            return False
        else:
            return True


def check_price(total_deposited):
    if total_deposited < 2.5:
        print("Not enough money.")
        return False
    else:
        return True


def print_resources(water_amount, milk_amount, coffee_amount, collected_money):
    print(f"Water: {water_amount}ml")
    print(f"Milk: {milk_amount}ml")
    print(f"Coffee: {coffee_amount}g")
    print(f"Money: ${collected_money}")


def insert_coin():
    quarters = int(input("How many quarters?: ")) * 0.01
    dimes = int(input("How many dimes?: ")) * 0.05
    nickles = int(input("How many nickles?: ")) * 0.1
    pennies = int(input("How many pennies?: ")) * 0.25
    return quarters + dimes + nickles + pennies

# Penny $0.01 | Nickel $0.05 | Dime $0.1 | Quarter $0.25


coffee_choice = input("What would you like? | Espresso | Latte | Cappuccino (for report type 'report'): ").lower()


if coffee_choice != 'report':
    # while not coffee_choice == 'cappuccino' or coffee_choice == 'latte' or coffee_choice == 'espresso':
    #     print("Invalid input.")
    #     coffee_choice = input("What would you like? | Espresso | Latte | Cappuccino (for report type 'report'): ").lower()
    check_resource_result = check_resource(coffee_choice)
    if check_resource_result:
        print("Please insert coins.")
        total = insert_coin()
        print(f"Your deposit is: {total}")
        while not check_price(total):
            continue_add_money = input("You may want to add more money (yes/no): ").lower()
            if continue_add_money == 'yes':
                total += insert_coin()
        if check_price(total):
            print(f"Here is your {coffee_choice}!")
            money_changes = total - 2.5
            money += 2.5
            print(f"And here is your changes: ${money_changes}")
elif coffee_choice == 'report':
    print_resources(water, milk, coffee, money)