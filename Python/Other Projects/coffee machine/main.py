
from typing import OrderedDict
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker

#Classes
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

#starts with coffee machine 'on' to work
machine = "on"
while machine == "on":
    #choose menu item
    options = menu.get_items()
    choice = input(f"What would you like? {options}")
    if choice == "off":
        machine = "off"
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        #check if machine has resources, pay, and make coffee
        drink = menu.find_drink(choice)
        print(drink)
        print(coffee_maker.is_resource_sufficient(drink))
        if coffee_maker.is_resource_sufficient(drink) == False:
            print("sorry there is not enough resources")
        print(money_machine.make_payment(drink.cost))
        coffee_maker.make_coffee(order=drink)
    

    
    
