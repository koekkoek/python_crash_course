foods = ("tosti", "pizza", "sandwich", "fries", "salad")

print("Choose some food:")
for i in range(5):
    print(f"{i+1}. {foods[i]}")

#foods[1] = "something else"

foods = ("tosti", "vegan surprise", "sandwich", "hotdog", "salad")

print("\nWe changed our menu. What do you want to order?")
for i in range(5):
    print(f"{i+1}. {foods[i]}")
