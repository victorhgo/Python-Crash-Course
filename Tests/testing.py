""" We can test our code using some methods. When testing our code we can guarantee that our
program is working as expected and no bugs will interfer."""

# The module that we will be using is the unittest.

""" We will learn how to create a test case and verify if a set of input results in the 
desired output. We will know a test that pass and a test that does not, and finally, 
we will learn howto test functions and classes and learn which tests must be written 
in a project."""

# Testing a function

""" We will be using a simple function to write the tests"""

def get_formatted_name(first_name,last_name):
    full_name = first_name + ' ' + last_name
    return full_name.title()

print("Enter 'q' to quit")
"""
while True:
    first_name = input("What's your first name: ")
    if first_name == 'q':
        break
    last_name = input("What's your last name: ")
    if last_name == 'q':
        break
    formatted_name = get_formatted_name(first_name, last_name)
    print("Name: " + formatted_name + '.') """

# Unit tests and test cases.
""" The unit test verifies if the specific aspect of a function behavior will be the expected for 
each input of a function."""

# A test that will pass.
""" The sintax to create a test case needs some practice to learn. To create a test case we import the unittest"""
import unittest

class NameTestCase(unittest.TestCase):
    def test_first_last_name(self):
        formatted_name = get_formatted_name('jimi','hendrix')
        """ The assert method is the most useful resource from unittest. They verify
        if a received result is equal the result we are expecting."""
        self.assertEqual(formatted_name, 'Jimi Hendrix')

# To start the file tests
unittest.main()

# Finish this chapter, page 260
