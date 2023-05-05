guests = ["Pieter", "Werner", "Jan", "Frits"]

for i in range(4):
    print(f"{guests[i]}, you are invited!")

print(f"\nSorry, {guests[1]} can't make it. We wil remove him from the list. And add Tom to it.\n")

del guests[1]
guests.insert(1, "Tom")

for i in range(4):
    print(f"{guests[i]}, you are invited!")

print("\nWe got a much bigger table! So we will add some guests.\n")

guests.insert(1, "Ron")
guests.append("Henk")
guests.append("Jaap")

for i in range(7):
    print(f"{guests[i]}, you are invited!")