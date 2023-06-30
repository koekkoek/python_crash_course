from random import choice


def lottery():
    items = (
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "10",
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
            winner.append(current_item)

    return winner


my_ticket = ["1", "a", "5", "9"]
count = 0

while True:
    ticket = lottery()

    if my_ticket == ticket:
        break
    else:
        count += 1

print(f"We had to try {count} times before you finally won a price!")
