person_1 = {
    'first_name': "henk",
    'last_name': "de gier",
    'age': 34,
    'city': "bodegraven",
    }

person_2 = {
    'first_name': "menno",
    'last_name': "jansen",
    'age': 55,
    'city': "arnhem",
    }

person_3 = {
    'first_name': 'marieke',
    'last_name': 'jongelaar',
    'age': 23,
    'city': 'utrecht'
}

people = [person_1, person_2, person_3]

for person in people:
    full_name = f"{person['first_name']} {person['last_name']}"
    print(f"\nNaam: {full_name.title()}")
    print(f"Leeftijd: {person['age']}")
    print(f"City: {person['city'].title()}")
