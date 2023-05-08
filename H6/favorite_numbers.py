favorite_number = {
    'Henk': [2, 5, 12],
    'Jan': [14, 3, 2, 14],
    'Jaap': [22, 1, 30, 10],
    'Fien': [7],
    'Liz': [3, 7],
    }

for name, numbers in favorite_number.items():
    if len(numbers) > 1:
        print(name, "'s favorite numbers are:", sep='')
        
        for number in numbers:
            print(f"* {number}")
        
        print("")
    
    else:
        print(name, "'s favorite number is: ", numbers, "\n", sep='')