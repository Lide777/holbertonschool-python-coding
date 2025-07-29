from utils import get_random_word


class HangmanGame:
    def __init__(self, word=None, guessed_letters=None, max_error=15, error=0):
        self.__word = word or get_random_word()
        self.guessed_letters = guessed_letters or set()
        self.max_error = max_error
        self.error = error

    @property
    def word(self):
        return self.__word

    @word.setter
    def word(self, value):
        self.__word = value

    def display_progress(self):
        return ' '.join([
            letter if not letter.isalpha() or letter in self.guessed_letters else '_'
            for letter in self.__word
        ])

    def guess(self, letter):
        letter = letter.lower()

        if letter in self.guessed_letters:
            print("Tu as déjà essayé cette lettre.")
        elif letter in self.__word:
            self.guessed_letters.add(letter)
            print("Bonne réponse !")
        else:
            self.guessed_letters.add(letter)
            self.error += 1
            print("Mauvaise réponse.")

        print(self.display_progress())
        print(f"Erreurs : {self.error}/{self.max_error}")

    def is_won(self):
        return all(
            letter in self.guessed_letters
            for letter in self.__word
            if letter.isalpha()
        )

    def is_lost(self):
    return self.error >= self.max_error
