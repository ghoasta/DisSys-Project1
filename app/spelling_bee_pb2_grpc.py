# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import spelling_bee_pb2 as spelling__bee__pb2


class SpellingBeeStub(object):
    """The greeting service definition.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.sayHello = channel.unary_unary(
                '/app.SpellingBee/sayHello',
                request_serializer=spelling__bee__pb2.Empty.SerializeToString,
                response_deserializer=spelling__bee__pb2.WorkPangram.FromString,
                )
        self.sendWork = channel.unary_unary(
                '/app.SpellingBee/sendWork',
                request_serializer=spelling__bee__pb2.Word.SerializeToString,
                response_deserializer=spelling__bee__pb2.Points.FromString,
                )


class SpellingBeeServicer(object):
    """The greeting service definition.
    """

    def sayHello(self, request, context):
        """Sends a greeting
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def sendWork(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SpellingBeeServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'sayHello': grpc.unary_unary_rpc_method_handler(
                    servicer.sayHello,
                    request_deserializer=spelling__bee__pb2.Empty.FromString,
                    response_serializer=spelling__bee__pb2.WorkPangram.SerializeToString,
            ),
            'sendWork': grpc.unary_unary_rpc_method_handler(
                    servicer.sendWork,
                    request_deserializer=spelling__bee__pb2.Word.FromString,
                    response_serializer=spelling__bee__pb2.Points.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'app.SpellingBee', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class SpellingBee(object):
    """The greeting service definition.
    """

    @staticmethod
    def sayHello(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/app.SpellingBee/sayHello',
            spelling__bee__pb2.Empty.SerializeToString,
            spelling__bee__pb2.WorkPangram.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def sendWork(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/app.SpellingBee/sendWork',
            spelling__bee__pb2.Word.SerializeToString,
            spelling__bee__pb2.Points.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
