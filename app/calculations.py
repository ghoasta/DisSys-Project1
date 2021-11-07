import json
import random
import threading

class Calculations:
    #singleton
    __instance = None
    @staticmethod
    def get_instance():
        if Calculations.__instance is None:
            with threading.Lock():
                if Calculations.__instance is None:
                    Calculations()
        return Calculations.__instance

    def __init__(self):
        if Calculations.__instance is not None:
            raise Exception("This is a singleton!")
        else:
            Calculations.__instance = self

        with open("../dictionary/pangrams.json") as pangram_file:
            self.pangram = json.load(pangram_file)

        with open("../dictionary/words_dictionary.json") as words_dict_file:
            self.words_dict = json.load(words_dict_file)

        middle_letter = ""

    def choose_word(self):
        while True:
            pangram = random.choice(list(self.pangram.keys()))
            pangram_letter = list(set(pangram))
            if len(pangram) ==7 and len(pangram_letter) == 7 and 's' not in pangram_letter:
                break
        return pangram
    pass



    def visual(self,word):
        word_list = list(word)
        word_list.insert(3,'[')
        word_list.insert(5,']')
        new_word = ""
        return new_word.join(word_list)

    def find_middle(self,word):
        middle_letter = word[3]
        return middle_letter

    def checkPangram(self, word,pangram):

        if len(word) < 4:
            points = 0
            message = "Word shorter then 4 letters"
            return message, points

        if word not in self.words_dict:
            points = 0
            message = "Not a valid word"
            return message, points

        if pangram[3] in word:
            if len(word) == 4:
                points = 1
                message = f"Valid word! You get ({points})"
                return message, points
            elif len(word) == 7:
                points = len(word) + 7
                message = f"You have find Pangram! You get ({points})"
                return message, points
            else:
                points = len(word)
                message = f"Valid word! You get ({points})"
                return message, points
        else:
            message = "You need middle letter"
            points = 0
            return message, points

    pass




