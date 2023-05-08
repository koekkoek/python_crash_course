car = "Hyundai"

print("\nIs car == 'ford'? I predict False.")
print(car.lower() == "ford")

print("\nIs car == 'hyundai'? I predict True.")
print(car.lower() == "hyundai")

car = "Ford"

print("\nIs Hyundai de beste auto? Denk het niet...")
print(car.lower() == "hyundai")

print("\nIs het dan een ford? Natuurlijk, let maar op!")
print(car.lower() == "ford")

# Users input about car brands
answer = input("\nWelke auto rijd je? ")
if answer.lower() != "ford" and answer.lower() == "hyundai":
    print("Sjonge jonge. Dit is het ergste wat kan gebeuren. Ik moet hier even van bijkomen...")
elif answer.lower() != "ford":
    print("Balen voor je! Ga toch eens een echte auto rijden!")
else:
    print("Gaaf man! Heerlijk is dat!")

# numerical tests
age = 12
if age < 4:
    print('je bent nog veel te jong om alcohol te drinken')
elif age < 18:
    print(f"je mag nog geen alcohol drinken. Je moet nog {18 - age} jaar wachten.")
else:
    print("Gefeliciteerd. Je bent oud genoeg voor alcohol!")

# Trying to find out if an item is and is not in a list
menu = {"ginger", "tea", "fries", "pizza", "mushrooms", "potatoes"}

if "pizza" in menu:
    print("Yes, you can order pizza!")

if "olives" not in menu:
    print("That's sad. We don't have olives...")