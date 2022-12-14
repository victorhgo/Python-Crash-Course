# Use a dictionary to store the favorite number for some person.

favorite_numbers = {
    'isac':8,'karen':7,'victor':15,'matheus':17,'neto':49,}

# Using a for loop and the method items()
for person,number in favorite_numbers.items():
    print("Hello " + person.title() + ', I can see that your favorite number is',number)
