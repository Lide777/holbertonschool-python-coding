#!/usr/bin/python3
import random


def get_random_word():
    with open("wordlist.txt") as f:
        return random.choice([w.strip() for w in f if w.strip().isalpha()])
