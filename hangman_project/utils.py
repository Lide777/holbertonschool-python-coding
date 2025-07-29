import random

def get_random_word():
    try:
        with open("wordlist.txt", encoding="utf-8") as file:
            words = file.read().strip().split()
        return random.choice(words)
    except FileNotFoundError:
        print("Erreur : le fichier 'wordlist.txt' est introuvable.")
        return "python" 