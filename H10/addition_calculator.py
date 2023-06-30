print("======================")
print("Let's add two numbers.")
print("======================")

while True:
    print("\nUse s to stop.")
    number_1 = input("First number: ")

    if number_1 == "s":
        break

    number_2 = input("Second number: ")
    if number_2 == "s":
        break

    try:
        sum = int(number_1) + int(number_2)
    except ValueError:
        print("\nOnly use integers please.")
    else:
        print(f"The sum is: {sum}")
        break
