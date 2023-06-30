from pathlib import Path

answer = input("What's your name? ")

path = Path("guest.txt")

# Save the name of the guest in guest.txt
path.write_text(answer)
