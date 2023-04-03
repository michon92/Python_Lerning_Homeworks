class Car():
    """Prosta próba zaprazentowania samochodu"""
    def __init__(self, make, model, year):
        """Inicjalizacja atrybutów opisujących auto"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0  # początkowa wartość przebiegu 


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


    def increment_odometer(self, kilometers):
        """Inkrementacja wartości licznika przebiegu samochodu o podaną wartość"""
        self.odometer_reading += kilometers


my_used_car = Car('subaru', 'outback', 2013)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23500)
my_used_car.road_odometer()

my_used_car.increment_odometer(1500)
my_used_car.road_odometer()