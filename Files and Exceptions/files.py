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
""" In this example, let's explore some of the pi digits"""

file_name = 'text_files\pi_digits1.txt'

with open(file_name) as file_object:
    lines = file_object.readlines()
pi_string = ''

for line in lines:
    pi_string += line.rstrip()
    print(pi_string)
    print(len(pi_string))

# Gigantic files: 1 million of digits.
""" Let's open a file that contains 1 million digits of Pi"""
pi_million = 'text_files\pi_million_digits.txt'

with open(pi_million) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()
    print(pi_string[:52] + '...')
    print(len(pi_string))

# Is my birthday in Pi?
pi_million = 'text_files\pi_million_digits.txt'

with open(pi_million) as file_object:
    lines = file_object.readlines()
    
pi_string = ''
for line in lines:
    pi_string += line.rstrip()

birthday = input("Birthday (mmddyy): ")
if birthday in pi_string:
    print("Your birthday appears in pi!")
else:
    ("Your birthday is not in pi!")

# Write data to a file:
""" We can write data to a open file using open() with a second argument to tell Python that
we want to write data to a file."""

write_file = 'text_files\hello.txt'

""" Open file as Write, Read, Concatenation 'a' and R/W 'r+ '"""
with open(write_file, 'w') as file_object:
    file_object.write("Hello World")

""" We use the write() method to write string in the opened file"""
"""
write_user = 'text_files\hellouser.txt'

with open(write_user, 'w') as writing:
    input_user = input("Data to be stored: ")
    writing.write(input_user)"""

""" The write() function does not add lines to the string. To add line break in
write() instruction can be done by inserting an \n"""

write_line = 'text_files\linebreak.txt'

with open(write_line, 'w') as writing1:
    writing1.write("Inserting new lines\n")
    writing1.write("To this file\n")

# We can concatenate data into a file:
""" We can add more data to a file instead of overwrite the existing data. We can
do that by opening a file in the concat mode 'a'."""

concat_test = 'text_files\linebreak.txt'

with open(concat_test, 'a') as concat:
    i = 0
    while(i < 10):
        concat.write("Adding more and more information + 1\n")
        i += 1
