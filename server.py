import grpc

from generado import HelloWorld_pb2_grpc
from generado import HelloWorld_pb2

from concurrent import futures


class MyServer(HelloWorld_pb2_grpc.SaludarServiceServicer):
    def SaludarRpc(self, request, context):
        return HelloWorld_pb2.HelloReply(mensajeRespuesta='Hola causa soy un HelloReply.mensajeRespuesta')


def iniciar_server():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    HelloWorld_pb2_grpc.add_SaludarServiceServicer_to_server(servicer=MyServer(), server=server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    iniciar_server()
