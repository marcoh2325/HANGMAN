# HANGMAN

A version of the hangman game.
In this game a random word is obtained from a file of words. The user must guess characters until is able to
guess the word. If the user doesn't guess the word before some number of attempts, the user loses the game.
Otherwise the user wins.

In this version the words to guess for the game are obtained from the books:
Frankenstein; or, the modern prometheus by Mary Wollstonecraft Shelley,
Treasure Island by Robert Louis Stevenson, 
The Picture of Dorian Gray by Oscar Wilde

The content of the books is processed in the file get_words.py and the words stored in the file words.txt
The books can be download from Project Gutemberg https://www.gutenberg.org/
You may choose the books that you want or modify get_words.py so it fill it's self from other source.
There's repositories like https://github.com/dwyl/english-words or https://www.mit.edu/~ecprice/wordlist.10000 (contains some words that may not be good choices for the game like dv, or dvd)
that can also be used and some python libraries (NLTK) and os like linux and mac contain also english words
But I decided to get the words this way in this version
Problems: 
- By using this method without a dictionary to check if such words exist or not, some non words like "www" are included
However the chance of getting those to guess is seems quite low.
