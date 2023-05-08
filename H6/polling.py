favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
    }

persons = ['jen', 'ruben', 'piet', 'gerard', 'edward']

for person in persons:
    if person in favorite_languages.keys():
        print(f"{person.title()}, thanks for voting!")
    else:
        print(f"{person.title()} please vote...")
