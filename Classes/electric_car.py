from car_module import Car
class Battery:
    def __init__(self, battery_size=70):
        """Inicjalizaja atrybutów akumulatora"""
        self.battery_size = battery_size

    def describe_battery(self):
        """Wyświetlenie informacji o wielkości akumulatora"""
        print("\tTen samochód ma akumulator o pojemności " +
              str(self.battery_size) + " kWh.")

    def get_range(self):
        """
        Wyświetla info o zasięgu na podstawie pojemności akumulatora
        """
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        message = "Zasięgo tego samochodu wynosi około " + str(range)
        message += " km po pełnym naładowaniu baterii"
        print(message + "\n")


class ElectricCar(Car):
    """Przedstawia cechy charakterystyczne samochodu eletrycznego"""

    def __init__(self, make, model, year):
        """
        Inicjalizacja atrybutów klasy nadrzędnej
        Następnie inicijalizacja atrybutów charakterystycznych dla
        samochodu eletrycznego,
        """
        super().__init__(make, model, year)
        self.battery = Battery()

    def fill_gas_tank(self):
        """Samochód o napędzie el. nie ma zbiornika paliwa"""
        print("\tTen samochó nie wymaga tankowania paliwa!\n")


my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.tank_range = 300
my_tesla.fill_gas_tank()
my_tesla.battery.get_range()

my_bmw = Car('bmw', 'e87', 2009)
print(my_bmw.get_descriptive_name())
my_bmw.tank_range = 500
my_bmw.fill_gas_tank()
