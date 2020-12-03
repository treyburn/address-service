# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from addresspb import address_pb2 as addresspb_dot_address__pb2


class AddressParseServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.AddressParse = channel.unary_unary(
                '/address.AddressParseService/AddressParse',
                request_serializer=addresspb_dot_address__pb2.APRequest.SerializeToString,
                response_deserializer=addresspb_dot_address__pb2.APResponse.FromString,
                )


class AddressParseServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def AddressParse(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_AddressParseServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'AddressParse': grpc.unary_unary_rpc_method_handler(
                    servicer.AddressParse,
                    request_deserializer=addresspb_dot_address__pb2.APRequest.FromString,
                    response_serializer=addresspb_dot_address__pb2.APResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'address.AddressParseService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class AddressParseService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def AddressParse(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/address.AddressParseService/AddressParse',
            addresspb_dot_address__pb2.APRequest.SerializeToString,
            addresspb_dot_address__pb2.APResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)