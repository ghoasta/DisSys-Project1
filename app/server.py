from concurrent import futures
import logging

import grpc
import spelling_bee_pb2
import spelling_bee_pb2_grpc
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


class SpellingBeeServer(spelling_bee_pb2_grpc.SpellingBeeServicer):

    def SayHello(self, request, context):
        #print(word)
        if request.name == pangram_word:
            return spelling_bee_pb2.HelloReply(message='Correct guess: %s!' % request.name)
        else:
            return spelling_bee_pb2.HelloReply(message='Incorrect guess: %s!' % request.name)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    spelling_bee_pb2_grpc.add_SpellingBeeServicer_to_server(SpellingBeeServer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    pangram_word = (choose_word())
    print(pangram_word)
    serve()
