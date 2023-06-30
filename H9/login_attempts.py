class User:
    """A class representing a user."""

    def __init__(self, first_name, last_name, hobby, eye_color, length):
        self.first_name = first_name
        self.last_name = last_name
        self.hobby = hobby
        self.eye_color = eye_color
        self.length = length
        self.login_attempts = 0

    def describe_user(self):
        print("\n=========================================")
        print(f"Summary of user: {self.first_name} {self.last_name}")
        print(f"Hobby: {self.hobby}")
        print(f"Eye color: {self.eye_color}")
        print(f"Lenght: {self.length} cm")
        print("=========================================")

    def greet_user(self):
        print(f"\nHi {self.first_name}! Nice to meet you!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


# Make instance
tom = User("Tom", "van Dorp", "Tennis", "Bruin", "180")

# Login attempts should be 0 by default:
print(tom.login_attempts)

# Call increment_login_attempts a couple times and show attempts
for _ in range(5):
    tom.increment_login_attempts()

print(tom.login_attempts)

# Reset login attempts and show result
tom.reset_login_attempts()
print(tom.login_attempts)
