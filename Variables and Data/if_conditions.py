# If conditions are useful to analyse conditions and perform actions
# The simplest way to answer a question:
friends = ['victor', 'daniel', 'david', 'abraham']

for friend in friends:
    if friend == 'victor':
        print(friend.title() + ' was invited to the party!')
    else:
        print(friend.title() + ' was not invited to the party!')

# Verifying equality
name = 'victor'
print(name == 'victor')  # It will return True
print(name == 'abraham') # It will return False

# Working with upper or lower letters:
name = 'Victor'
print(name == 'victor')

# To compare and ignore the upper or lower letters:
print(name.lower() == 'victor')

# Comparing difference using !=
icecream_topping = 'strawberry'

if icecream_topping != 'chocolate':
    print("Hold the chocolate!")

# --------------------------------------------- #
# Numeric Comparison:

answer = 89

if answer != 89:
    print("Wrong answer, try again")

# Verify if a item is on a list:
icecream_topping = ['strawberry', 'chocolate', 'coconut', 'nutella']

if 'vanilla' in icecream_topping:
    print("You can put vanilla")
if 'vanilla' not in icecream_topping:
    print("You can't have vanilla")

# If else:
age = 16

if age > 18:
    print("You can drive")
else:
    print("You cannot drive yet!")

# if-elif-else
age = 18

if age < 15:
    print("You are a child")
elif age < 18:
    print("You are an adolescent")
else:
    print("You are an adult!")

# Using a lot of elif blocks
age = 60

if age < 15:
    print("You are a child")
elif age < 18:
    print("You are an adolescent")
elif age < 60:
    print("You are an adult!")
else:
    print("You're an elder!")

# We can also omitt the else block:
age = 70

if age < 15:
    print("You are a child")
elif age < 18:
    print("You are an adolescent")
elif age < 60:
    print("You are an adult!")
elif age >= 60:
    print("You're an elder!")

# If we want to test varius possibilities:
icecream_toppings = ['strawberry', 'chocolate', 'coconut', 'nutella']
if 'strawberry' in icecream_toppings:
    print('Adding strawberries...')
if 'chocolate' in icecream_toppings:
    print('Adding chocolate...')
if 'nutella' in icecream_toppings:
    print('Adding nutella...')
if 'coconut' in icecream_toppings:
    print('Adding coconut...')

print("Your ice-cream is ready!")

# Using if with lists:
requested_toppings = ['peanut butter', 'marshmellow', 'chocolate', 'strawberry jam']

for requested_topping in requested_toppings:
    print('Adding ' + requested_topping.title() +'.')

print('Your icecream is ready!')

# What if the chocolate jar is empty? A simple if in the for lace can be used:
requested_toppings = ['peanut butter', 'marshmellow', 'chocolate', 'strawberry jam']

for requested_topping in requested_toppings:
    if requested_topping == 'chocolate':
        print("Sorry, we're out of " + requested_topping + '.')
    else:
        print('Adding ' + requested_topping + ' to your icecream' )

print("Your ice cream is ready")

# Verifying if a list is not empty
requested_toppings = []

if requested_toppings:
    for requested_topping in requested_toppings:
        print("Adding " + requested_topping + ' to your ice cream')
        print("Finished your ice cream")
else:
    print("Are you sure you want a plain ice cream?")

# Using various lists:
requested_toppings = ['peanut butter', 'marshmellow', 'chocolate', 'strawberry jam', 'ketchup']

available_toppings = ('peanut butter', 'marshmellow', 'chocolate', 'strawberry jam')

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding " + requested_topping + " in your ice cream")
    else:
        print("Sorry, we don't have " + requested_topping + '.')

print("Your ice cream is ready!")

# End of Chapter