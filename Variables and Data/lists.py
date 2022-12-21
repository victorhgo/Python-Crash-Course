# What are lists and how do we work with them? #

# In a simple way, lists are collection of items      #
# in a particular order, lists can contain numbers,   #
# letters, words, sentences... Any information can be #
# stored on a list and they don't need to have any re #
# lation. It's always a good idea to have lists names #
# in plural.                                          #

# keyword: vectors

# A list containing some aircraft companies           #
aircrafts = ['boeing','airbus','cesna','embraer','bombardier']

# We can print this full list with print() #
print(aircrafts)

# We can print them on a sorted way: print(string(index)) #
print(aircrafts[0].title()) # using title() method.

# To return the very last item using -1
print(aircrafts[-1].title())

# Using individual values from a list
message = "I love to fly in " + aircrafts[3].title() + " airplanes!"
print(message)

# --------------------------------------------- #
# Ex 1 #
names = ['karen', 'isac', 'matheus', 'alisson', 'felipe']
print(names[0].title())
print(names[1].title())
print(names[2].title())
print(names[3].title())
print(names[-1].title())

# Ex 2 #
greetings = "Hello, " + names[0].title()
print(greetings)
greetings = "Hello, " + names[1].title()
print(greetings)
greetings = "Hello, " + names[2].title()
print(greetings)
greetings = "Hello, " + names[3].title()
print(greetings)
greetings = "Hello, " + names[-1].title()
print(greetings)

# --------------------------------------------- #
# ------ Modifying elements from a list ------- #

cars = ['subaru', 'mercedes', 'BMW', 'honda', 'volkswagen', 'dodge']

# To modify the first element from a list:
print(cars[0].title())
cars[0] = 'ferrari'
print(cars[0].title())

# Adding elements to a list using append() #
cars = ['subaru', 'mercedes', 'BMW', 'honda']

print(cars)
cars.append('toyota')
print(cars)

# Using append() to fill an empty list #
laptop_makers = []

laptop_makers.append('dell')
laptop_makers.append('apple')
laptop_makers.append('samsung')

print(laptop_makers)

# Using insert() to add elements to a list #
laptop_makers = ['apple', 'samsung', 'dell', 'lenovo']
laptop_makers.insert(0, 'hp') # index, 'content

print(laptop_makers)

# Removing elements from a list using del instruction #
laptop_makers = ['apple', 'samsung', 'dell', 'lenovo']

del laptop_makers[3]

print(laptop_makers)

# Removing using the pop() method #
laptop_makers = ['apple', 'samsung', 'dell', 'lenovo']

print(laptop_makers)

popped_laptop_makers = laptop_makers.pop()

print(popped_laptop_makers)

first_owned = laptop_makers.pop(0) # It will remove 'apple' from laptop_makers
print("The first laptop I owned was an " + first_owned.title() + " one.")

print(laptop_makers)

# Removing items accordingly to value using remove() #
laptop_makers = ['apple', 'samsung', 'dell', 'lenovo']
laptop_makers.remove('apple')

print(laptop_makers)

# Removing to work with a item that will be removed from a list 
laptop_makers = ['apple', 'samsung', 'dell', 'lenovo']
too_expensive = 'apple'
laptop_makers.remove(too_expensive)

print("\nAn " + too_expensive.title() + " laptop is too expensive!")

# ------------ Sorting a List in Python ------------ #

# Sorting a list using the sort() method #
# The sort() will put all the words in alphabetical order
# if all the items are in lowcase letters.

# sort() will change a list PERMANENTLY!!!

names = ['Hanna', 'Lara', 'Stella', 'Judithy', 'Luanna', 'Alice', 'Benetta']
names.sort()

print(names)

# We can reverse them alphabetically by reverse=True
names.sort(reverse=True)

print(names)

# Sorting a list TEMPORARILY using sorted()
names = ['Hanna', 'Lara', 'Stella', 'Judithy', 'Luanna', 'Alice', 'Benetta']

print('The original list is:')
print(names)

print('List temporarily sorted:')
print(sorted(names))

# Reversed a string using reversed()

# It changes a list permanently, but can be undone using reverse() again
names = ['Hanna', 'Lara', 'Stella', 'Judithy', 'Luanna', 'Alice', 'Benetta']

names.reverse()
print(names)

# Size of a list using the method len()
names = ['Hanna', 'Lara', 'Stella', 'Judithy', 'Luanna', 'Alice', 'Benetta']

print(len(names))

# End of Chapter
