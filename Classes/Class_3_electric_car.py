class Car():
    """Prosta próba zaprazentowania samochodu"""
    def __init__(self, make, model, year):
        """Inicjalizacja atrybutów opisujących auto"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading =250000  # początkowa wartość przebiegu 
        self.tank_range = 700


    def get_descriptive_name(self):
        """Zwrot elegancko sformatowanego opisu samochodu"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    

    def road_odometer(self):
        """Wyświetla info o przebiegu samochodu"""
        print("\tTen samochód ma przejechane " + str(self.odometer_reading) + " km.")

    
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
        
    

class ElectricCar(Car):
    """Przedstawia cechy charakterystyczne samochodu eletrycznego"""
    def __init__(self, make, model, year):
        """
        Inicjalizacja atrybutów klasy nadrzędnej
        Następnie inicijalizacja atrybutów charakterystycznych dla
        samochodu eletrycznego,
        """
        super().__init__(make, model, year)
        self.battery_size = 70

    def describe_battery(self):
        """Wyświetla info o wielkości zainstalowanego akumulatora"""
        print("\tTen samochód ma akumulator o pojemności " + 
              str(self.battery_size) + " kWh.")
        
    def fill_gas_tank(self):
        """Samochód o napędzie el. nie ma zbiornika paliwa"""
        print("Ten samochó nie wymaga tankowania paliwa!")



my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()
my_tesla.fill_gas_tank()

my_bmw = Car('bmw', 'e87', 2009)
print(my_bmw.get_descriptive_name())
my_bmw.fill_gas_tank()
