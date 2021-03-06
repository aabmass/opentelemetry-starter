# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from foodfinder.vendor import vendor_pb2 as foodfinder_dot_vendor_dot_vendor__pb2


class VendorStub(object):
    """*
    Gives inventory and price of item from the given vendor
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.queryInventory = channel.unary_unary(
                '/foodfinder.vendor.Vendor/queryInventory',
                request_serializer=foodfinder_dot_vendor_dot_vendor__pb2.QueryInventoryRequest.SerializeToString,
                response_deserializer=foodfinder_dot_vendor_dot_vendor__pb2.QueryInventoryResponse.FromString,
                )


class VendorServicer(object):
    """*
    Gives inventory and price of item from the given vendor
    """

    def queryInventory(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_VendorServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'queryInventory': grpc.unary_unary_rpc_method_handler(
                    servicer.queryInventory,
                    request_deserializer=foodfinder_dot_vendor_dot_vendor__pb2.QueryInventoryRequest.FromString,
                    response_serializer=foodfinder_dot_vendor_dot_vendor__pb2.QueryInventoryResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'foodfinder.vendor.Vendor', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Vendor(object):
    """*
    Gives inventory and price of item from the given vendor
    """

    @staticmethod
    def queryInventory(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/foodfinder.vendor.Vendor/queryInventory',
            foodfinder_dot_vendor_dot_vendor__pb2.QueryInventoryRequest.SerializeToString,
            foodfinder_dot_vendor_dot_vendor__pb2.QueryInventoryResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)
