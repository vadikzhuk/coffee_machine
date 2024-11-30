from coffee_data import MENU, INITIAL_RESOURCES, COINS

class coffeeMachine():
    def __init__(self):
        self.funds = 0
        self.water = INITIAL_RESOURCES["water"]
        self.milk = INITIAL_RESOURCES["milk"]
        self.coffee = INITIAL_RESOURCES["coffee"]

        self.ordered_coffee = ""
        self.price = 0
        self.required_water = 0
        self.required_milk = 0
        self.required_coffee = 0

    def process_order(self, order):
        self.ordered_coffee = order
        if self.ordered_coffee in list(MENU.keys()):
            self.price = MENU[self.ordered_coffee]["cost"]
            self.required_water, self.required_milk, self.required_coffee = \
                MENU[order]["ingredients"]["water"], \
                MENU[order]["ingredients"]["milk"], \
                MENU[order]["ingredients"]["coffee"]
            return True
        print("That type of coffee is unknown. Choose from espresso/latte/cappuccino")
        return False

    def process_payment(self, order_availability):
        if order_availability:
            while self.price > 0:
                print(f"You have to pay ${self.price}")
                coin = input("Toss a coin (penny/nickel/dime/quarter/dollar/five):")
                if coin in list(COINS.keys()):
                    self.funds += COINS[coin]
                    self.price -= COINS[coin]
                else:
                    print("Wrong coin!")

            if self.price < 0:
                if self.funds >= self.price:
                    self.funds += self.price
                    print(f"Take your change: ${-self.price}")
                else:
                    print("Sorry, not enough money for change")

        return order_availability

    def check_availability(self, order_status):
        if order_status:
            missing_ingredients = []

            if self.water < self.required_water:
                missing_ingredients.append("water")
            if self.milk < self.required_milk:
                missing_ingredients.append("milk")
            if self.coffee < self.required_coffee:
                missing_ingredients.append("coffee")

            if len(missing_ingredients) == 0:
                return True

            print(f"Cannot brew coffee, missing {', '.join(missing_ingredients)}")
            return False
        return False

    def brew(self, order_availability):
        if order_availability:
            self.water -= self.required_water
            self.milk -= self.required_milk
            self.coffee -= self.required_coffee
            print(f"{self.ordered_coffee.capitalize()} brewed successfully!")

    def create_report(self):
        return f"""Ingredients left:
Water: {self.water}ml.;
Milk: {self.milk}ml.;
Coffee: {self.coffee}g.

Cash in machine: ${self.funds}"""

    def print_report(self):
        print(self.create_report())

    def reset_order_data(self):
        self.ordered_coffee = ""
        self.price = 0
        self.required_water = 0
        self.required_milk = 0
        self.required_coffee = 0

    def run_cycle(self):
        while True:
            order = input("Choose your coffee (espresso/latte/cappuccino):")

            match order:
                case "off":
                    del self
                    break
                case "report":
                    self.print_report()
                case _:
                    order_status = self.process_order(order)
                    order_availability = self.check_availability(order_status)
                    if order_availability:
                        self.process_payment(order_availability)
                        self.brew(order_availability)
                    self.reset_order_data()

            print("********************************")
