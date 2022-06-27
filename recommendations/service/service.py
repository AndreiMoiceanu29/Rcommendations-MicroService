import grpc
from pb_grpc.recommendations_pb2 import BookRecommendation
from pb_grpc.recommendations_pb2 import CreateRecommendationRequest
from pb_grpc.recommendations_pb2 import UpdateRecommendationRequest
from pb_grpc.recommendations_pb2 import DeleteRecommendationRequest
from pb_grpc.recommendations_pb2 import RecommendationRequest
from pb_grpc.recommendations_pb2 import CreateRecommendationResponse
from pb_grpc.recommendations_pb2 import UpdateRecommendationResponse
from pb_grpc.recommendations_pb2 import DeleteRecommendationResponse
from pb_grpc.recommendations_pb2 import RecommendationResponse
from pb_grpc import recommendations_pb2_grpc
from validator import RecommendationValidator
from service_exceptions import InvalidRecommendation
from mge_logging import mge_log
from repository import RepositoryFile
class Service(recommendations_pb2_grpc.RecommendationsServicer):
    def __init__(self, repository: RepositoryFile):
        super().__init__()
        self.repository = repository
    
    def Create(self, request: CreateRecommendationRequest, context: grpc.RpcContext) -> CreateRecommendationResponse:
        recommendation = request.recommendation
        mge_log.info("Client requested to create a recommendation")
        try :
            RecommendationValidator.validate_recommendation(recommendation)
        except InvalidRecommendation as e:
            mge_log.warning(e.message)
            context.abort(grpc.StatusCode.INVALID_ARGUMENT, str(e))
        self.repository.store_recommendation(recommendation)
        mge_log.info("Recommendation created")
        return CreateRecommendationResponse(recommendation=recommendation)

    def Update(self, request: UpdateRecommendationRequest, context: grpc.RpcContext) -> UpdateRecommendationResponse:
        old_recommendation = request.old_recommendation
        new_recommendation = request.new_recommendation
        mge_log.info("Client requested to update a recommendation")
        try :
            RecommendationValidator.validate_recommendation(new_recommendation)
        except InvalidRecommendation as e:
            mge_log.warning(e.message)
            context.abort(grpc.StatusCode.INVALID_ARGUMENT, str(e))
        try:
            RecommendationValidator.validate_recommendation(old_recommendation)
        except InvalidRecommendation as e:
            mge_log.warning(e.message)
            context(grpc.StatusCode.INVALID_ARGUMENT, str(e))
        self.repository.update_recommendation(old_recommendation, new_recommendation)
        mge_log.info("Recommendation updated")
        return UpdateRecommendationResponse(old_recommendation=old_recommendation,status=str(grpc.StatusCode.OK))

    def Delete(self, request: DeleteRecommendationRequest, context: grpc.RpcContext) -> DeleteRecommendationResponse:
        recommendation = request.recommendation
        mge_log.info("Client requested to delete a recommendation")
        try:
            RecommendationValidator.validate_recommendation(recommendation)
        except InvalidRecommendation as e:
            mge_log.warning(e.message)
            context(grpc.StatusCode.INVALID_ARGUMENT, str(e))
        self.repository.delete_recommendation(recommendation)
        mge_log.info("Recommendation deleted")
        return DeleteRecommendationResponse(recommendation=recommendation)
    def Recommend(self, request: RecommendationRequest, context: grpc.RpcContext) -> RecommendationResponse:
        recommendations = self.repository.get_recommendations(request.recommendation)
        mge_log.info("Client requested recommendations")
        return RecommendationResponse(recommendations=recommendations)