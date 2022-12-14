# Functions are code blocks named, they are defined to perform specific tasks.
# When we want to execute a function, we call it by name. It's useful to work with functions when the program gets bigger and bigger.

# The simplest form of function to greet the user:
def greet_user(): 
    """Simple Function"""
    print("Hello user")

greet_user()

# We can insert information on a function:
def greet_user(username):
    """Inserting information"""
    print('Hello ' + username.title())

greet_user('victor')

# Arguments and parameters:
# The parameter of a function is what we defined during the function definition.
# The argument is when we call the function and specify the argument. In our example above, username is the parameter and
# victor is the argument.

# We can put arguments on the function using insert():
def favorite_game(game_name):
    print('My favorite game is ' + game_name.title())

favorite_game(input('Game: '))

# Positional Arguments:
def describe_game(game_genre, game_name):
    print("\nOne example of a " + game_genre.title() +
    ' game is ' + game_name.title() + '.')

describe_game('rpg','skyrim')

# Named Arguments: (keyword argument)
def describe_book(book_genre, book_name):
    print("I have a(n) " + book_genre.title() + ' book called ' 
    + book_name.title())

describe_book(book_name='the hobbit',book_genre='adventure')

# Default parameter:
def favorite_movie(movie_title, movie_genre='scientific fiction'):
    print("My favorite " + movie_genre.title() + ' movie is '
    + movie_title.title() + '!')

favorite_movie(movie_title='interstellar')

# Returning values:

# Return a simple value:
# A function to return first and last name formatted:
def formatted_name(first_name, last_name):
    """Return a name formatted"""
    full_name = first_name + ' ' + last_name
    return full_name.title()

person = formatted_name('george', 'harrison')

print(person)

# Returning a Dictionary:
# A function can return simple and more complex data structure such as lists and dictionaries:

# The following function receives name and returns a dictionary:
def build_character(first_name, last_name, age):
    character = {'first': first_name, 'last':last_name}
    if age:
        character['age'] = age
    return character

musician = build_character('paul','mccartney',age=81)
print(musician)

# Using functions with a While loop:
# Let's use the formatted_name() function to greet the users:
def formatted_name(first_name, last_name):
    full_name = first_name + ' ' + last_name
    return full_name.title()

while True:
    print("\nWhat's your name? Enter q to quit")
    f_name = input('First name: ')
    if f_name == 'q':
        break
    l_name = input('Last name: ')
    if l_name == 'q':
        break
    form_name = formatted_name(f_name, l_name)

    print("Hello, " + form_name + "!")

# Functions to work with lists:
def greet_names(names):
    for name in names:
        message = "Hello" + name.title() + '.'
    print(message)

# Our list with the names
usernames = ['victor','gomez','wanda','rowenna']
greet_names(usernames)

# --------------------------------------------- #

# Modify a list in a function:
unready_instruments = ['bass','violin','cello']
completed_instruments = []

# To simulate the making of each instrument:
while unready_instruments:
    # To move from the project area to the production: 
    current_production = unready_instruments.pop()
    print("Making the: " + current_production)
    completed_instruments.append(current_production)

    print("The following instruments are ready to be shipped: ")
    for completed_instrument in completed_instruments:
        print(completed_instrument.title())

# The above program can be rewritten using two funcions:
# The first function is to make the instruments:
def make_instrument(unready_instruments,completed_instruments):
    while unready_instruments:
        """ To move from the project area to the production: """
        current_production = unready_instruments.pop()
        print("Making the: " + current_production.title())
        completed_instruments.append(current_production)

# To show each ready to be shipped instruments:
def ready_shipping(completed_instruments):
    print("The following instruments are ready to be shipped: ")
    for completed_instrument in completed_instruments:
        print(completed_instrument.title())

# Instrument list
unready_instruments = ['guitar','acoustic guitar','bass']
completed_instruments = []

make_instrument(unready_instruments, completed_instruments)
ready_shipping(completed_instruments)

""" We can avoid to modify a list using the slice method by sending a copy of the list to the function. For instance:
  In the example bellow, instead of sending the unready_instruments list to the function,
  we could simply create a copy of the list:
  funcion_name(list_name[:]) """

# A function can receive an arbitrary amount of arguments:
def make_icecream(*toppings):
    """List of ordered toppings"""
    print(toppings)

make_icecream('chocolate')
make_icecream('caramel','strawberry','nutella')

# The * tells Python to create an empty tuple to receive the data from the user

# We can blend positional argument with arbritary ones:
def make_icecream(flavour,*toppings):
    print(" Making a(n) " + flavour.title() + 
    ' ice cream with the following toppings: ')
    for topping in toppings:
        print("- " + topping)

make_icecream('vanilla','cherry','chocolate')
