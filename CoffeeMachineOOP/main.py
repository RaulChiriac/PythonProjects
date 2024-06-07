from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


client = Menu()
info = CoffeeMaker()
infom = MoneyMachine()
is_ok = True


while is_ok:
    options = client.get_items()
    choice = input(f'What would you want? {options}: ')
    if choice == 'off':
        is_ok =False
    elif choice == 'report':
        info.report()
        infom.report()
    else:
        drink = client.find_drink(choice)
        if info.is_resource_sufficient(drink) and infom.make_payment(drink.cost):
            info.make_coffee(drink)
