MENU = {
    "espresso": {"ingredients": {"water": 50, "coffee": 18}, "cost": 1.5},
    "latte": {"ingredients": {"water": 200, "milk": 150, "coffee": 24}, "cost": 2.5},
    "cappuccino": {"ingredients": {"water": 250, "milk": 100, "coffee": 24}, "cost": 3.0},
}

resources = {"water": 300, "milk": 200, "coffee": 100}
profit = 0  # Define profit outside functions


def print_report():
    """Prints the current resource values and profit."""
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${profit:.2f}")


def check_resources(drink):
    """Checks if the machine has enough resources to make the selected drink."""
    for item, amount in drink["ingredients"].items():
        if resources[item] < amount:
            print(f"Sorry, there is not enough {item}.")
            return False
    return True


def process_coins():
    """Prompts the user to insert coins and calculates the total amount."""
    print("Please insert coins.")
    quarters = int(input("How many quarters? ")) * 0.25
    dimes = int(input("How many dimes? ")) * 0.10
    nickels = int(input("How many nickels? ")) * 0.05
    pennies = int(input("How many pennies? ")) * 0.01
    return quarters + dimes + nickels + pennies


def make_coffee(drink):
    """Deducts the required ingredients from the resources."""
    for item, amount in drink["ingredients"].items():
        resources[item] -= amount


def coffee_machine():
    global profit
    is_on = True
    while is_on:
        choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if choice == "off":
            print("Turning off the coffee machine. Goodbye!")
            is_on = False
        elif choice == "report":
            print_report()
        elif choice in MENU:
            drink = MENU[choice]
            if check_resources(drink):
                payment = process_coins()
                if payment >= drink["cost"]:
                    change = round(payment - drink["cost"], 2)
                    print(f"Here is ${change} in change.")
                    profit += drink["cost"]
                    make_coffee(drink)
                    print(f"Here is your {choice}. Enjoy! ☕")
                else:
                    print("Sorry, that's not enough money. Money refunded.")
        else:
            print("Invalid choice. Please choose again.")


# Start the Coffee Machine Program
coffee_machine()
