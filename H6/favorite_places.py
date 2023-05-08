favorite_places = {
    'frans': ['woerden', 'utrecht', 'new york'],
    'mathilde': ['utrecht', 'london', 'new york'],
    'henk': ['leiden', 'brussel', 'paris'],
    'peter': ['amsterdam', 'bagdad'],
    'marieke': ['groningen', 'madrid', 'cairo'],
    }

for name, place in sorted(favorite_places.items()):
    print(f"\nName: {name.title()}")
    print("Favorite cities:")

    for city in place:
        print(f"* {city.title()}")