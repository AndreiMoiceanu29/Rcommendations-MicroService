from pb_grpc.recommendations_pb2 import BookRecommendation
from typing import List, Protocol
class IRepository(Protocol):
    """Repository Interface"""
    def get_recommendations(self,filter_recommendation: BookRecommendation) -> List[BookRecommendation]:
        """Get all recommendations"""
        raise NotImplementedError
    
    def store_recommendation(self,recommendation: BookRecommendation) -> None:
        """Store a recommendation"""
        raise NotImplementedError