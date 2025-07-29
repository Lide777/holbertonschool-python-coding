from game import HangmanGame


def main():
    game = HangmanGame()
    olders = set()

    while True:
        print("\nMot actuel :", game.display_progress())
        guessed_letter = input(
            'Entrez une lettre (ou "exit" pour quitter) : ').strip().lower()

        if guessed_letter == 'exit':
            print("À bientôt !")
            break

        if len(guessed_letter) != 1:
            print('Vous devez entrer une seule lettre.')
            continue
        elif not guessed_letter.isalpha():
            print('Ce doit être une lettre.')
            continue
        elif guessed_letter in olders:
            print('Lettre déjà essayée.')
            continue
        else:
            olders.add(guessed_letter)
            game.guess(guessed_letter)

        if game.is_won():
            print(f"\nBravo, tu as gagné Shrek va t'embrasser! Le mot était : {game.word}")
            break
        elif game.is_lost():
            print(f"\nTu as perdu. Shrek n'est pas content! Le mot était : {game.word}")
            break


if __name__ == "__main__":
    main()
