from pathlib import Path
import json


def insert_favorite_number():
    favorite_number = input("What's your favorite number? ")

    path = Path("favorite_number.txt")
    contents = json.dumps(favorite_number)
    path.write_text(contents)


def get_favorite_number():
    path = Path("favorite_number.txt")

    if path.exists():
        contents = path.read_text()
        favorite_number = json.loads(contents)
        print(f"I know your favorite number! It's {favorite_number}!")
    else:
        print("bummer!")


insert_favorite_number()
get_favorite_number()
