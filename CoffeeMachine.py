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

    def __init__(self, water, milk, coffee, money):
        self.resource = { "Water" : water,
                          "Milk": milk,
                          "Coffee" : coffee }
        self.money = money
        self.prompt = ''

    def process_prompt(self, prompt):
        if prompt == 'off':
            sys.exit()
        elif prompt == 'report':
            self.report()
        elif prompt.lower in ('latte','cappuccino','espresso'):
            if self.check_resources(self, prompt):
                self.process_coins()
                if self.transaction():
                    self.make_coffee(prompt)

    def process_coins(self):
        return True

    def transaction(self):
        return True

    def make_coffee(self, prompt):
        print("Here is your ", prompt, ". Enjoy!")

    def on(self):
        self.prompt = input("What would you like? (expresso/latte/cappuccino)")

    def check_resources(self, prompt):
            for k,v in self.resource:
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
prompt = input("What would you like? (expresso/latte/cappuccino)")

prompt = prompt.lower()

