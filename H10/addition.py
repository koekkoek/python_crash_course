print("======================")
print("Let's add two numbers.")
print("======================")

try:
    number_1 = int(input("First number: "))
    number_2 = int(input("second number: "))
except ValueError:
    print("\nOnly use integers please.")
else:
    sum = number_1 + number_2
    print(f"The sum is: {sum}")
