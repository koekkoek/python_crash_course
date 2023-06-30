class User:
    """A class representing a user."""

    def __init__(self, first_name, last_name, hobby, eye_color, length):
        self.first_name = first_name
        self.last_name = last_name
        self.hobby = hobby
        self.eye_color = eye_color
        self.length = length

    def describe_user(self):
        print("\n=========================================")
        print(f"Summary of user: {self.first_name} {self.last_name}")
        print(f"Hobby: {self.hobby}")
        print(f"Eye color: {self.eye_color}")
        print(f"Lenght: {self.length} cm")
        print("=========================================")

    def greet_user(self):
        print(f"\nHi {self.first_name}! Nice to meet you!")


# Make instances from class
tom = User("Tom", "van Dorp", "Tennis", "Bruin", "180")
peter = User("Peter", "van Veen", "Fitness", "Blauw", "178")
mark = User("Mark", "Koning", "BBQ", "Blauw-groen", "175")

# Call methods of instances
tom.describe_user()
tom.greet_user()
peter.describe_user()
peter.greet_user()
mark.describe_user()
mark.greet_user()
