from user import User


class Admin(User):
    def __init__(self, first_name, last_name, hobby, eye_color, length):
        super().__init__(first_name, last_name, hobby, eye_color, length)
        self.privileges = Privileges(
            ["can add post", "can delete post", "can ban user"]
        )


class Privileges:
    def __init__(self, privileges):
        self.privileges = privileges

    def show_privileges(self):
        """Show the privileges of this admin."""
        print("This admin has the following privilege(s):")
        for privilege in self.privileges:
            print(f"- {privilege}")
