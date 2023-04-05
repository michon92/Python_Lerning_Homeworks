from user_ import User


class Admin(User):
    """definiuję klasę Admin dziedziczącą po klasie """
    def __init__(self, first_name, last_name, job, city):
        super().__init__(first_name, last_name, job, city)
        self.privelages = Privelages()


class Privelages:
    def __init__(self):
        """Inicjalizacja uprawnnień"""
        self.privelages = ['nic nie może', 'xD']

    def show_privelages(self):
        print("\nUprawnienia użytkownika Admin: ")
        for privelages in self.privelages:
            print("\t" + privelages)


my_user = Admin('admin', 'admin', 'adminek', 'adminowo')
my_user.privelages.show_privelages()
