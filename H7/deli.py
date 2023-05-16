sandwich_orders = ['salmon', 'bmt', 'chicken', 'brie', 'cheese', 'healthy']
finished_sandwiches = []

while sandwich_orders:
    # Pop sandwich from order and store it in temp value
    sandwich = sandwich_orders.pop()

    # Print a 'sandwich ready' order
    print(f"I made your {sandwich} sandwich.")

    # Add sandwich to new list
    finished_sandwiches.append(sandwich)

print("\nThat's it. I've made the following sandwiches:")

for sandwich in finished_sandwiches:
    # print(f"* {sandwich}")
    print(f"* {sandwich.title()} sandwich")
