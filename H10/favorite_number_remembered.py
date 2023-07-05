from pathlib import Path
import json


path = Path("favorite_number.txt")
if path.exists():
    contents = path.read_text()
    favorite_number = json.loads(contents)
    print(f"I know your favorite number! It's '{favorite_number}'")
else:
    favorite_number = input("What's your favorite number? ")
    contents = json.dumps(favorite_number)
    path.write_text(contents)
    print("\nThanks, I will remember your favorite number!")
