class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0


    def describe_restaurant(self):
        print(self.restaurant_name.upper() + " - restaurant name")
        print(self.cuisine_type.title() + " - cuisine week")
    

    def open_restaurant(self):
        print(self.restaurant_name.title() + " opens: 9-17 .")

    
    def number_of_served(self):
        """Bezpośrednia modyfikacja atrybutu"""
        print(str(self.number_served) + " clients today.")


restaurant = Restaurant('dagrasso', 'włoski')
restaurant.describe_restaurant()
restaurant.open_restaurant()
restaurant.number_served = 17
restaurant.number_of_served()