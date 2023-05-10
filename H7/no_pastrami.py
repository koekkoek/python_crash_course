sandwich_orders = ['salmon', 'bmt', 'pastrami', 'chicken', 'brie', 'pastrami', 'cheese', 'healthy', 'pastrami']
finished_sandwiches = []

print('The Deli is run out of pastrami...\n')

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
    print("I removed a pastrami from the orders.")

print('')

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f"I'm busy finishing your {sandwich} sandwich!")
    finished_sandwiches.append(sandwich)

print("\nI'm done. The following sandwiches are ready to eat:")
for sandwich in finished_sandwiches:
    print(f"* {sandwich}")