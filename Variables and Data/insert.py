# The input() function is used to insert data from the user. After Python receives the data
# it is stored into a variable to be used within the program.
# To display simple message from the user:
# message = input("Write anything you like: ")
# print(message)

# A simple way to do that is:
# print(input('Enter something: '))

# If we want to enter numeric data, we use the int() function.

# print(int(input('How old are you? ')))

# How tall are you?

#height = input('Hoow tall are you? ')
#height = float(height)

#if height >= 1.7:
#    print("You are tall enought to enlist the army!")
#else:
#    print("You aren't tall enought to enlist the army! ")

# While...

#current_number = 1

#while current_number <= 5:
#    print(current_number)
#    current_number += 1

# The user can say if he wants to leave:
#prompt = "\tSay something. Enter 'quit' to leave: "
#message = ""

#while message != 'quit':
#    message = input(prompt)

#    if message != 'quit':
#        print(message)

# Using flags
# We will create a flag named active to control if the program should continue or not:
prompt = "\tSay something. Enter 'quit' to leave: "
message = ""

active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)

# Using break to leave a while loop:
prompt = 'Enter a name: '
prompt += "\nEnter 'quit' when you finish: "

while True: 
    name = input(prompt)
    if name == 'quit':
        break
    else:
        print("Nice to meet you, " + name.title() + '.')

# Using continue in a loop:
# We can use continue to return to the beginning of the program:
current_number = 0

while current_number < 10:
    current_number += 1
    if current_number % 2 == 0: # Print the odds
        continue
    print(current_number)

# Using while loop with lists and dictionaries:
# A for loop might be efficient to run a list, but we should avoid modifying a list
# using the for loop. We shall have problems to keep the control of items in a list.
# To modify a list while working with them, we should use a while loop.
# Using while loops with lists and dictionaries allow us to colect, store and sort a lot of inputs and outputs.

# Moving items from one list to another:

# Creating a list to confirm users:
unconfirmed_users = ['victor', 'alisson', 'gabriel']
confirmed_users = []

# Confirms each users:
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user)

print("The following users were successfully confirmed:")

for confirmed_user in confirmed_users:
    print(confirmed_user.title())

# Removing each instance of specific values in a list


# End of Chapter