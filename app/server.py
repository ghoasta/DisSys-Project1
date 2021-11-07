from concurrent import futures
import logging

import grpc
import spelling_bee_pb2, spelling_bee_pb2_grpc
from calculations import choose_word
from calculations import checkPangram

#pangrams = {}


class SpellingBeeServer(spelling_bee_pb2_grpc.SpellingBeeServicer):

    def sayHello(self, request, context):
        #just send the pangram back to client
        return spelling_bee_pb2.WorkPangram(pangram=pangram_word)

    def sendWork(self, request, context):
        #pangram = pangram_word
        messege, points = checkPangram(request.word)
        return spelling_bee_pb2.Points(messege=messege, points=points, pangram=pangram_word)

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
