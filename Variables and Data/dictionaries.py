# Dictionaries can be compared to ordered pairs.
# In Discrete Mathematics, we use the concept of an ordered pair (a, b) as a pair of objects. 
# The order in which the objects appear in the pair is significant: the ordered pair (a, b) 
# is different from the # ordered pair (b, a) unless 
# a = b. (In contrast, the unordered  # pair {a, b} equals the unordered pair {b, a}.) 

# dictionary = {key1:value1, key2:value2}
# A simple dictionary can have the form of:
dragon_0 = {'name':'paarthurnax','element':'fire'}

print(dragon_0['name'].title())
print(dragon_0['element'].title())

# Accessing data from a dictionary
dragon_name = dragon_0['name']
dragon_element = dragon_0['element']

print("You were hit by " + dragon_element + ' attack from ' + dragon_name.title() + '.')

# Adding new pair key:value
# Since dictionaries are dynamic, we can add new pair of key:value to a dictionary by any time. To do that:
# Let's add two new info for our dragon_0: level and role
dragon_0 = {'name':'paarthurnax','element':'fire'}

dragon_0['level'] = 32
dragon_0['role'] = 'ally'

if dragon_0['role'] == 'ally':
    print(dragon_0['name'].title() + ' is your ally. Current level is:', dragon_0['level'],'xp')

# Starting an empty dictionary:
dragon_1 = {}

dragon_1['name'] = 'alduin'

print(dragon_1)

# Modifying values from a dictionary:
dragon_1 = {'name':'alduin','element':'frost'}

print(dragon_1['name'].title() + 'is a ' + dragon_1['element'] + ' dragon!')

dragon_1['element'] = 'fire'
print(dragon_1['name'].title() + ' is now a ' + dragon_1['element'] + ' dragon!')

# Let's imagine Paarthurnax attacking with fire breath that causes a damage of 35 fire damage per second:
dragon_0 = {'name':'paarthurnax','attack':'strong','attackbase':0}

print(dragon_0['name'].title() + ' is ' + dragon_0['attack'] + ' attacking')

if dragon_0['attack'] == 'light':
    attackbase = 35
elif dragon_0['attack'] == 'strong':
    attackbase = 45

dragon_0['attackbase'] = dragon_0['attackbase'] + attackbase
print(dragon_0['name'].title() + ' has a base attack of', dragon_0['attackbase'],'per second')

# Removing a pair of key:value
# Let's remove the attack and attackbase attributes from dragon_0
dragon_0 = {'name':'paarthurnax','attack':'strong','attackbase':0}

print(dragon_0)

del dragon_0['attack']
del dragon_0['attackbase']

print(dragon_0)

# Now let's create an dictionary containing the same type of information: dragon name and specialty:
dragons = {
    'paarthurnax':'fire','alduin':'frost','durnehviir':'dark magic',}

# Each key is the name of dragon and each value is the specialty
# We can run each data using a for lace:

# Running each elements:
user_0 = {
    'username':'victorh', 'first': 'victor', 'last':'hugo'}

for key, value in user_0.items():
    print("\nKey: " + key)
    print("Value: " + value)

# Or:
dragons = {
    'paarthurnax':'fire','alduin':'frost','durnehviir':'dark magic',}

for name, specialty in dragons.items():
    print(name.title() + ' specialty is ' + specialty + '.')

# Running every KEYS in a dictionary using keys()
# We can use this method when the value is not what we want to work with:
dragons = {
    'paarthurnax':'fire','alduin':'frost','durnehviir':'dark magic',}

# Let's see what dragons do we have:
for name in dragons.keys():
    print(name.title())

# We can access the value associated with any key using the actual key. Let's see what The Beatles used to play:

beatles = {
    'paul':'bass','ringo':'drums','harrison':'guitar','lennon':'vocals'}

string_players = ['paul','harrison']

for name in beatles.keys():
    print(name.title())
    if name in string_players:
        print('Hello ' + name.title() +', I see you can play ' +
        beatles[name] + '.')

# Let's see if Freddie Mercury was a beatle:
if 'mercury' not in beatles.keys():
    print('Freddie Mercury was not a beatle.')

# Running all the keys from a dictionary thru a lace:
# We cannot obtain the items from a dictionary in a predictable order. But this is not a problem because we only want a 
# value associated with a key. # We can order the keys using the sorted() method to get a ordered copy from the keys:
beatles = {
    'paul':'bass','ringo':'drums','harrison':'guitar','lennon':'vocals'}

for name in sorted(beatles.keys()):
    print(name.title() + ' is an amazing musician!')

# Running all the VALUES from a dictionary using values()
beatles = {
    'paul':'bass','ringo':'drums','harrison':'guitar','lennon':'vocals'}

print('The Beatles had:')

for instrument in beatles.values():
    print(instrument.title())

# --------------------------------------------- #
# Nested infos:
# We can store a set of dictionaries in a list of items
# as a value in a dictionary, or even a dictionary in another dictionary. Nesting information can be done in the following way:
dragon_0 = {'color':'green','element':'fire'}
dragon_1 = {'color':'golden','element':'frost'}
dragon_2 = {'color':'black','element':'fire'}

# How can we manage a group of dragons?
# We can store all dragons in dragon[]
dragons = [dragon_0, dragon_1, dragon_2]

for dragon in dragons:
    print(dragon)

# Let's create a group of 30 dragons:
# Creating a list to store a lot of dragons:
dragons = []

# Let's create 30 black dragons:
for dragon_number in range(30):
    new_dragon = {'color':'black','element':'fire'}
    dragons.append(new_dragon)

# Let's see our first 5 dragons:
for dragon in dragons[:5]:
    print(dragon)
    print('...')

# How much dragons do we have?
print("We have " + str(len(dragons)) + ' dragons created!')

# Since Python will thread each dragon as a different object, how can we work with a set of dragons?
# Let's pretend that we need some dragons to change their color and elements:
# We can use a for lace to change their color and an if to change their elements:
# Creating a list to store a lot of dragons:
dragons = []

# Let's create 30 red dragons:
for dragon_number in range(30):
    new_dragon = {'color':'red','element':'fire'}
    dragons.append(new_dragon)

for dragon in dragons[0:3]:
    if dragon['color'] == 'red':
        dragon['color'] = 'blue'
        dragon['element'] = 'frost'

for dragon in dragons[0:5]:
    print(dragon)
    print('...')

# We can add an elif block to turn blue dragon in allies:
# Let's create 30 red dragons:
for dragon_number in range(30):
    new_dragon = {'color':'red','element':'fire'}
    dragons.append(new_dragon)

for dragon in dragons[0:3]:
    if dragon['color'] == 'red':
        dragon['color'] = 'blue'
        dragon['element'] = 'frost'
    elif dragon['color'] == 'blue':
        dragon['role'] = 'ally'

for dragon in dragons[0:5]:
    print(dragon)

# We can do the opposite and add a list into a dictionary:
# Let's create a list with the aspects of ice cream like the flavours and toppings:

ice_cream = {
    'flavour':'vanilla','toppings':['chocolate', 'cherries']}

# Listing the order:
print("You want a " + ice_cream['flavour'] + " ice cream with the toppings:")

for topping in ice_cream['toppings']:
    print("\t" + topping.title())

# We can have more than one information:
beatles = {
    'paul':['bass','guitar','piano','vocals'],'ringo':['drums','piano','vocals'],
    'harrison':['guitar','bass','citar','vocals'],'lennon':['vocals','piano','guitar','bass'],}

for name,instruments in beatles.items():
    print("\n" + name.title() + ' can play:')
    for instrument in instruments:
        print("\t" + instrument.title())

# End of Chapter


