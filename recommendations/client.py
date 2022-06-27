import grpc
from pb_grpc.recommendations_pb2_grpc import RecommendationsStub
from pb_grpc.recommendations_pb2 import RecommendationRequest,BookCategory,CreateRecommendationRequest,CreateRecommendationResponse,BookRecommendation,UpdateRecommendationRequest,UpdateRecommendationResponse,DeleteRecommendationRequest,DeleteRecommendationResponse


def run_create_test():
    print("Running create test")
    channel = grpc.insecure_channel('localhost:50051')
    client = RecommendationsStub(channel)
    # create some recommendations
    recom = BookRecommendation()
    recom.title = "Star Wars"
    recom.id = 1
    recommendationReq = CreateRecommendationRequest(
        recommendation=recom)
    recommendation = client.Create(recommendationReq)

    from_sv = client.Recommend(RecommendationRequest(recommendation=recom)).recommendations[0]

    # Assert titles match
    assert from_sv.title == "Star Wars"
    print("Create test completed")

def run_update_test():
    print("Running update test")
    channel = grpc.insecure_channel('localhost:50051')
    client = RecommendationsStub(channel)
    # create some recommendations
    recom = BookRecommendation()
    recom.title = "Star Wars"
    recom.id = 1
    # Update the recommendation, set the title to "Hunger Games"
    new_recom = BookRecommendation()
    new_recom.id = recom.id
    new_recom.title = "Hunger Games"
    old = client.Update(UpdateRecommendationRequest(new_recommendation=new_recom,old_recommendation=recom))
    # Assert titles match
    assert old.old_recommendation.title == "Star Wars"
    new_rec = client.Recommend(RecommendationRequest(recommendation=recom)).recommendations[0]
    # Assert titles match
    assert new_rec.title == "Hunger Games"
    print("Update test completed")

def run_delete_test():
    print("Running delete test")
    channel = grpc.insecure_channel('localhost:50051')
    client = RecommendationsStub(channel)
    # create some recommendations
    recom = BookRecommendation()
    recom.title = "Star Wars"
    recom.id = 1
    new_recom = BookRecommendation()
    new_recom.title = "Marvel"
    new_recom.id = 2
    new_recommendationReq = CreateRecommendationRequest(recommendation=new_recom)
    new_recommendation = client.Create(new_recommendationReq)
    # Delete the recommendation with id 1
    client.Delete(DeleteRecommendationRequest(recommendation=recom))
    # Assert the recommendation with id 1 is gone
    try:
        client.Recommend(RecommendationRequest(recommendation=recom)).recommendations[0]
        assert False
    except IndexError:
        assert True
    # Assert the recommendation with id 2 is still there
    new_rec = client.Recommend(RecommendationRequest(recommendation=new_recom)).recommendations[0]
    assert new_rec.title == "Marvel"
    print("Delete test completed")
def run_tests():
    print("Running tests")
    run_create_test()
    run_update_test()
    run_delete_test()
    print("Tests completed")




# Create a new recommendation, Marvel with id 2
if __name__ == '__main__':
    run_tests()