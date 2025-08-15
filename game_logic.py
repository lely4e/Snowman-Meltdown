from ascii_art import STAGES, WON
import random
import sys

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]


def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


def display_welcome_message():
    """Displays the welcome message."""
    print("* " * 17)
    print("WELCOME TO SNOWMAN MELTDOWN GAME!")
    print("* " * 17)


def validate_input_guess(user_input):
    """Validates if the user guess is a single alphabetical character."""
    return len(user_input) == 1 and user_input.isalpha()


def play_game():
    """Play a game of Snowman-Meltdown."""
    secret_word = get_random_word()
    mistakes = 0
    guessed_letters = []

    display_welcome_message()

    while True:
        display_game_state(mistakes, secret_word, guessed_letters)

        # Check if the user won
        if set(secret_word).issubset(guessed_letters):
            print(WON[0])
            print("Congratulations, you saved the snowman!\n")
            new_round()

        # Check if the user lose
        if mistakes >= len(STAGES) - 1:
            print("\nGame over! The word was:", secret_word)
            print(STAGES[-1])
            new_round()

        # Prompt the user until the game end
        guess = input("Guess a letter: ").strip().lower()
        valid_guess = validate_input_guess(guess)

        # Check if letter in secret word
        if valid_guess:
            if guess in secret_word and guess not in guessed_letters:
                guessed_letters.append(guess)
            elif guess in guessed_letters:
                print("You already guessed that letter.")
            else:
                mistakes += 1
        else:
            print("Invalid Input. Please enter exactly one letter\n")
            continue


def display_game_state(mistakes, secret_word, guessed_letters):
    """Displays the current game state."""
    print(STAGES[mistakes])

    guessed_word = ""

    for letter in secret_word:
        if letter in guessed_letters:
            guessed_word += letter + " "
        else:
            guessed_word += "_ "

    print("Word: ", guessed_word.strip(), "\n")


def new_round():
    """Check if the user wants to play again."""
    while True:
        user_answer = input("Do you want to play again? (Y/N)").strip().upper()
        if user_answer == "Y":
            play_game()
        elif user_answer == "N":
            print("Goodbye!")
            sys.exit()
        else:
            print("Sorry, I didn't understand that. Please enter 'Y' or 'N'.\n")
            continue




