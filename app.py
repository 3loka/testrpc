import logging
import sys
from concurrent import futures

import grpc
from grpc_reflection.v1alpha import reflection

import messages.service_pb2 as GRPCService_messages
import messages.service_pb2_grpc as GRPCService_service
from config import Config
from interceptors.request_header import RequestHeaderInterceptor
from services.service import GRPCService

# Logging Settings
logging.basicConfig(stream=sys.stdout,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    level=Config.LOGLEVEL,
                    datefmt='%Y-%m-%d %H:%M:%S')
logger = logging.getLogger()


def grpc_server():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10),
                         interceptors=(RequestHeaderInterceptor(),))

    # Register service
    GRPCService_service.add_GRPCServiceServicer_to_server(
        GRPCService(), server)

    # Enable Reflection
    SERVICE_NAMES = (
       GRPCService_messages.DESCRIPTOR.services_by_name['GRPCService'].full_name,
        reflection.SERVICE_NAME
    )
    reflection.enable_server_reflection(SERVICE_NAMES, server)

    logging.info(
        f"Service Running on port: {Config.SERVICE_PORT}")
    # This is just for testing only ( Not recommended in production )
    server.add_insecure_port(f"[::]:{Config.SERVICE_PORT}")
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    grpc_server()
