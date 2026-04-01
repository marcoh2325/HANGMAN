# Code to get words to fill words.txt
# a file with all the words that the game can use
# (a word per line)



# In this version the words are obtained from three book
from string import whitespace, punctuation

CHARACTERS_TO_REMOVE = whitespace + punctuation

def separate_words(content):
    """Separate words from a text"""
    start_word = True
    end_word = False
    for c in content:
        if c in CHARACTERS_TO_REMOVE:
            pass


books = ["data/The_Picture_of_Dorian_Gray.txt",
         "data/Treasure_Island.txt",
         "data/Frankenstein.txt"]
content = ""
for book_name in books[:1]:
    with open(book_name, encoding='utf-8') as f:
        content += f.read()

print(content)