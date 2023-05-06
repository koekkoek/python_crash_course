pizzas = ["hawaii", "salami", "quatro formagi"]
friend_pizzas = pizzas[:]

# Add a new pizza to the original list
pizzas.append("calzone")

# Add a different pizza to the list friend_pizzas
friend_pizzas.append("kebab")

# Print favorite pizza's
print("\nMy favorite pizza's are:")
for pizza in pizzas:
    print(f"* {pizza}")

print("\nMy friend's favorite pizza's are:")
for pizza in friend_pizzas:
    print(f"* {pizza}")