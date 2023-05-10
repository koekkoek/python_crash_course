toppings = []
message = "Enter a pizza topping:"
message += "\nEnter 'quit' to stop this program. "

flag = True

while flag:
    topping = input(message)

    if topping.lower() != "quit":
        toppings.append(topping)
        print(f"I will add {topping} to your pizza.")
    else:
        flag = False

print(toppings)