#!/usr/bin/python3

class HangmanGame:
    def __init__(self, word):
        self.word = word
        self.guessed_letters = []
        self.max_errors = 6
        self.errors = 0

    def display_progress(self):
        result = ''
        for letter in self.word:
            if letter in self.guessed_letters:
                result += letter + ' '
            else:
                result += '_ '
        return result.strip()
