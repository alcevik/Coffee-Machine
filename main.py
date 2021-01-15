from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

#Print Report
#Check resources is_resource_sufficient
#Process Coins
#Check transaction is succesful 
#Make Coffee 

coffee_maker = CoffeeMaker()
menu = Menu()
money_machine = MoneyMachine()

is_on = True

while is_on:
  options = menu.get_items()
  choice = input(f"What would you like? {options}: ")
  if choice == 'off':
    is_on = False
  elif choice == 'report':
    coffee_maker.report()
    money_machine.report()
  else:
    drink = menu.find_drink(choice)
    is_resource_sufficient = coffee_maker.is_resource_sufficient(drink)
    is_payment_succesful = money_machine.make_payment(drink.cost)
    if is_payment_succesful and is_resource_sufficient:
      coffee_maker.make_coffee(drink)
