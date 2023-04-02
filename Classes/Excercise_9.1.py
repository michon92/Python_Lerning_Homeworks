class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type


    def describe_restaurant(self):
        print(self.restaurant_name.upper() + " - restaurant name")
        print(self.cuisine_type.title() + " - cuisine week")
    

    def open_restaurant(self):
        print(self.restaurant_name.title() + " open: 9-17 .")


restaurant = Restaurant('name', 'type')
restaurant.describe_restaurant()
restaurant.open_restaurant()


    
    

