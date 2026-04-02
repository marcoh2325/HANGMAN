# Code to get words to fill words.txt
# words.txt is a file with all the words that the game can use
# (a word per line)

# In this version the words are obtained from three books
from string import whitespace, punctuation, digits

CHARACTERS_TO_REMOVE = whitespace + punctuation + digits

def separate_words(content):
    """Separate words from a text"""
    word = ""
    words = []
    for c in content:
        if c in CHARACTERS_TO_REMOVE:
            if word:
                words.append(word.lower())
            word = ""
        else:
            word += c
    
    if word:
        words.append(word)
    return words

if __name__ == "__main__":

    books = ["data/The_Picture_of_Dorian_Gray.txt",
            "data/Treasure_Island.txt",
            "data/Frankenstein.txt"]
    content = ""
    for book_name in books[:1]:
        with open(book_name, encoding='utf-8') as f:
            content += f.read()

    words = separate_words(content)
    words = set(words)
    # TO DO write words in file
    with open("data/words.txt", "w", encoding='utf-8') as f:
        for word in words:
            f.write(word)
            f.write("\n")
