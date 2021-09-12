from concurrent import futures
import logging
import grpc
import property_pb2
import property_pb2_grpc
from services.mysqlbase import MySQLBase


class Property(property_pb2_grpc.PropertyServicer):
    def Properties(self, request, context):
        results = MySQLBase().execute_command("grpc_property_by_id",
                                              (request.property_id, ))

        return property_pb2.PropertyReply(
            address=results[0]["address"],
            city=results[0]["city"],
            price=results[0]["price"],
            description=results[0]["description"])


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    property_pb2_grpc.add_PropertyServicer_to_server(Property(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    print('Starting server. Listening on port 50051.')
    logging.basicConfig()
    serve()