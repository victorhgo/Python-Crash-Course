""" We can work with text file that contains whole blocks. A lot of books are available in
text files and some can be downloaded in http://gutenberg.org/for free.
To begin this study, we will use the book Alice in Wonderland"""

# The split() method is very useful when using texts:

""" The split() method will take the title of this book as and example and we can do something like that:"""
# title = "Alice in Wonderland"
# title.split() ['Alice', 'in', 'Wonderland']

# The split separates the words when it finds a blank space.

# Let's open the book as alice.txt

alice = 'text_files\\alice.txt'
book_title = 'Alice in Wonderland'

try:
    with open(alice, encoding='utf-8') as book:
        contents = book.read()
except FileNotFoundError:
    print("The file " + alice + ' does not exist.')
else:
    words = contents.split()
    word_count = len(words)
    print(f"The book {book_title} has about {word_count} words.")

# Let's import the text_method modules with count_words function:
from text_methods import *

filename = 'text_files\\alice.txt'

count_words(filename)

""" Now let's analyse different books"""

books = ['text_files\\dracula.txt', 'text_files\\successful_stories.txt','text_files\\alice.txt']

for filename in books:
    count_words(filename)

