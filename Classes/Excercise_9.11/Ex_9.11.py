"""Importuję moduł :klasauser"""

from klasauser import Admin, Privelages

my_user = Admin('admin', 'admin', 'programista','szczecin')
my_user.privelages.show_privelages()