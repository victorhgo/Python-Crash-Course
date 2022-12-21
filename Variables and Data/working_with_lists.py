# Working with lists in Python and the use of for #

# We can create a list and run on each item of this list.
# This can simply be done using the for lace.

# For this example, we will create a list containing our dragons:

dragons = ['paarthurnax', 'alduin', 'odahviing', 'durnehviir']

# We can use a for to show the name of each dragon:
for dragon in dragons:
    print(dragon.title())

# Let's print some information with each dragon:
for dragon in dragons:
    print(dragon.title() + ' is fire breathing!')

# We can also perform more actions with each information
for dragon in dragons:
    print(dragon.title() + ' is flying.')
    print('Now ' + dragon.title() + ' has landed.')

# Performing actions:
for dragon in dragons:
    print(dragon.title() + ' is flying.')
    print('Now ' + dragon.title() + ' has landed.')

print('All dragons went resting now')

# --------------------------------------------- #
# -------------- Using range() ---------------- #

# This function allow us to create a serie of numbers:
for value in range(1, 10): # It will print from 1 to 9
    print(value)

# We can create a list of numbers using range() with list()
numbers = list(range(1,10))
print(numbers)

# We can use the range() to tell Python to ignore some number in a given interval
# For instance, to print the even numbers from 0 to 10:
even_numbers = list(range(0,11,2)) # 0 is the start point, 11 the end point and 2 the number to be added
print(even_numbers)

# To create a list with all squares from 1 to 10:
squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)

print(squares)

# The preview code can be re-factored and written like:
# In this example, we are not using the variable square
squares = []
for value in range(1,11):
    squares.append(value**2)

print(squares)

# Simple statistics using a number list:

# min() max() and sum()
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(min(data))
print(max(data))
print(sum(data))

# --------------------------------------------- #
#               List comprehensions             #
# --------------------------------------------- #
# Generating lists with a simple method:

# Creating the list with numbers from 0 to 10:
numbers = [number for number in range(0, 11)]
print(numbers)

#Creating the list with the squares from 0 to 10:
squares = [value**2 for value in range(0,11)]
print(squares)

# --------------------------------------------- #
# One million:
million = list(range(1,1000001))
# Or: million = [num for num in range(0,1000001)]

# for number in million:
#    print(number)

print(min(million))
print(max(million))
print(sum(million))

# --------------------------------------------- #
# Slicing a list:
dragons = ['paarthurnax', 'alduin', 'odahviing', 'durnehviir']

# Show the first 3 dragons:
print(dragons[0:3])

# We can generate any subset of a list like:
print(dragons[1:3])

# Using for for subsets:
dragons = ['paarthurnax', 'alduin', 'odahviing', 'durnehviir']

print("Here are the companion dragons:")
for dragon in dragons[2:4]:
    print(dragon.title())

# Copying a list using:

my_foods = ['pie', 'strawberry cake', 'pizza', 'lasagna']
other_foods = my_foods[:]

print("My favorite foods are:")
print(my_foods)

# Tuples: We call imutable lists as tuples
# The only difference is we use [] to specify mutable lists and () for tuples

board_dimension = (10,20)
print("Height:", board_dimension[0],"Width:", board_dimension[1])

# End of Chapter