import sys

# TODO: Turn off the Coffee Machine by entering “ off ” to the prompt.

# TODO: Print report.
class CoffeeMachine:
    # class variables
    latte = { "Water" : 200,
            "Milk": 150,
            "Coffee" : 24 }

    cappuccino = {"Water": 250,
             "Milk": 100,
             "Coffee": 24}

    espresso = {"Water": 50,
             "Milk": 0,
             "Coffee": 18}

    menu = {'latte': latte,
            'cappuccino': cappuccino,
            'espresso' : espresso}
    price = {'latte': 2.5,
             'cappuccino': 2.50,
             'espresso' : 2.50}

    def __init__(self, water, milk, coffee, money):
        self.resource = { "Water" : water,
                          "Milk": milk,
                          "Coffee" : coffee }
        self.money = money
        self.prompt = ''
        self.money_input = 0.00

    def process_prompt(self):
        if self.prompt == 'off':
            sys.exit()
        elif self.prompt == 'report':
            self.report()
        elif self.prompt in ('latte','cappuccino','espresso'):
            if self.check_resources():
                self.process_coins()
                if self.transaction():
                    self.make_coffee()

    def process_coins(self):
        print("Please insert coins.")
        Quarters = int(input("Enter number of Quarters: "))
        Dimes = int(input("Enter number of Dimes: "))
        Nickles = int(input("Enter number of Nickles: "))
        Pennies = int(input("Enter number of Pennies: "))
        self.money_input = (0.25*Quarters) +(0.1*Dimes) + (0.05*Nickles) + (0.01*Pennies)

    def transaction(self):
        if self.price[self.prompt]>=self.money_input:
            print("Sorry that's not enough money. Money refunded.")
            self.money_input=0
            return False
        elif self.price[self.prompt]<=self.money_input:
            self.money+=self.money_input
            if self.price[self.prompt] < self.money_input:
                print("Here is $", round((self.money_input - self.price[self.prompt]),2)," dollars in change.")
            self.money_input=0
            return True

    def make_coffee(self):
        for k, v in self.resource.items():
            self.resource[k] -= self.menu[self.prompt][k]
        print("Here is your ", self.prompt, ". Enjoy!")

    def on(self):
        self.prompt = input("What would you like? (espresso/latte/cappuccino)").lower()
        self.process_prompt()

    def check_resources(self):
            for k,v in self.resource.items():
                if self.resource[k]< self.menu[self.prompt.lower()][k]:
                    print("Sorry there is not enough ", k)
                    return False
            print("There is enough resources")
            return True

    def report(self):
        print("Water: ", self.resource['water'], "ml")
        print("Milk: ", self.resource['milk'], "ml")
        print("Coffee: ", self.resource['coffee'], "g")
        print("Money: $", self.money)



Nescafe = CoffeeMachine(1000,1000,1000,20)

Nescafe.on()