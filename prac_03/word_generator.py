def is_valid_format(word):
    if word_format == True:
        print("Word format is True")
    else:
        print("Word format is False")
    return word

import random

VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"

word_format = "ccvcvvc"
word = ""
for kind in word_format:
    if kind == "c":
        word += random.choice(CONSONANTS)
    else:
        word += random.choice(VOWELS)

print(is_valid_format(word))
