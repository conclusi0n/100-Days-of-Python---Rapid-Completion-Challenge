class MenuItem:
    """Models each Menu Item."""
    def __init__(self, name, water, milk, coffee, cost):
        self.name = name
        self.cost = cost
        self.ingredients = {
            "water": water,
            "milk": milk,
            "coffee": coffee
        }

class Menu:
    """Models the Menu containing multiple items."""
    def __init__(self):
        self.menu = [
            MenuItem(name="latte", water=200, milk=150, coffee=24, cost=2.5),
            MenuItem(name="espresso", water=50, milk=0, coffee=18, cost=1.5),
            MenuItem(name="cappuccino", water=250, milk=50, coffee=24, cost=3),
        ]

    def get_options(self):
        """Returns a string of all menu item names separated by slashes."""
        options = ""
        for item in self.menu:
            options += f"{item.name}/"
        return options.strip("/")  # Removes trailing slash

    def find_drink(self, order_name):
        """Finds a drink by name."""
        for item in self.menu:
            if item.name == order_name:
                return item
        return None  # Return None if no matching drink is found


# Main Interaction
menu = Menu()

while True:
    # Display menu options
    print(f"Available options: {menu.get_options()}")
    order = input("What would you like? ").lower()

    # Find and process the drink
    drink = menu.find_drink(order)
    if drink:
        print(f"You ordered {drink.name}, which costs ${drink.cost}. Ingredients: {drink.ingredients}")
    else:
        print("Not available.")