"""Moduł Restaurant i IceCreamStand na potrzeby Zadania9.10"""


class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 15

    def describe_restaurant(self):
        print(self.restaurant_name.upper() + " - restaurant name")
        print(self.cuisine_type.title() + " - cuisine week")

    def open_restaurant(self):
        print(self.restaurant_name.title() + " opens: 9-17 .")

    def served(self):
        print("\tObsłużono " + str(self.number_served) + " gości.")

    def increment_number_served(self, numbers_clients):
        self.number_served += numbers_clients


class IceCreamStand(Restaurant):
    """Budka z lodamu"""
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavours = ['malinka', 'śmietanka', 'czekoladka',
                         'śmietanka ze skałki']

    def flavours_choose(self):
        print("\nDostępne smaki:")
        for flavour in self.flavours:
            print("\t" + flavour.title())
