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


class Admin(User):
    def __init__(self, first_name, last_name, hobby, eye_color, length):
        super().__init__(first_name, last_name, hobby, eye_color, length)
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        """Show the privileges of this admin."""
        print(f"\n{self.first_name} has the following privilege(s):")
        for privilege in self.privileges:
            print(f"- {privilege}")


michel = Admin("Michel", "Koek", "Fifa", "Brown", 197)
michel.show_privileges()
