from pathlib import Path
import json


def get_stored_userinfo(path):
    """Get stored userinfo if available."""
    if path.exists():
        contents = path.read_text()
        info = json.loads(contents)
        return info
    else:
        return None


def get_new_userinfo(path):
    """Prompt for a new userinfo."""
    username = input("What's your name? ")
    email = input("What's your e-mail? ")
    age = input("What's your age? ")

    info = {"username": username, "e-mail": email, "age": age}
    content = json.dumps(info)
    path.write_text(content)
    return info


def greet_user():
    """Greet the user by name and show userinfo."""
    path = Path("userinfo.json")
    info = get_stored_userinfo(path)
    if info:
        print(f"Is '{info['username']}' your username?")
        answer = input("Type Y or N. ")
        if answer == "Y" or answer == "y":
            print(f"Welcome back {info['username']}. Here is your info:")
            print(f"E-mail: {info['e-mail']}")
            print(f"Age: {info['age']} years old.")
        else:
            get_new_userinfo(path)
    else:
        info = get_new_userinfo(path)
        print(f"We'll remember you when you come back, {info['username']}!")


greet_user()
