pets = []

pet = {
    'specie': 'dog',
    'name': 'keesje',
    'owner': 'bas',
    'weight': 21,
    }
pets.append(pet)

pet = {
    'specie': 'cat',
    'name': 'sammie',
    'owner': 'merel',
    'weight': 11,
    }
pets.append(pet)

pet = {
    'specie': 'rabbit',
    'name': 'white',
    'owner': 'naomi',
    'weight': 2,
}
pets.append(pet)

for pet in pets:
    print(f"\n{pet['name'].title()} is a {pet['specie']} with the name {pet['name'].title()} and has a weight of {pet['weight']} kilo. The owner's name is {pet['owner'].title()} ")