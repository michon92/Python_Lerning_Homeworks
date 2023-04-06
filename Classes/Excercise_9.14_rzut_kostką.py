from random import randint

import time


class Die:
    """rzut kostką"""

    def __init__(self):
        """ile ścianek ma kostka: domyślnie 6, i ile trafimy 6tek: 0"""
        self.sides = 6  # wartość domyślna wielkości kostki
        self.count = 0  # zliczanie trafień 6tki

    def roll_die(self):
        """symulacja 10 rzutów kistką"""
        for i in range(10):
            x = randint(1, self.sides)  # liczba oczek/ścianek
            print(x)
            time.sleep(0.5)  # czeka 0,5 sekundy
            if x == self.sides:  # sprawdzam czy trafiłem full-a XD
                print("\tBrawo, trafiłeś: " + str(x) + " !!")
                self.count += 1
        print("Trafiłęś " + str(self.count) + " X full-a: " + str(self.sides))

    def die_update(self, kostka):
        """zmiana wielkości kostki do x ilości ścianek"""
        self.sides = kostka  # w nawiasie podaj ilość ścianek kostki

    def points(self):
        """zlicza sumę pkt w danej serii 10 rzutów kostką danej wielkości"""
        pkts = self.count * self.sides  # zdobyte punkty w serii
        print("Zdobyłeś " + str(pkts) + " punktów! Kostką o "
              + str(self.sides) + " ściankach.")

    def default(self):
        """Przywrócenie ustawień domyślnych, zerownaie punktów"""
        self.count = 0


my_try = Die()  # implementacja klasy Die
my_try.roll_die()  # rzut kostką 6cio ściankową
my_try.points()  # zdobyte pkty
my_try.default()  # ustawienia domyślne
my_try.die_update(10)  # rzut kostka "10"
my_try.roll_die()
my_try.points()
my_try.default()  # zerowanie
my_try.die_update(20)
my_try.roll_die()
my_try.points()
