from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# My first project in OOP

# Initiate an instance of CoffeeMaker
coffee_machine_1 = CoffeeMaker()
main_menu = Menu()  # initiate an object from class Menu()
finance_coffee_machine_1 = MoneyMachine()

is_on = True
while is_on:
    # Prompts the user to pick an item from menu
    item = input("What would you like:  " + f"({main_menu.get_items()}): ").lower()
    # Machine will find the drink in the menu and returns its ingredients and cost.
    # Returns the drink as an object from the Class Menu()

    # Check for the input of the user
    if item == "report":
        coffee_machine_1.report()
        finance_coffee_machine_1.report()
    elif item == "off":
        is_on = False
    else:
        drink_chosen = main_menu.find_drink(item)
        if coffee_machine_1.is_resource_sufficient(drink_chosen):   # Check if resources is enough
            if finance_coffee_machine_1.make_payment(drink_chosen.cost):  # Prompts the user to make payment.
                # The coffee is made, and the resources & profit gets updated.
                coffee_machine_1.make_coffee(drink_chosen)