from pathlib import Path

filenames = ["cats.txt", "dogs.txt"]

for file in filenames:
    print("======================")
    print(f"Current file: {file}")
    path = Path(file)

    try:
        file = path.read_text()
    except FileNotFoundError:
        print(" Unfortunately, this file doens't exist.")
    else:
        print("\nNames found:")
        print(file)
        print("======================\n")
