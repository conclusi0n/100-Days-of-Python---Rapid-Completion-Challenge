from Day16menue import Menu, MenuItem
from day16coffeemaker import CoffeeMaker
from Day16moneymachine import MoneyMachine

# Initialize main components
menu = Menu()  # This contains the menu items
coffee_maker = CoffeeMaker()  # Handles resource checks and coffee-making
money_machine = MoneyMachine()  # Handles payments

on = True  # Controls the coffee machine loop

while on:
    # Get user input
    choice = input(f"What would you like? ({menu.get_options()}): ").lower()

    if choice == 'off':
        print("Turning off. Goodbye!")
        on = False
    elif choice == 'report':
        # Show reports
        coffee_maker.report()
        money_machine.report()
    else:
        # Find the drink in the menu
        coffee_choice = menu.find_drink(choice)

        if coffee_choice:
            # Check resources and process payment
            if coffee_maker.is_resource_sufficient(coffee_choice) and money_machine.make_payment(coffee_choice.cost):
                coffee_maker.make_coffee(coffee_choice)
        else:
            print(f"'{choice}' is not a valid option. Please choose from {menu.get_options()}.")







