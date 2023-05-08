glossary = {
    'for': 'looping through your program',
    'string': 'text',
    'int': 'a number',
    'github': 'a site to synch your git repository.',
    'variable': 'to store some information in it. Like a int, string or float.',
    }

print("Here are the terms:")
for term in glossary.keys():
    print(term)

print("\nAnd here is what they mean:")
for value in glossary.values():
    print(value)

print("\nAnd together:")
for term, meaning in glossary.items():
    print(f"{term}: '{meaning}'")

print("\nNow I will add some more Python terms.\n")

glossary['bool'] = "check if a statement is true or false."
glossary['=='] = "check if a variable is equal to another.."
glossary['loop'] = "running code over and over again. As long it is true."

for term, meaning in glossary.items():
    print(f"{term}: {meaning}")
