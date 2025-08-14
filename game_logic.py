from ascii_art import STAGES
from snowman import WORDS
import random
import sys


def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


def play_game():
    secret_word = get_random_word()
    print("Secret word: " + secret_word)
    mistakes = 0
    guessed_letters = []

    # Displaying Welcome message
    print("Welcome to Snowman Meltdown!")
    print(STAGES[0])
    print("Word: ", len(secret_word) * "_ ", "\n")

    while True:
        # Prompt the user until the game end
        guess = input("Guess a letter: ").lower()
        if guess in secret_word and guess not in guessed_letters:
            guessed_letters.append(guess)
        else:
            mistakes += 1
        display_game_state(mistakes, secret_word, guessed_letters)

        #print("You guessed:", guess)


def display_game_state(mistakes, secret_word, guessed_letters):
    """Displays the game state."""
    if mistakes < 3:
        print(STAGES[mistakes])
    else:
        print("Game over! The word was:", secret_word)
        print(STAGES[mistakes])
        sys.exit()

    guessed_word = ""

    for letter in secret_word:
        if letter in guessed_letters:
            guessed_word += letter + " "
        else:
            guessed_word += "_ "

    print("Word: ", guessed_word )