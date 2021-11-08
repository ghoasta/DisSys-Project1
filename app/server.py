from concurrent import futures
import logging

import grpc
import spelling_bee_pb2, spelling_bee_pb2_grpc
from calculations import Calculations

class SpellingBeeServer(spelling_bee_pb2_grpc.SpellingBeeServicer):

    def sayHello(self, request, context):
        new_word = new_single.visual(pangram_word.upper())
        return spelling_bee_pb2.WorkPangram(pangram=new_word)

    def sendWork(self, request, context):
        messege, points = new_single.checkPangram(request.word, pangram_word)
        return spelling_bee_pb2.Points(messege=messege, points=points, pangram=pangram_word)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    spelling_bee_pb2_grpc.add_SpellingBeeServicer_to_server(SpellingBeeServer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    new_single = Calculations()
    pangram_word = new_single.choose_word()
    print("Server starting")
    print(pangram_word.upper())
    serve()
