# All different kind of data we can work with Python #

# The first basic is a string:

message = "Hello, my name is Victor Hugo!"
greetings = "Nice to meet you!"

print(message + ' ', greetings)

# Changing between lowercase and capital letters #

# To make the first letter as capital using title() #

name = "margareth hamilton"
print(name.title())

# Make all letters uppercase using upper() #

print(name.upper())

# All letters as lower case using lower() #

print(name.lower())

# Combining and concatenating strings #

first_name = "victor"
last_name = "correa"
full_name = first_name + ' ' + last_name
print("Hello, " + full_name.title() + "!")

# Or

message = "Hello, " + full_name.title() + "!"
print(message)

# --------------------------------------------- #

# Adding blank spaces in tabulated strings or line breaks #

# Using \t to add tabulating in text like: #

print("\tPython\tC++\tJavaScript\tCobol")

# The \n can be used to create a new line #

print("\n\tPython\n\tC++\n\tJavaScript\n\tCobol")

quote = '\n\t"Every one of us is, in the cosmic perspective, precious. If a human disagrees with you, let him live. In a hundred billion galaxies, you will not find another."'
author = "carl sagan"
quoting = author.title() + " once said: " + quote
print(quoting)

# --------------------------------------------- #
# ------------ Working with Numbers ----------- #

# Wishing happy birthday #

age = 24
name = "Victor Hugo"
message = "Happy " + str(age) + "rd Birthday, " + name + '!'
print(message)

# --------------------------------------------- #
# Arithmetic Operators #

print(5 + 3)
print(16 / 2)
print(4 * 2)
print(9 - 1)
