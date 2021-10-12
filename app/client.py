from __future__ import print_function

import logging

import grpc
import spelling_bee_pb2
import spelling_bee_pb2_grpc


def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.

    print("This is a spelling bee!")
    word = input("Enter word >> ")

    with grpc.insecure_channel('localhost:50051') as channel:
        stub = spelling_bee_pb2_grpc.GreeterStub(channel)
        response = stub.SayHello(spelling_bee_pb2.HelloRequest(name='you'))
    print("Greeter client received: " + response.message)


if __name__ == '__main__':
    logging.basicConfig()
    run()