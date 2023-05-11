prompt = "If you could visit one place in the world, where would you go? "
vacation = {}

while True:
    name = input("Type 'exit' to stop this program.\nWhat's your name? ")
    city = input(prompt)

    if name.lower() == 'exit' or city.lower() == 'exit':
        break
    else:
        vacation[name] = city

print("\nDE RESULTATEN:\n")

for key, value in vacation.items():
    print(f"{key.title()} would like to visit {value.title()}.")