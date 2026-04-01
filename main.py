import json
from random import choice

# TO DO: look for a way to get a random word in json more efficiently
def get_visible_word(word, characters_to_show):
    """Prints word with only the guessed characters"""
    visible_word = ""
    for c in word:
        if characters_to_show[c]:
            visible_word += c
        else:
            visible_word += "_"
    return visible_word

def print_hangman_game_state(visible_word, attempts):
    """Prints the state of the hangman and the word"""
    # TO DO: change this for a function that draws the hangman
    print(visible_word)
    print(attempts)

def play_hangman():
    """Hangman game. 
    difficulty: indicates the difficulty of the game, with 0 being easy,
    1 being medium and 2 being hard"""
    # TO DO: Find a dictionary or api where to get words
    # TO DO: modify json or input so there's more words (maybe I can
    # get the words from an api
    with open("data/words.txt") as f:
        words = f.read()

    word = choice(words.split("\n"))
    word_guessed = False
    attempts = 0
    max_attempts = 10
    characters_to_show = dict()
    # TO DO: Modify game so there's different difficulties
    # hard: 0 help, medium: 1 character, easy: 2 characters shown
    # difficulty by lenght or characters?
    # character_to_show is a dictionary where the keys are
    # the word characters and the values are False if
    # that character must not be shown and True otherwise
    for c in set(word):
        characters_to_show[c] = False
    visible_word = get_visible_word(word, characters_to_show)
    print(visible_word)
    print_hangman_game_state(visible_word, attempts)
    while not word_guessed and attempts < max_attempts:
        character_guess = input("Introduce a character: ")
        if character_guess in word:
            characters_to_show[character_guess] = True
        else:
            attempts += 1
        visible_word = get_visible_word(word, characters_to_show)
        if word == visible_word:
            word_guessed = True
        print_hangman_game_state(visible_word, attempts)

    if word_guessed:
        print("You won")
    else:
        print("You lose")

if __name__ == '__main__':
    play_again = 'y'
    while play_again == 'y' or play_again == 'yes':
        play_hangman()
        play_again = input("Do you want to play again? y/n\n").lower()
    print("Thanks for playing! Until next time")