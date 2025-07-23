#!/usr/bin/python3
def get_random_word():
    import random
    with open("wordlist.txt") as list:
        text = list.read().strip()
    word = text.split()
    random_word = random.choice(word)
    print(random_word)


get_random_word()
