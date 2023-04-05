"""In this excersise we will upgrade battery capacity"""


class Car:
    """Prosta próba zaprazentowania samochodu - gotowy moduł"""

    def __init__(self, make, model, year):
        """Inicjalizacja atrybutów opisujących auto"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 250000  # początkowa wartość przebiegu
        self.tank_range = 700

    def get_descriptive_name(self):
        """Zwrot elegancko sformatowanego opisu samochodu"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def road_odometer(self):
        """Wyświetla info o przebiegu samochodu"""
        print("\tTen samochód ma przejechane " +
              str(self.odometer_reading) + " km.")

    def update_odometer(self, mileage):
        """Przypisanie danej wartości licznikowi przebiegu auta.
        Zmiana zostanie odrzócona w przypadku próby cofnięcia licznika!
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("Nie można cofać licznika !!!")

    def fill_gas_tank(self):
        print("Fuell range " + str(self.tank_range))


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

    def upgrade_battery(self):
        if self.battery_size != 85:
            self.battery_size = 85
            print("Upgrade baterii w toku ;)")


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


my_tesla = ElectricCar('tesla', 'model', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.upgrade_battery()
my_tesla.battery.describe_battery()
