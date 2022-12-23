""" Open a text file and write what we've learned so far in Python. After that, write a program that
reads and show what we've written"""

learning_python = 'texts\learning_python.txt'

""" To print the entire archive"""
with open(learning_python, 'r') as learning: 
    full_text = learning.read()
    print(full_text.rstrip())  

""" To print the archive using a string to store the content"""
with open(learning_python) as file_object:
    lines = file_object.readlines()

file_string = ''

for line in lines:
    file_string += line.rstrip()

print(file_string.rstrip())
print("This file contains:",len(file_string)," characters")

""" To print the content using a for loop"""
with open(learning_python) as text:
    text_loop = text.readlines()

for line in text_loop:
    print(line.rstrip())

""" Change all Python reference to COBOL"""
with open(learning_python) as learn_cobol:
    replace_text = learn_cobol.readlines()

for text in replace_text:
    print(text.replace('Python','COBOL'))