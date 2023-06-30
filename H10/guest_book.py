from pathlib import Path

guest_list = ""
path = Path("guest.book.txt")

while True:
    print("Enter s to stop and save names in a file.")
    name = input("Name for guest list: ")

    if name == "s":
        break
    else:
        guest_list += f"{name}\n"

path.write_text(guest_list)
