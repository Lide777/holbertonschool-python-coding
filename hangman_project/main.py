#!/usr/bin/python3

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
    guessed_letters = []  # Example list of letters already guessed
    letter = get_valid_guess(guessed_letters)
    print(f"Valid letter received: {letter}")
