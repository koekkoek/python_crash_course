toppings = []
message = "Enter a pizza topping:"
message += "\nEnter 'quit' to stop this program. "
count = 0

flag = True

while flag:
    count += 1
    topping = input(message)

    if topping.lower() == "ham":
        print("That doesn't belong to a pizza! So I will exit this program!")
        print(count)
        flag = False
    
    elif topping.lower() != "quit":
        toppings.append(topping)
        print(f"I will add {topping} to your pizza.\n")
    
    else:
        print(count)
        break

print(toppings)