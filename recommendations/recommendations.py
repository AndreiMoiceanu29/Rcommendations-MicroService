from concurrent import futures
from signal import signal, SIGTERM
import grpc
from pb_grpc import recommendations_pb2_grpc
from service import Service
from repository import RepositoryFile
from mge_logging import mge_log

def run_service(port: int) -> None:
    mge_log.info("Starting service")
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    file = "recommendations.txt"
    repository = RepositoryFile(file)
    service = Service(repository)
    recommendations_pb2_grpc.add_RecommendationsServicer_to_server(service, server)
    server.add_insecure_port(f"[::]:{port}")
    server.start()
    mge_log.info("Service started")
    def handle_sigterm(*_):
        """
        Handle stoping the service on a cloud device when updating the codebase.
        """
        mge_log.info("Stopping service")
        done_event = server.stop(30)
        done_event.wait(30)
        mge_log.info("Service stopped successfully")
    server.wait_for_termination()
    signal(SIGTERM, handle_sigterm)
    mge_log.critical("Service stopped")

if __name__=='__main__':
    run_service(port=50051)