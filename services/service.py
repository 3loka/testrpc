import logging
import random
import string
import sys

import grpc
from config import Config
from messages import service_pb2 as GRPCService_messages
from messages import service_pb2_grpc as GRPCService_service

# Logging Settings
logging.basicConfig(stream=sys.stdout,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    level=Config.LOGLEVEL,
                    datefmt='%Y-%m-%d %H:%M:%S')
logger = logging.getLogger()


class GRPCService(GRPCService_service.GRPCServiceServicer):

    def create(self, request, context):
        logger.info("Received request: %s", request)

        return GRPCService_messages.CreateReply(message=request.message)

    def update(self, request, context):
        logger.info("Received request: %s", request)

        return GRPCService_messages.UpdateReply(message=request.message)

    def delete(self, request, context):
        logger.info("Received request: %s", request)

        return GRPCService_messages.DeleteReply(message=request.message)

    def get(self, request, context):
        logger.info("Received request: %s", request)

        return GRPCService_messages.GetReply(message=request.message)

    def list(self, request, context):
        logger.info("Received request: %s", request)

        return GRPCService_messages.CreateReply(message=request.message)
