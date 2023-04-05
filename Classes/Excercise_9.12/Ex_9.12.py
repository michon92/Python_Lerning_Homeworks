"""Importuję moduł privelages"""


from privelages import Admin, Privelages

my_user = Admin('admin', 'admin', 'adminek', 'adminowo')
my_user.privelages.show_privelages()