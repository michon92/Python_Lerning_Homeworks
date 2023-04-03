class Car():
    """Prosta próba zaprazentowania samochodu"""
    def __init__(self, make, model, year):
        """Inicjalizacja atrybutów opisujących auto"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading =250000  # początkowa wartość przebiegu 


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


my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.update_odometer(130000)  # testujemy skrypt próbojąc cofnoąć licznik
my_new_car.road_odometer()