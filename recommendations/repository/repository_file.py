from pb_grpc.recommendations_pb2 import BookRecommendation
from .repository_interface import IRepository
from typing import List
from mge_logging import mge_log
import os
class RepositoryFile(IRepository):
    def __init__(self,filename):
        super().__init__()
        self.filename = filename

    def get_recommendations(self,filter_recommendation: BookRecommendation) -> List[BookRecommendation]:
        mge_log.info("Getting recommendations from file")
        with open(self.filename) as f:
            lines = f.readlines()
        recommendations = []
        for line in lines:
            recommendation = BookRecommendation()
            id = line.split(" ")[0]
            # title is the rest of the line [1:]
            title = " ".join(line.split(" ")[1:])
            # Remove trailing newline
            title = title[:-1]
            recommendation.id = int(id)
            recommendation.title = title
            if filter_recommendation.id == recommendation.id:
                recommendations.append(recommendation)
        return recommendations
    
    def store_recommendation(self,recommendation: BookRecommendation) -> None:
        # First check if the recommendation already exists, if it does, then update it, if not, then add it by appending it to the file
        with open(self.filename) as f:
            lines = f.readlines()
            for line in lines:
                id = line.split(" ")[0]
                if id == str(recommendation.id):
                    self.update_recommendation(recommendation,recommendation)
                    return None
        with open(self.filename, 'a') as f:
            f.write(str(recommendation.id) + " " + recommendation.title + "\n")
            f.flush()
            os.fsync(f.fileno())
            f.close()
            return None
        return None

    
    def update_recommendation(self,old_recommendation: BookRecommendation,new_recommendation: BookRecommendation) -> None:
        # Delete the old recommendation, check it by comparing the id field, if they are the same, then delete it, then write the new one
        self.delete_recommendation(old_recommendation)
        self.store_recommendation(new_recommendation)
    
    def delete_recommendation(self,recommendation: BookRecommendation) -> None:
        """
        Read the file line by line, the recommendations are stored in the folowing format Id Name1 Name2 ... NameN
        Find the matching recomendation, delete it, then close the file
        """
        with open(self.filename) as f:
            lines = f.readlines()
        for line in lines:
            id = line.split(" ")[0]
            if id == str(recommendation.id):
                lines.remove(line)
                break
        with open(self.filename, 'w') as f:
            for line in lines:
                f.write(line)
            f.flush()
            os.fsync(f.fileno())
            f.close()
            return None
        return None
    