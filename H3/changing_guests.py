guests = ["Pieter", "Werner", "Jan", "Frits"]

for i in range(4):
    print(f"{guests[i]}, you are invited!")

#remove Werner & add Tom
print("\nThere will be some changes...\n")
del(guests[1])
guests.insert(1, "Tom")

for i in range(4):
    print(f"{guests[i]}, you are invited!")