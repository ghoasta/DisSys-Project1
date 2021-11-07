from __future__ import print_function

import logging

import grpc
import spelling_bee_pb2, spelling_bee_pb2_grpc


def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = spelling_bee_pb2_grpc.SpellingBeeStub(channel)
    check_word = stub.sayHello(spelling_bee_pb2.Empty())
    print("*"*20)
    print("This is a spelling bee!")
    while(True):
        print("Your pangram for today is: " + check_word.pangram)
        print("*" * 20)
        print("type exit to exit")
        word_input = input("Enter word >> ")
        word_input = word_input.lower()
        if word_input == "exit":
            print("bye bye")
            break


        #response = stub.SayHello(spelling_bee_pb2.HelloRequest(name='you'))
        #response = stub.SayHello(spelling_bee_pb2.HelloRequest(name=word_input))
        #print("Message from server: " + response.message)

    #response = stub.SendWord(spelling_bee_pb2.SendWordRequest(word='sdasd'))
    #print ("Answer = " + response.word)


    #print("*"*20)
    #with grpc.insecure_channel('localhost:50051') as channel:
    #    stub = spelling_bee_pb2_grpc.SpellingBeeStub(channel)
    #    response = stub.SendWord(spelling_bee_pb2.SendWordRequest(word=word_input))
    #print("Did you guessed the word? => " + response.word)

if __name__ == '__main__':
    logging.basicConfig()
    run()