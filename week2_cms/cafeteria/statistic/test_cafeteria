import time


#gpt:
"""
This module takes coffee order
"""

RECIPE = {
        "espresso": {
            'espresso': 30},
        "latte": {
            'espresso': 60,
            'steamed_milk': 120, 
            'foamed_milk': 15},
        "macchiato": {
            'espresso': 60,
            'foamed_milk': 15},
        "flat white": {
            'espresso': 60,
            'steamed_milk': 120},
        "dopio": {
            'espresso': 60},
        "cappuccino": {
            'espresso': 60,
            'steamed_milk': 60, 
            'foamed_milk': 60},
        "lungo": {
            'espresso': 90},
        "cortado": {
            'espresso': 60,
            'steamed_milk': 60}
            }
class Track:
    """
    Tracks orders
    """
    MENU = {
        "espresso": 40,
        "latte": 70,
        "flat white": 70,
        "dopio": 50,
        "cappuccino": 60,
        "lungo": 50,
        "cortado": 55,
        "mocca": 60}
    __beans = 5000
    __milk = 20000
    safety = True

    def __init__(self, date):
        """
        Takes date
        """
        self.date = date
        self.orders = []
        self.__total_milk = 0
        self.__total_beans = 0

    def place_order(self, order):
        """
        Takes order
        """
        if not self.safety:
            return 'Unfortunately, now it is not safe to make coffee.'

        if not isinstance(order, Coffee):
            return "We can't create anything that is not a Coffee instance."

        order_name = order.name

        if order_name not in self.MENU:
            order.is_paid = False
            return "Unfortunately, we don't have such kind of coffee in the menu."

        order_milk = order.milk

        if order_milk > self.milk:
            return "Unfortunately, we don't have enough ingredients."

        order_price = self.MENU[order_name] * order.count
        order.price = order_price
        self.orders.append(order)
        order.is_paid = True

        self.__total_milk += order_milk
        self.__total_beans += round(order.espresso * 6 * 2 / 60)

        return 'Done!'

    def total_revenue(self):
        """
        Returns profit
        """
        return sum(i.price for i in self.orders)

    def total_milk(self):
        """"
        Amount of milk needed
        """
        return self.__total_milk

    def total_beans(self):
        """
        Amount of beans needed
        """
        return self.__total_beans

    @property
    def beans(self):
        """
        Amount of beans left
        """
        return self.__beans - self.total_beans()

    @property
    def milk(self):
        """
        Amount of milk left
        """
        if self.__milk - self.total_milk() <= 0:
            return 0
        return self.__milk - self.total_milk()

    def milk_spoil(self, amount):
        """
        Amount of spoiled milk
        """
        if self.__milk - amount < 0:
            self.__milk = 0
        else:
            self.__milk -= amount

    @classmethod
    def set_limit_milk(cls, limit):
        """
        Limit for milk usage
        """
        cls.__milk = limit

    @staticmethod
    def change_air_state():
        """
        Checks if air alarm
        """
        Track.safety = not Track.safety


class Coffee():
    """
    takes coffe order
    """
    _Coffee__recipe = {}
    name = ''
    is_paid = False
    def __init__(self, name, count = 1) -> None:
        """
        takes data
        """
        self.name = name
        self.count = count
        if self._Coffee__recipe and self.name in self._Coffee__recipe:
            self.is_paid = False
    @classmethod
    def set_recipe(cls, recipe):
        """
        sets recipe
        """
        cls._Coffee__recipe = recipe
        cls.is_paid = False
    def __str__(self):
        """
        Returns a string representation of the order state.
        """
        if self.is_paid:
            return f'Preparing {self.count} {self.name}...'
        if not self._Coffee__recipe:
            return 'Order cannot be created. Recipe has not been set.'
        if self.name not in self._Coffee__recipe:
            return "Order cannot be created. We don't have recipe for it."
        return f'Order "{self.count} {self.name}" is created.'

    def __repr__(self):
        """
        Returns a string representation of the order.
        """
        return f"{self.count} {self.name}"

    @property
    def espresso(self):
        """
        Calculates the amount of espresso needed.
        """
        return self._Coffee__recipe[self.name].get('espresso', 0) * self.count

    @property
    def milk(self):
        """
        Calculates the amount of milk needed.
        """
        foamed_milk = self._Coffee__recipe[self.name].get('foamed_milk', 0)
        steamed_milk = self._Coffee__recipe[self.name].get('steamed_milk', 0)
        return (foamed_milk + steamed_milk) * self.count

    def __eq__(self, other):
        """
        Checks if two orders are equal.
        """
        return self.name == other.name and self.count == other.count

class FlavorMixin:
    """
    A mixin to add flavors to orders.
    """
    def add_flavor(self, sugar=0, cinnamon=False, syrup=''):
        """
        Adds flavor to the order.
        """
        if self.is_paid:
            self.sugar = sugar * self.count
            self.cinammon = cinnamon
            self.syrup = syrup
            self.flavor = True
            return "Done!"
        else:
            return 'Please, pay for it.'


class CustomCoffee(Coffee, FlavorMixin):
    """
    Represents a custom coffee order.
    """
    def __init__(self, name, count=1) -> None:
        """
        Initializes a custom coffee order.
        """
        super().__init__(name)
        self.count = count
        self.name = name
        self.flavor = False

    def __str__(self):
        """
        Returns a string representation of the custom coffee order.
        """
        if self.flavor:
            if self.is_paid:
                flavor_description = ""
                if self.sugar > 0:
                    flavor_description += f"{self.sugar} stickers of sugar"
                if self.cinammon:
                    flavor_description += ", cinammon" if flavor_description else "cinammon"
                if self.syrup:
                    flavor_description += f", {self.syrup} syrup" if flavor_description else f"{self.syrup} syrup"
                return f"Your best {self.name} is ready! It has: {flavor_description}."
        if self.is_paid:
            return f'Preparing {self.count} {self.name}...'
        return f'Order "{self.count} custom {self.name}" is created.'

    def __repr__(self):
        """
        Returns a string representation of the custom coffee order.
        """
        return f"{self.count} custom {self.name}"

    def __eq__(self, other):
        """
        Compares two orders for equality.
        """
        if self.name == other.name and self.count == other.count:
            if isinstance(other, CustomCoffee):
                return self.flavor and self.sugar == other.sugar and \
                self.cinammon == other.cinammon and self.syrup == other.syrup
            if self.flavor:
                other.sugar = 0
                other.cinammon = False
                other.syrup = ''
            return not self.flavor
        return False

start = time.time()


RECIPE = {
        "espresso": {
            'espresso': 30},
        "latte": {
            'espresso': 60,
            'steamed_milk': 120, 
            'foamed_milk': 15},
        "macchiato": {
            'espresso': 60,
            'foamed_milk': 15},
        "flat white": {
            'espresso': 60,
            'steamed_milk': 120},
        "dopio": {
            'espresso': 60},
        "cappuccino": {
            'espresso': 60,
            'steamed_milk': 60, 
            'foamed_milk': 60},
        "lungo": {
            'espresso': 90},
        "cortado": {
            'espresso': 60,
            'steamed_milk': 60}
            }


print("Testing Cafeteria class...")
# We track the orders during the day
day_track = Track('07.02.2024')
day_track.date = '07.02.2024'
# Our cafeteria has a lot of different beverages in the menu and
# all of them are connected to coffee.
# The cafeteria use classical RECIPE that provided as a 
# constant.
order1 = Coffee('latte')
assert str(order1) == 'Order cannot be created. Recipe has not been set.'
# We need to set the recipe before creating the instances.
assert order1.__dict__ == {'name': 'latte', 'count': 1}
Coffee.set_recipe(RECIPE)
# A client can order only some kind of coffee.
order1 = Coffee('latte', 2)
assert order1.name == 'latte'
assert order1.count == 2
# also when the client ask for some order the is_paid attribute is
# created and it is False from the start.
assert order1.is_paid is False
# Coffee have three main ingredients that provide variety of the drinks:
# espresso, steamed milk and foamed milk. But on the side of the client we 
# provide only name of the drink and total amount of espresso
# and milk in ml.
assert order1.espresso == 120
assert order1.milk == 270
assert Coffee._Coffee__recipe[order1.name] == {'espresso': 60, 'steamed_milk': 120, 'foamed_milk': 15}
assert str(order1) == 'Order "2 latte" is created.'
#now we are ready to place this order
assert Track.MENU == {
    "espresso":  40,
    "latte": 70,
    "flat white": 70,
    "dopio":  50,
    "cappuccino":  60,
    "lungo": 50,
    "cortado": 55,
    "mocca": 60}
assert day_track.place_order(order1) == 'Done!'
assert order1.price == 140
assert order1.is_paid == True
assert str(order1) == 'Preparing 2 latte...'
assert len(day_track.orders) == 1
# it is possible that we have a coffee in recipe but 
# don't have in a menu
order2 = Coffee("macchiato")
assert str(order2) == 'Order "1 macchiato" is created.'
assert order2.__dict__ == {'name': 'macchiato', 'count': 1, 'is_paid': False}
assert day_track.place_order(order2) == "Unfortunately, we don't have such kind of coffee in the menu."
assert len(day_track.orders) == 1
order2 = Coffee("mocca")
assert str(order2) == "Order cannot be created. We don't have recipe for it."
assert order2.__dict__ == {'name': 'mocca', 'count': 1}
# Each customer can ask for adding sugar, cinammon or syrup 
# thus creating custom coffee.
order2 = CustomCoffee('cappuccino')
assert isinstance(order2, CustomCoffee)
assert isinstance(order2, Coffee)
assert isinstance(order2, FlavorMixin)
assert not isinstance(order1, CustomCoffee)
assert not isinstance(order1, FlavorMixin)
assert order2.name == 'cappuccino'
assert order2.count == 1
assert order2.espresso == 60
assert order2.milk == 120
assert order2.flavor == False
assert day_track.place_order(order2) == 'Done!'
assert len(day_track.orders) == 2
assert str(order2) == 'Preparing 1 cappuccino...'
assert order2.price == 60
assert order2.add_flavor(2, True, 'almond') == 'Done!'
assert order2.sugar == 2 #number of stickers
assert order2.cinammon == True #just to add some
assert order2.syrup == 'almond' #type of syrup
assert str(order2) == 'Your best cappuccino is ready! It has: 2 stickers of sugar, cinammon, almond syrup.'
#of course we track the orders
assert str(day_track.orders) == '[2 latte, 1 custom cappuccino]'
assert day_track.total_revenue() == 200
assert day_track.total_milk() == 390
#we need approx 6 grams of coffee beans to prepare 
# one espresso
assert day_track.total_beans() == 36
assert not isinstance(order2, Track)
# of course we have some reserves of milk and beans
# but they are limited. At the beginning of the day we usually
#have 20 litres of milk and 5 kg of beans
assert Track._Track__beans == 5000
assert Track._Track__milk == 20000
assert day_track.beans == 4964
assert day_track.milk == 19610
order3 = Coffee('Irish Coffee', 3)
# unfortunately we don't have this kind of drinks
# please let our customer know about it
assert day_track.orders == [order1, order2]
order3 = CustomCoffee('latte', 2)
assert order3 == order1
assert order3.add_flavor(3, False, 'green banana') == 'Please, pay for it.'
assert day_track.place_order(order3) == 'Done!'
assert order3.add_flavor(3, False, 'green banana') == 'Done!'
assert order3.sugar == 6
assert str(order3) == 'Your best latte is ready! It has: 6 stickers of sugar, green banana syrup.'
assert order3 != order1

# Sometimes we have situation when the milk spoiled
# in grams
day_track.milk_spoil(19340)
assert day_track.milk == 0
order4 = Coffee('latte', 2)
assert day_track.place_order(order4) == "Unfortunately, we don't have enough ingredients."
assert len(day_track.orders) == 3
#oneday our founder bought new fridge
# and we can store more milk
Track.set_limit_milk(30000)
assert Track._Track__milk == 30000


order5 = "Coffee"
assert not isinstance(order5, CustomCoffee)
assert day_track.place_order(order5) == "We can't create anything that is not a Coffee instance."
#and sure we don't work in air alert time
Track.change_air_state()
assert Track.safety == False
order6 = CustomCoffee('lungo', 2)
assert day_track.place_order(order6) == 'Unfortunately, now it is not safe to make coffee.'
Track.change_air_state()
assert Track.safety == True
order6 = CustomCoffee('lungo')
assert str(order6) == 'Order "1 custom lungo" is created.'
assert day_track.place_order(order6) == 'Done!'
assert day_track.total_revenue() ==  390
assert day_track.total_milk() == 660
assert day_track.total_beans() == 78
print('Done!')

end = time.time()

print((end - start)*5000000)

#time = 4806.5185546875



#Blackbox:

class Track():
    """
    Tracks orders
    """
    MENU = {
        "espresso":  40,
        "latte": 70,
        "flat white": 70,
        "dopio":  50,
        "cappuccino":  60,
        "lungo": 50,
        "cortado": 55,
        "mocca": 60}
    _Track__beans = 5000
    _Track__milk = 20000
    safety = True
    def __init__(self, date) -> None:
        """
        takes date
        """
        self.date = date
        self.orders = []

    def place_order(self, order):
        """
        Takes an order object and processes it if it's safe to make coffee.
        """
        if not self.safety:
            return "Unfortunately, now it is not safe to make coffee."

        if not isinstance(order, Coffee):
            return "We can't create anything that is not a Coffee instance."

        if order.name not in self.MENU:
            order.is_paid = False
            return "Unfortunately, we don't have such kind of coffee in the menu."

        if order.milk > self.milk:
            return "Unfortunately, we don't have enough ingredients."

        order.price = self.MENU[order.name] * order.count
        self.orders.append(order)
        order.is_paid = True
        return 'Done!'
    def total_revenue(self):
        """
        returns profit
        """
        return sum((i.price for i in self.orders))
    def total_milk(self):
        """"
        amount of milk needed
        """
        return sum((i.milk for i in self.orders))
    def total_beans(self):
        """
        Calculates the total amount of coffee beans needed for all orders.
        """
        return sum((round(i.espresso*6*2/60) for i in self.orders))
    @property
    def beans(self):
        """
        amount of beans left
        """
        return  self._Track__beans - self.total_beans()
    @property
    def milk(self):
        """
        amount of milk left
        """
        if self._Track__milk - self.total_milk() <= 0:
            return 0
        return  self._Track__milk - self.total_milk()
    def milk_spoil(self, amount):
        """
        Spoils the specified amount of milk.
        """
        if self._Track__milk - amount < 0:
            self._Track__milk = 0
        else:
            self._Track__milk -=  amount
    @classmethod
    def set_limit_milk(cls, lim):
        """
        liit for milk usage
        """
        cls._Track__milk = lim
    @staticmethod
    def change_air_state():
        """
        Toggles the air alarm state.
        """
        Track.safety = not Track.safety

class Coffee():
    """
    takes coffe order
    """
    _Coffee__recipe = {}
    name = ''
    is_paid = False
    def __init__(self, name, count = 1) -> None:
        """
        takes data
        """
        self.name = name
        self.count = count
        if self._Coffee__recipe and self.name in self._Coffee__recipe:
            self.is_paid = False
    @classmethod
    def set_recipe(cls, recipe):
        """
        sets recipe
        """
        cls._Coffee__recipe = recipe
        cls.is_paid = False
    def __str__(self):
        """
        Returns a string representation of the coffee order.
        """
        if self.is_paid:
            return f'Preparing {self.count} {self.name}...'
        if not self._Coffee__recipe:
            return 'Order cannot be created. Recipe has not been set.'
        if self.name not in self._Coffee__recipe:
            return "Order cannot be created. We don't have recipe for it."
        return f'Order "{self.count} {self.name}" is created.'
    def __repr__(self):
        """
        prints name of order
        """
        return f"{self.count} {self.name}"
    @property
    def espresso(self):
        """
        checks how much espresso need
        """
        return self._Coffee__recipe[self.name]['espresso']*self.count
    @property
    def milk(self):
        """
        Calculates the amount of milk needed for the order.
        """
        total_milk = 0
        for ingredient, quantity in self._Coffee__recipe[self.name].items():
            if 'milk' in ingredient:
                total_milk += quantity * self.count
        return total_milk
    def __eq__(self, other):
        """
        Compares two coffee orders for equality.
        """
        return self.name is other.name and self.count is other.count

class FlavorMixin:
    """
    add flavors
    """
    def add_flavor(self, sugar, cinammon , syrup):
        """
        adds flavor
        """
        if self.is_paid:
            self.sugar = sugar*self.count
            self.cinammon = cinammon
            self.syrup = syrup
            self.flavor = True
            return "Done!"
        return 'Please, pay for it.'

class CustomCoffee(Coffee, FlavorMixin):
    """
    takes custom coffe order
    """
    def __init__(self, name, count = 1) -> None:
        """
        take data
        """
        super().__init__(name)
        self.count = count
        self.name = name
        self.flavor = False
    def __str__(self):
        """
        Prints a string representation of the coffee order.
        """
        if self.flavor:
            if self.is_paid:
                if self.cinammon and self.sugar > 0 and self.syrup:
                    line =  f"Your best {self.name} is ready! It has: {self.sugar} \
stickers of sugar, cinammon, {self.syrup} syrup."
                if not self.cinammon and self.sugar > 0 and self.syrup:
                    line = f"Your best {self.name} is ready! It has: \
{self.sugar} stickers of sugar, {self.syrup} syrup."
                if self.cinammon and self.sugar > 0 and not self.syrup:
                    line =  f"Your best {self.name} is ready! It has: \
{self.sugar} stickers of sugar, cinammon."
                if self.cinammon and self.sugar == 0 and self.syrup :
                    line = f"Your best {self.name} is ready! It has: cinammon, {self.syrup} syrup."
                if self.cinammon and self.sugar == 0 and self.syrup == '' :
                    line =  f"Your best {self.name} is ready! It has: cinammon."
                if not self.cinammon and self.sugar == 0 and self.syrup != '' :
                    line = f"Your best {self.name} is ready! It has: {self.syrup} syrup."
                if not self.cinammon and self.sugar > 0 and self.syrup == '' :
                    line =  f"Your best {self.name} is ready! It has: \
{self.sugar} stickers of sugar."
                return line
        if self.is_paid:
            return f'Preparing {self.count} {self.name}...'
        return f'Order "{self.count} custom {self.name}" is created.'
    def __repr__(self):
        """
        prints order
        """
        return f"{self.count} custom {self.name}"
    def __eq__(self, other):
        """
        Compares two coffee orders for equality.
        """
        if self.name != other.name or self.count != other.count:
            return False
        if not self.flavor and not isinstance(other, CustomCoffee):
            return True
        if not isinstance(other, CustomCoffee) and self.flavor:
            other.__dict__.update(sugar=0, cinammon=False, syrup='')
        return self.flavor and self.sugar == other.sugar and self.cinammon == other.cinammon and self.syrup == other.syrup


start = time.time()


RECIPE = {
        "espresso": {
            'espresso': 30},
        "latte": {
            'espresso': 60,
            'steamed_milk': 120, 
            'foamed_milk': 15},
        "macchiato": {
            'espresso': 60,
            'foamed_milk': 15},
        "flat white": {
            'espresso': 60,
            'steamed_milk': 120},
        "dopio": {
            'espresso': 60},
        "cappuccino": {
            'espresso': 60,
            'steamed_milk': 60, 
            'foamed_milk': 60},
        "lungo": {
            'espresso': 90},
        "cortado": {
            'espresso': 60,
            'steamed_milk': 60}
            }


print("Testing Cafeteria class...")
# We track the orders during the day
day_track = Track('07.02.2024')
day_track.date = '07.02.2024'
# Our cafeteria has a lot of different beverages in the menu and
# all of them are connected to coffee.
# The cafeteria use classical RECIPE that provided as a 
# constant.
order1 = Coffee('latte')
assert str(order1) == 'Order cannot be created. Recipe has not been set.'
# We need to set the recipe before creating the instances.
assert order1.__dict__ == {'name': 'latte', 'count': 1}
Coffee.set_recipe(RECIPE)
# A client can order only some kind of coffee.
order1 = Coffee('latte', 2)
assert order1.name == 'latte'
assert order1.count == 2
# also when the client ask for some order the is_paid attribute is
# created and it is False from the start.
assert order1.is_paid is False
# Coffee have three main ingredients that provide variety of the drinks:
# espresso, steamed milk and foamed milk. But on the side of the client we 
# provide only name of the drink and total amount of espresso
# and milk in ml.
assert order1.espresso == 120
assert order1.milk == 270
assert Coffee._Coffee__recipe[order1.name] == {'espresso': 60, 'steamed_milk': 120, 'foamed_milk': 15}
assert str(order1) == 'Order "2 latte" is created.'
#now we are ready to place this order
assert Track.MENU == {
    "espresso":  40,
    "latte": 70,
    "flat white": 70,
    "dopio":  50,
    "cappuccino":  60,
    "lungo": 50,
    "cortado": 55,
    "mocca": 60}
assert day_track.place_order(order1) == 'Done!'
assert order1.price == 140
assert order1.is_paid == True
assert str(order1) == 'Preparing 2 latte...'
assert len(day_track.orders) == 1
# it is possible that we have a coffee in recipe but 
# don't have in a menu
order2 = Coffee("macchiato")
assert str(order2) == 'Order "1 macchiato" is created.'
assert order2.__dict__ == {'name': 'macchiato', 'count': 1, 'is_paid': False}
assert day_track.place_order(order2) == "Unfortunately, we don't have such kind of coffee in the menu."
assert len(day_track.orders) == 1
order2 = Coffee("mocca")
assert str(order2) == "Order cannot be created. We don't have recipe for it."
assert order2.__dict__ == {'name': 'mocca', 'count': 1}
# Each customer can ask for adding sugar, cinammon or syrup 
# thus creating custom coffee.
order2 = CustomCoffee('cappuccino')
assert isinstance(order2, CustomCoffee)
assert isinstance(order2, Coffee)
assert isinstance(order2, FlavorMixin)
assert not isinstance(order1, CustomCoffee)
assert not isinstance(order1, FlavorMixin)
assert order2.name == 'cappuccino'
assert order2.count == 1
assert order2.espresso == 60
assert order2.milk == 120
assert order2.flavor == False
assert day_track.place_order(order2) == 'Done!'
assert len(day_track.orders) == 2
assert str(order2) == 'Preparing 1 cappuccino...'
assert order2.price == 60
assert order2.add_flavor(2, True, 'almond') == 'Done!'
assert order2.sugar == 2 #number of stickers
assert order2.cinammon == True #just to add some
assert order2.syrup == 'almond' #type of syrup
assert str(order2) == 'Your best cappuccino is ready! It has: 2 stickers of sugar, cinammon, almond syrup.'
#of course we track the orders
assert str(day_track.orders) == '[2 latte, 1 custom cappuccino]'
assert day_track.total_revenue() == 200
assert day_track.total_milk() == 390
#we need approx 6 grams of coffee beans to prepare 
# one espresso
assert day_track.total_beans() == 36
assert not isinstance(order2, Track)
# of course we have some reserves of milk and beans
# but they are limited. At the beginning of the day we usually
#have 20 litres of milk and 5 kg of beans
assert Track._Track__beans == 5000
assert Track._Track__milk == 20000
assert day_track.beans == 4964
assert day_track.milk == 19610
order3 = Coffee('Irish Coffee', 3)
# unfortunately we don't have this kind of drinks
# please let our customer know about it
assert day_track.orders == [order1, order2]
order3 = CustomCoffee('latte', 2)
assert order3 == order1
assert order3.add_flavor(3, False, 'green banana') == 'Please, pay for it.'
assert day_track.place_order(order3) == 'Done!'
assert order3.add_flavor(3, False, 'green banana') == 'Done!'
assert order3.sugar == 6
assert str(order3) == 'Your best latte is ready! It has: 6 stickers of sugar, green banana syrup.'
assert order3 != order1

# Sometimes we have situation when the milk spoiled
# in grams
day_track.milk_spoil(19340)
assert day_track.milk == 0
order4 = Coffee('latte', 2)
assert day_track.place_order(order4) == "Unfortunately, we don't have enough ingredients."
assert len(day_track.orders) == 3
#oneday our founder bought new fridge
# and we can store more milk
Track.set_limit_milk(30000)
assert Track._Track__milk == 30000


order5 = "Coffee"
assert not isinstance(order5, CustomCoffee)
assert day_track.place_order(order5) == "We can't create anything that is not a Coffee instance."
#and sure we don't work in air alert time
Track.change_air_state()
assert Track.safety == False
order6 = CustomCoffee('lungo', 2)
assert day_track.place_order(order6) == 'Unfortunately, now it is not safe to make coffee.'
Track.change_air_state()
assert Track.safety == True
order6 = CustomCoffee('lungo')
assert str(order6) == 'Order "1 custom lungo" is created.'
assert day_track.place_order(order6) == 'Done!'
assert day_track.total_revenue() ==  390
assert day_track.total_milk() == 660
assert day_track.total_beans() == 78
print('Done!')

end = time.time()

print((end - start)*5000000)

#time = 5011.558532714844




#my code:
"""
This module takes coffee order
"""

RECIPE = {
        "espresso": {
            'espresso': 30},
        "latte": {
            'espresso': 60,
            'steamed_milk': 120, 
            'foamed_milk': 15},
        "macchiato": {
            'espresso': 60,
            'foamed_milk': 15},
        "flat white": {
            'espresso': 60,
            'steamed_milk': 120},
        "dopio": {
            'espresso': 60},
        "cappuccino": {
            'espresso': 60,
            'steamed_milk': 60, 
            'foamed_milk': 60},
        "lungo": {
            'espresso': 90},
        "cortado": {
            'espresso': 60,
            'steamed_milk': 60}
            }

class Track():
    """
    Tracks orders
    """
    MENU = {
        "espresso":  40,
        "latte": 70,
        "flat white": 70,
        "dopio":  50,
        "cappuccino":  60,
        "lungo": 50,
        "cortado": 55,
        "mocca": 60}
    _Track__beans = 5000
    _Track__milk = 20000
    safety = True
    def __init__(self, date) -> None:
        """
        takes date
        """
        self.date = date
        self.orders = []
    def place_order(self, order):
        """
        takes order
        """
        if self.safety is False:
            return 'Unfortunately, now it is not safe to make coffee.'
        if not isinstance(order, Coffee):
            return "We can't create anything that is not a Coffee instance."
        if order.name not in self.MENU:
            order.is_paid = False
            return "Unfortunately, we don't have such kind of coffee in the menu."
        if order.milk > self.milk:
            return "Unfortunately, we don't have enough ingredients."
        order.price = Track.MENU[order.name]*order.count
        self.orders.append(order)
        order.is_paid = True
        return 'Done!'
    def total_revenue(self):
        """
        returns profit
        """
        return sum((i.price for i in self.orders))
    def total_milk(self):
        """"
        amount of milk needed
        """
        return sum((i.milk for i in self.orders))
    def total_beans(self):
        """
        amount of beans needed
        """
        return sum((round(i.espresso*6*2/60) for i in self.orders))
    @property
    def beans(self):
        """
        amount of beans left
        """
        return  self._Track__beans - self.total_beans()
    @property
    def milk(self):
        """
        amount of milk left
        """
        if self._Track__milk - self.total_milk() <= 0:
            return 0
        return  self._Track__milk - self.total_milk()
    def milk_spoil(self, a):
        """
        amount of spoiled milk
        """
        if self._Track__milk - a < 0:
            self._Track__milk = 0
        else:
            self._Track__milk = self._Track__milk - a
    @classmethod
    def set_limit_milk(cls, lim):
        """
        liit for milk usage
        """
        cls._Track__milk = lim
    @staticmethod
    def change_air_state():
        """
        checks if air alarm
        """
        if Track.safety is True:
            Track.safety = False
        else:
            Track.safety = True

class Coffee():
    """
    takes coffe order
    """
    _Coffee__recipe = {}
    name = ''
    is_paid = False
    def __init__(self, name, count = 1) -> None:
        """
        takes data
        """
        self.name = name
        self.count = count
        if self._Coffee__recipe and self.name in self._Coffee__recipe:
            self.is_paid = False
    @classmethod
    def set_recipe(cls, recipe):
        """
        sets recipe
        """
        cls._Coffee__recipe = recipe
        cls.is_paid = False
    def __str__(self):
        """
        prints a state of order
        """
        if self.is_paid is True:
            return f'Preparing {self.count} {self.name}...'
        if not self._Coffee__recipe:
            return 'Order cannot be created. Recipe has not been set.'
        if self.name not in self._Coffee__recipe:
            return "Order cannot be created. We don't have recipe for it."
        return f'Order "{self.count} {self.name}" is created.'
    def __repr__(self):
        """
        prints name of order
        """
        return f"{self.count} {self.name}"
    @property
    def espresso(self):
        """
        checks how much espresso need
        """
        return self._Coffee__recipe[self.name]['espresso']*self.count
    @property
    def milk(self):
        """
        checks how much milk needed
        """
        res = 0
        if 'foamed_milk' in self._Coffee__recipe[self.name]:
            res += self._Coffee__recipe[self.name]['foamed_milk']*self.count
        if 'steamed_milk' in self._Coffee__recipe[self.name]:
            res += self._Coffee__recipe[self.name]['steamed_milk']*self.count
        return res
    def __eq__(self, other):
        """
        compares 2 orders
        """
        if self.name == other.name and self.count == other.count:
            return True
        return False

class FlavorMixin:
    """
    add flavors
    """
    def add_flavor(self, sugar, cinammon , syrup):
        """
        adds flavor
        """
        if self.is_paid is True:
            self.sugar = sugar*self.count
            self.cinammon = cinammon
            self.syrup = syrup
            self.flavor = True
            return "Done!"
        return 'Please, pay for it.'

class CustomCoffee(Coffee, FlavorMixin):
    """
    takes custom coffe order
    """
    def __init__(self, name, count = 1) -> None:
        """
        take data
        """
        super().__init__(name)
        self.count = count
        self.name = name
        self.flavor = False
    def __str__(self):
        """
        prints added flavors
        """
        if self.flavor is True:
            if self.is_paid is True:
                if self.cinammon is True and self.sugar > 0 and self.syrup != '' :
                    line =  f"Your best {self.name} is ready! It has: {self.sugar} \
stickers of sugar, cinammon, {self.syrup} syrup."
                if self.cinammon is False and self.sugar > 0 and self.syrup != '':
                    line = f"Your best {self.name} is ready! It has: \
{self.sugar} stickers of sugar, {self.syrup} syrup."
                if self.cinammon is True and self.sugar > 0 and self.syrup == '':
                    line =  f"Your best {self.name} is ready! It has: \
{self.sugar} stickers of sugar, cinammon."
                if self.cinammon is True and self.sugar == 0 and self.syrup != '' :
                    line = f"Your best {self.name} is ready! It has: cinammon, {self.syrup} syrup."
                if self.cinammon is True and self.sugar == 0 and self.syrup == '' :
                    line =  f"Your best {self.name} is ready! It has: cinammon."
                if self.cinammon is False and self.sugar == 0 and self.syrup != '' :
                    line = f"Your best {self.name} is ready! It has: {self.syrup} syrup."
                if self.cinammon is False and self.sugar > 0 and self.syrup == '' :
                    line =  f"Your best {self.name} is ready! It has: \
{self.sugar} stickers of sugar."
                return line
        if self.is_paid is True:
            return f'Preparing {self.count} {self.name}...'
        return f'Order "{self.count} custom {self.name}" is created.'
    def __repr__(self):
        """
        prints order
        """
        return f"{self.count} custom {self.name}"
    def __eq__(self, other):
        """
        compares 2 orders
        """
        if self.name == other.name and self.count == other.count:
            if self.flavor is False and not isinstance(other, CustomCoffee):
                return True
            if not isinstance(other, CustomCoffee) and self.flavor is True:
                other.sugar = 0
                other.cinammon = False
                other.syrup = ''
            if self.flavor is True and self.sugar == other.sugar and \
                self.cinammon == other.cinammon and self.syrup == other.syrup:
                return True
        return False





start = time.time()


RECIPE = {
        "espresso": {
            'espresso': 30},
        "latte": {
            'espresso': 60,
            'steamed_milk': 120, 
            'foamed_milk': 15},
        "macchiato": {
            'espresso': 60,
            'foamed_milk': 15},
        "flat white": {
            'espresso': 60,
            'steamed_milk': 120},
        "dopio": {
            'espresso': 60},
        "cappuccino": {
            'espresso': 60,
            'steamed_milk': 60, 
            'foamed_milk': 60},
        "lungo": {
            'espresso': 90},
        "cortado": {
            'espresso': 60,
            'steamed_milk': 60}
            }


print("Testing Cafeteria class...")
# We track the orders during the day
day_track = Track('07.02.2024')
day_track.date = '07.02.2024'
# Our cafeteria has a lot of different beverages in the menu and
# all of them are connected to coffee.
# The cafeteria use classical RECIPE that provided as a 
# constant.
order1 = Coffee('latte')
assert str(order1) == 'Order cannot be created. Recipe has not been set.'
# We need to set the recipe before creating the instances.
assert order1.__dict__ == {'name': 'latte', 'count': 1}
Coffee.set_recipe(RECIPE)
# A client can order only some kind of coffee.
order1 = Coffee('latte', 2)
assert order1.name == 'latte'
assert order1.count == 2
# also when the client ask for some order the is_paid attribute is
# created and it is False from the start.
assert order1.is_paid is False
# Coffee have three main ingredients that provide variety of the drinks:
# espresso, steamed milk and foamed milk. But on the side of the client we 
# provide only name of the drink and total amount of espresso
# and milk in ml.
assert order1.espresso == 120
assert order1.milk == 270
assert Coffee._Coffee__recipe[order1.name] == {'espresso': 60, 'steamed_milk': 120, 'foamed_milk': 15}
assert str(order1) == 'Order "2 latte" is created.'
#now we are ready to place this order
assert Track.MENU == {
    "espresso":  40,
    "latte": 70,
    "flat white": 70,
    "dopio":  50,
    "cappuccino":  60,
    "lungo": 50,
    "cortado": 55,
    "mocca": 60}
assert day_track.place_order(order1) == 'Done!'
assert order1.price == 140
assert order1.is_paid == True
assert str(order1) == 'Preparing 2 latte...'
assert len(day_track.orders) == 1
# it is possible that we have a coffee in recipe but 
# don't have in a menu
order2 = Coffee("macchiato")
assert str(order2) == 'Order "1 macchiato" is created.'
assert order2.__dict__ == {'name': 'macchiato', 'count': 1, 'is_paid': False}
assert day_track.place_order(order2) == "Unfortunately, we don't have such kind of coffee in the menu."
assert len(day_track.orders) == 1
order2 = Coffee("mocca")
assert str(order2) == "Order cannot be created. We don't have recipe for it."
assert order2.__dict__ == {'name': 'mocca', 'count': 1}
# Each customer can ask for adding sugar, cinammon or syrup 
# thus creating custom coffee.
order2 = CustomCoffee('cappuccino')
assert isinstance(order2, CustomCoffee)
assert isinstance(order2, Coffee)
assert isinstance(order2, FlavorMixin)
assert not isinstance(order1, CustomCoffee)
assert not isinstance(order1, FlavorMixin)
assert order2.name == 'cappuccino'
assert order2.count == 1
assert order2.espresso == 60
assert order2.milk == 120
assert order2.flavor == False
assert day_track.place_order(order2) == 'Done!'
assert len(day_track.orders) == 2
assert str(order2) == 'Preparing 1 cappuccino...'
assert order2.price == 60
assert order2.add_flavor(2, True, 'almond') == 'Done!'
assert order2.sugar == 2 #number of stickers
assert order2.cinammon == True #just to add some
assert order2.syrup == 'almond' #type of syrup
assert str(order2) == 'Your best cappuccino is ready! It has: 2 stickers of sugar, cinammon, almond syrup.'
#of course we track the orders
assert str(day_track.orders) == '[2 latte, 1 custom cappuccino]'
assert day_track.total_revenue() == 200
assert day_track.total_milk() == 390
#we need approx 6 grams of coffee beans to prepare 
# one espresso
assert day_track.total_beans() == 36
assert not isinstance(order2, Track)
# of course we have some reserves of milk and beans
# but they are limited. At the beginning of the day we usually
#have 20 litres of milk and 5 kg of beans
assert Track._Track__beans == 5000
assert Track._Track__milk == 20000
assert day_track.beans == 4964
assert day_track.milk == 19610
order3 = Coffee('Irish Coffee', 3)
# unfortunately we don't have this kind of drinks
# please let our customer know about it
assert day_track.orders == [order1, order2]
order3 = CustomCoffee('latte', 2)
assert order3 == order1
assert order3.add_flavor(3, False, 'green banana') == 'Please, pay for it.'
assert day_track.place_order(order3) == 'Done!'
assert order3.add_flavor(3, False, 'green banana') == 'Done!'
assert order3.sugar == 6
assert str(order3) == 'Your best latte is ready! It has: 6 stickers of sugar, green banana syrup.'
assert order3 != order1

# Sometimes we have situation when the milk spoiled
# in grams
day_track.milk_spoil(19340)
assert day_track.milk == 0
order4 = Coffee('latte', 2)
assert day_track.place_order(order4) == "Unfortunately, we don't have enough ingredients."
assert len(day_track.orders) == 3
#oneday our founder bought new fridge
# and we can store more milk
Track.set_limit_milk(30000)
assert Track._Track__milk == 30000


order5 = "Coffee"
assert not isinstance(order5, CustomCoffee)
assert day_track.place_order(order5) == "We can't create anything that is not a Coffee instance."
#and sure we don't work in air alert time
Track.change_air_state()
assert Track.safety == False
order6 = CustomCoffee('lungo', 2)
assert day_track.place_order(order6) == 'Unfortunately, now it is not safe to make coffee.'
Track.change_air_state()
assert Track.safety == True
order6 = CustomCoffee('lungo')
assert str(order6) == 'Order "1 custom lungo" is created.'
assert day_track.place_order(order6) == 'Done!'
assert day_track.total_revenue() ==  390
assert day_track.total_milk() == 660
assert day_track.total_beans() == 78
print('Done!')

end = time.time()

print((end - start)*5000000)

#time = 5393.028259277344
