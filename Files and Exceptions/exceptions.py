""" Exceptions are used to manage errors during execution"""

# ZeroDivisionError

""" Let's do a division by zero and see what happens:"""
# print(1/0)

# Here's the output for this error:

"""Traceback (most recent call last):
  File "exceptions.py", line 6, in <module>
    print(1/0)
ZeroDivisionError: division by zero"""

# Using try-except blocks:

""" We use this blocks to treat one exception if happens during the program execution"""

try:
    print(1/0) 
except ZeroDivisionError:
    print("You can't divide by zero!")

# Now the output: You can't divide by zero!

# We can use exceptions to avoid failures:
print("Give me two numbers to be divided. Enter 'q' to leave: ")

while True:     
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("\nEnter the second number:")
    if second_number == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("Yu can't divide by zero")
    else:
        print(answer)




