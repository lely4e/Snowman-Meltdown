from ascii_art import STAGES
import random
import sys

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]


def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


def play_game():
    """Play a game of Snowman-Meltdown."""
    secret_word = get_random_word()
    print("Secret word: " + secret_word)
    mistakes = 0
    guessed_letters = []

    # Displaying Welcome message
    print("* " * 17)
    print("WELCOME TO SNOWMAN MELTDOWN GAME!")
    print("* " * 17)
    print(STAGES[0])
    print("Word: ", len(secret_word) * "_ ", "\n")

    while True:
        # Prompt the user until the game end
        guess = input("Guess a letter: ").lower()
        if len(guess) > 1 or not guess.isalpha():
            print("It must be exactly one letter\n")
            continue

        if guess in secret_word and guess not in guessed_letters:
            guessed_letters.append(guess)
        elif guess in guessed_letters: #________________________
            print("You already guessed that letter.")
        else:
            mistakes += 1
        display_game_state(mistakes, secret_word, guessed_letters)


def display_game_state(mistakes, secret_word, guessed_letters):
    """Displays the game state."""
    if mistakes < 3:
        print(STAGES[mistakes])
    else:
        print("\nGame over! The word was:", secret_word)
        print(STAGES[mistakes])
        new_round()

    guessed_word = ""

    for letter in secret_word:
        if letter in guessed_letters:
            guessed_word += letter + " "
        else:
            guessed_word += "_ "

    # Check if the user win
    if "_" not in guessed_word:
        print("Congratulations, you saved the snowman!\n")
        new_round()
    else:
        print("Word: ", guessed_word, "\n")


def new_round():
    """Check if the user wants to play again."""
    while True:
        user_answer = input("Do you wanna play one more time? (Y/N)").upper()
        if user_answer == "Y":
            play_game()
        elif user_answer == "N":
            print("Goodbye!")
            sys.exit()
        else:
            print("Sorry, I didn't understand that.")
            continue




