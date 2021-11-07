import json
from random import randint

pangrams = {}

def is_pangram(word_in):
    if len(set(word_in)) == 7 and 's' not in word_in:
        return True
    else:
        return False

def choose_word():
    with open("../dictionary/words_dictionary.json") as json_file:
        words = json.load(json_file)

    for word in words:
        if is_pangram(word):
            pangrams[word] = ""

    with open("../dictionary/pangrams.json", "w") as pangram_file:
        json.dump(pangrams, pangram_file)

    # Pick a random pangram
    rand_num = randint(0, len(pangrams))
    random_pangram = list(pangrams.keys())[rand_num]

    return random_pangram


def checkPangram(word):
    #with open("../dictionary/words_dictionary.json") as f:
    #    words = json.load(f)

    #with open("../dictionary/pangrams.json", "w") as pangram_file:
    #    pangram = json.load(pangram_file)

    #if word not in words:
    #    points = 0
    #    message = "Invalid word"
    #    return message, points

    if len(word) < 4:
        points = 0
        message = "Word shorter then 4 letters"
        return message, points

    if len(word) == 4:
        points = 1
        message = f"Valid word! You get ({points})"
        return message, points

    else:
        points = len(word)
        message = f"Valid word! You get ({points})"
        return message, points