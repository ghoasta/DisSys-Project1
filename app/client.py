from __future__ import print_function

import logging

import grpc
import spelling_bee_pb2, spelling_bee_pb2_grpc


def run():
    total_points = 0
    channel = grpc.insecure_channel('localhost:50051')
    stub = spelling_bee_pb2_grpc.SpellingBeeStub(channel)
    check_word = stub.sayHello(spelling_bee_pb2.Empty())
    print("*"*20)
    print("This is a spelling bee!")
    while(True):
        print("Your pangram for today is: \n" + check_word.pangram.upper())
        print("")
        print("type exit to exit")
        word_input = input("Enter word >> ")
        word_input = word_input.lower()
        if word_input == "exit":
            print("bye bye")
            break
        response = stub.sendWork(spelling_bee_pb2.Word(word=word_input))
        total_points = total_points + response.points
        print(f"{response.messege} Current points: [{total_points}]")

if __name__ == '__main__':
    logging.basicConfig()
    run()