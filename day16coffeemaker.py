class CoffeeMaker:
    def __init__(self):
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100
        }

    def report(self):
        print(f"Water: {self.resources['water']}ml")
        print(f"Milk: {self.resources['milk']}ml")
        print(f"Coffee: {self.resources['coffee']}g")

    def is_resource_sufficient(self, drink):
        """Check if resources are sufficient for the drink"""
        can_make = True
        for ingredient, amount in drink.ingredients.items():
            if amount > self.resources[ingredient]:
                print(f"Not enough {ingredient}.")
                can_make = False
        return can_make

    def make_coffee(self, order):
        """Deduct resources and make coffee"""
        for ingredient, amount in order.ingredients.items():
            self.resources[ingredient] -= amount
        print(f"Here is your {order.name}. Enjoy!")
