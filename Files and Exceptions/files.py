""" Now we will finally learn how to work with files, this way, we can write programs to
work fast with data."""

# Reading data from a file

""" Let's begin this chapter by opening the pi_digits.txt file"""
pi = 'pi_digits.txt'

# with open('pi_digits.txt') as file_object:
# with open(pi) as file_object:
#    contents = file_object.read()
#    print(contents.rstrip())

""" The with reserved word, closes the file after it's no longer being used"""

with open('text_files\pi_digits1.txt') as pi_digits:
    contents = pi_digits.read()
    print(contents.rstrip())

# Reading data line by line:

""" We can read line by line of a file to modify specific text from the file, or to
analyse specific information on the text.
 We can use a for loop in the object to analyse line by line:"""

with open('text_files\pi_digits1.txt') as pi_digits:
    for line in pi_digits:
        print(line)

# Creating a list of lines from a file:

""" When using with, the object returned by open() will be available only in that block. 
If we want to store the content of a file, we can store the lines of a file into a list"""

with open('text_files\pi_digits1.txt') as pi_digits:
    lines = pi_digits.readlines()
    for line in lines:
        print(line.rstrip())

# Working with the content of a file.