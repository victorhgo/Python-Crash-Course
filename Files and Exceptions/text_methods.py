""" This function will allow us to count the words in books"""

def count_words(filename):
    try:
        with open(filename, encoding='utf-8') as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        print(f"File {filename} not found")
    else:
        words = contents.split()
        word_count = len(words)
        print(f"The file {filename} has approximatelly {word_count} words")

