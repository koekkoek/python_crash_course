def sandwiches(*toppings):
    print("\nYou want the following toppings:")
    for topping in toppings:
        print(f"- {topping}")


sandwiches("salami", "cheese", "tomato's")
sandwiches("ham")
sandwiches("cheese", "mozarella", "strawberries", "more cheese", "pepperoni")
