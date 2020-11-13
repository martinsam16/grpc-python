import grpc

import HelloWorld_pb2
import HelloWorld_pb2_grpc


def corre_cliente():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = HelloWorld_pb2_grpc.SaludarServiceStub(channel)
        response = stub.SaludarRpc(HelloWorld_pb2.HelloRequest(mensajeRequest='Esto mandé'))
    print("[Cliente] Respuesta:" + response.mensajeRespuesta)


if __name__ == '__main__':
    corre_cliente()
