cities = {
    'bodegraven': {
        'country': 'the netherlands',
        'population': 35_000,
        'fact': 'city of cheese',
        },
    'utrecht': {
        'country': 'the netherlands',
        'population': 360_000,
        'fact': 'has many churches'
        },
    'london': {
        'country': 'england',
        'population': 3_450_821,
        'fact': 'one of worlds best metro network',
        },
    }

for name, facts in cities.items():
    print(f"\nInformation about {name.title()}:")

    for key, fact in facts.items():
        print(f"{key}: {fact}")


