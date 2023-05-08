rivers = {
    'Nile': 'Egypt',
    'Rijn': 'Netherlands',
    'Theems': 'England',
    }

for river, land in rivers.items():
    print(f"The {river} runs through {land}.")

print("\nThese are the available rivers:")
for river in rivers.keys():
    print(river)

print("\nEn these are the country's:")
for land in rivers.values():
    print(land)