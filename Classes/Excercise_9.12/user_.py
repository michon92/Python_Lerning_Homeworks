class User:  # Only one class in script = Y haven't use para
    """Easy way to count how many times did some users logged to the portal"""
    def __init__(self, first_name, last_name, job, city):
        self.first_name = first_name
        self.last_name = last_name
        self.job = job
        self.city = city
        self.name = first_name + " " + last_name
        self.login_attempts = 0

    def describe_user(self):
        """Describe users personal data"""
        print("\nUsers " + self.name.title() + " works as "
              + self.job.title() + " in " + self.city.title()
              + " city.")

    def great_user(self):
        """Welcome every user"""
        print("\tNice to see you back, dear " + self.name.upper())

    def login_counts(self):
        """Show input counts"""
        print("\tYou've logged a " + str(self.login_attempts) + " times!")

    def increment_login_attempts(self):
        """Counting login inputs"""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Reset login inputs"""
        self.login_attempts = 0
