"""Users INFO"""
class User():
    def __init__(self, first_name, last_name, job, city):
        self.first_name = first_name
        self.last_name = last_name
        self.job = job
        self.city = city
        self.name = first_name + " " + last_name


    def describe_user(self):
        """Describe users personal data"""
        print("\nUsers " + self.name.title() + " works as "
              + self.job.title() + " in " + self.city.title()
              + " city.")
        
    def great_user(self):
        """Welcome every user"""
        print("\tNice to see you back, dear " + self.name.upper())
        

my_user = User('first', 'last', 'job', 'city')
my_user.describe_user()
my_user.great_user()

my_user1 = User('kasztan', 'zielony', 'leśniczy', 'rzeszów')
my_user1.describe_user()
my_user1.great_user()

my_user2 = User('Jan', 'Kowalski', 'driver', 'wrocław')
my_user2.describe_user()
my_user2.great_user()

my_user_3 = User('mister', 'bean', 'stand-upper', 'london')
my_user_3.describe_user()
my_user_3.great_user()