"""Importuję moduł restaurant.py"""


from restaurant import Restaurant, IceCreamStand


my_icecream = IceCreamStand('U michałka', 'Kręcony')
my_icecream.describe_restaurant()
my_icecream.open_restaurant()
my_icecream.flavours_choose()

my_restaurant = Restaurant('KEBAB', 'Kręcioł')
my_restaurant.describe_restaurant()