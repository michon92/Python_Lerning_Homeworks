class Dog():
    """Easy try to simulate a dog"""
    def __init__(self, name, age):
        """Initial atributes name and age"""
        self.name = name
        self.age = age


    def sit(self):
        """Sit dog comment simulate"""
        print(self.name.title() + " sits now.")


    def roll_over(self):
        """Dog rolls over - simulate"""
        print(self.name.title() + " rolls over.")

my_dog = Dog('willie', 6)
your_dog = Dog('lucy', 5)
print("My dog name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")
my_dog.sit()
print("\nYours dog name is " + your_dog.name.title() + ".")
print("Yours dog is " + str(your_dog.age) + " years old.")
your_dog.roll_over()
