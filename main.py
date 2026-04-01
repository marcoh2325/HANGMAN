import json
from random import choice
# TO DO: modify json or input so there's more words
# TO DO: look for a way to get a random word in json more efficiently
def print_hangman_game_state(visible_word, attempts):
    print(visible_word)
    # TO DO: change this for a function that draws the hangman
    print(attempts)

def play_hangman():
    with open("words.json") as json_file:
        json_words = json.load(json_file)

    word = choice(json_words['words'])
    print(word)
    print("hey I'm playing the hangman")
    word_guessed = False
    attempts = 0
    max_attempts = 10
    visible_word = "_" * len(word) 
    print_hangman_game_state(visible_word, attempts)
    while not word_guessed or attempts < max_attempts:
        user_character = input("Introduce a character: ")
        if user_character in word:
            for i in range(len(word)):
                if word[i] == user_character:
                    # TO DO: CORRECT, visible_word can't be modified
                    # because is a string
                    visible_word[i] = user_character
            print_hangman_game_state(visible_word, attempts)

if __name__ == '__main__':


    play_again = 'y'
    while play_again == 'y' or play_again == 'yes':
        play_hangman()
        play_again = input("Do you want to play again? y/n\n").lower()
    print("Thanks for playing! Until next time")
