prompt = "\nWhat is your age?"
prompt += "\nType 'stop' to exit. "

while True:
    age = input(prompt)

    if age.lower() == 'stop':
        break

    age = int(age)
    if age < 3:
        print("Your ticket is free.")
    
    elif age <12:
        print("Your ticket is € 10,-")
    
    else:
        print("Your ticket is € 15,-")