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