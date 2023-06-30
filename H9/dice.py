from random import randint


class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        return randint(1, self.sides)


# Die with 6 sides, roll it 10 times
dice_6 = Die()
for n in range(10):
    print(f"New roll: {dice_6.roll_die()}")

# Die with 10 sides, roll it 10 times
print("\nNew Die with 10 sides. Here we go:")
dice_10 = Die()
dice_10.sides = 10
for n in range(10):
    print(f"New roll: {dice_10.roll_die()}")

# Die with 20 sides, roll it 10 times
print("\nNew Die with 20 sides. Here we go:")
dice_20 = Die()
dice_20.sides = 20
for n in range(10):
    print(f"New roll: {dice_20.roll_die()}")
