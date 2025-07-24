#!/usr/bin/python3

from hangman_game import HangmanGame


def get_valid_guess(guessed_letters):
    while True:
        guess = input("Guess a letter: ").lower()
        if len(guess) != 1:
            print("Error: please enter exactly one letter.")
        elif not guess.isalpha():
            print("Error: that is not a valid letter.")
        elif guess in guessed_letters:
            print("Error: you have already guessed that letter.")
        else:
            return guess


if __name__ == "__main__":
    guessed_letters = []
    letter = get_valid_guess(guessed_letters)
    print(f"Valid letter received: {letter}")


def main():
    word = "python"
    game = HangmanGame(word)

    while not game.is_won() and not game.is_lost():
        print("\nCurrent word:", game.display_progress())
        guess = input("Enter a letter: ").strip().lower()
        if not guess or len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Enter one letter.")
            continue

        if game.guess(guess):
            print("Good guess!" if guess in word else "Wrong guess.")
        else:
            print("You already guessed that letter.")

        print(f"Errors: {game.errors}/{game.max_errors}")

    # Game end
    if game.is_won():
        print(f"\nYou won Shrek will kiss you! The word was: {game.word}")
    else:
        print(f"\nGame over. The word was: {game.word}")


if __name__ == "__main__":
    main()
