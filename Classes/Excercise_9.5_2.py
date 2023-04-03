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


    def set_number_served(self, number):
        self.number_served = number
        print("\tObsłużono " + str(self.number_served) + " gości.")
        

restaurant = Restaurant('dagrasso', 'włoski')
restaurant.describe_restaurant()
restaurant.open_restaurant()
restaurant.set_number_served(5)
