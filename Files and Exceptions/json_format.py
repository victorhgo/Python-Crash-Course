""" We can store simple data structures into a JSON file."""

""" JSON: JavaScript Object Notation """

# json.dump() and json.load()

""" The first method to use is the json.dump() that dumps the data into the json file.
It has two arguments: a data to be stored and a file object that will receive the data"""
# Import the json libraries:
import json

names = ['victor hugo','albert einstein','julian gomez','ana de armas']

filename = 'text_files\\names.json'

with open(filename, 'w') as file_object:
    json.dump(names, file_object)

# Now we can use the json.load() method to visualize the data:
with open(filename) as file_object:
    names = json.load(file_object)

print(names)