
class MoneyMachine:
    coins_value = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickels": 0.05,
        "pennies": 0.01
    }

    def __init__(self):
        self.profit = 0
        self.money_received = 0

    def report(self):
        print(f"Money: ${self.profit}")

    def process(self):
        print("Enter coins")
        for coin in self.coins_value:
            self.money_received += int(input(f"How many {coin}: ")) * self.coins_value[coin]
        return self.money_received

    def make_payment(self, cost):
        self.process()
        if self.money_received >= cost:
            change = round(self.money_received - cost, 2)  # Round to 2 decimal places
            print(f"Here is your change: ${change}")
            self.profit += cost
            self.money_received = 0
            return True
        else:
            print("Not enough money.")
            self.money_received = 0
            return False