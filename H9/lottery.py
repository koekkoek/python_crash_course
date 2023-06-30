from random import choice

items = (
    "1",
    "2",
    "3",
    "4",
    "5",
    "10",
    "11",
    "15",
    "200",
    "234",
    "102",
    "a",
    "b",
    "c",
    "d",
    "e",
)
winner = []

while len(winner) < 4:
    current_item = choice(items)

    if current_item not in winner:
        print(f"The new number or letter is: {current_item}")
        winner.append(current_item)

print("That was a long wait...")
print("Ladies and gentlemens... The winner is...")

for n in winner:
    print(n, end=" ")
