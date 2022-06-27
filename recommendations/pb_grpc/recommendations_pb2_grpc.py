# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import recommendations_pb2 as recommendations__pb2


class RecommendationsStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Recommend = channel.unary_unary(
                '/Recommendations/Recommend',
                request_serializer=recommendations__pb2.RecommendationRequest.SerializeToString,
                response_deserializer=recommendations__pb2.RecommendationResponse.FromString,
                )
        self.Create = channel.unary_unary(
                '/Recommendations/Create',
                request_serializer=recommendations__pb2.CreateRecommendationRequest.SerializeToString,
                response_deserializer=recommendations__pb2.CreateRecommendationResponse.FromString,
                )
        self.Update = channel.unary_unary(
                '/Recommendations/Update',
                request_serializer=recommendations__pb2.UpdateRecommendationRequest.SerializeToString,
                response_deserializer=recommendations__pb2.UpdateRecommendationResponse.FromString,
                )
        self.Delete = channel.unary_unary(
                '/Recommendations/Delete',
                request_serializer=recommendations__pb2.DeleteRecommendationRequest.SerializeToString,
                response_deserializer=recommendations__pb2.DeleteRecommendationResponse.FromString,
                )


class RecommendationsServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Recommend(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Create(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Update(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Delete(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_RecommendationsServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Recommend': grpc.unary_unary_rpc_method_handler(
                    servicer.Recommend,
                    request_deserializer=recommendations__pb2.RecommendationRequest.FromString,
                    response_serializer=recommendations__pb2.RecommendationResponse.SerializeToString,
            ),
            'Create': grpc.unary_unary_rpc_method_handler(
                    servicer.Create,
                    request_deserializer=recommendations__pb2.CreateRecommendationRequest.FromString,
                    response_serializer=recommendations__pb2.CreateRecommendationResponse.SerializeToString,
            ),
            'Update': grpc.unary_unary_rpc_method_handler(
                    servicer.Update,
                    request_deserializer=recommendations__pb2.UpdateRecommendationRequest.FromString,
                    response_serializer=recommendations__pb2.UpdateRecommendationResponse.SerializeToString,
            ),
            'Delete': grpc.unary_unary_rpc_method_handler(
                    servicer.Delete,
                    request_deserializer=recommendations__pb2.DeleteRecommendationRequest.FromString,
                    response_serializer=recommendations__pb2.DeleteRecommendationResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Recommendations', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Recommendations(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Recommend(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Recommendations/Recommend',
            recommendations__pb2.RecommendationRequest.SerializeToString,
            recommendations__pb2.RecommendationResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Create(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Recommendations/Create',
            recommendations__pb2.CreateRecommendationRequest.SerializeToString,
            recommendations__pb2.CreateRecommendationResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Update(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Recommendations/Update',
            recommendations__pb2.UpdateRecommendationRequest.SerializeToString,
            recommendations__pb2.UpdateRecommendationResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Delete(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Recommendations/Delete',
            recommendations__pb2.DeleteRecommendationRequest.SerializeToString,
            recommendations__pb2.DeleteRecommendationResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
