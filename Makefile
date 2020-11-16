APP_NAME := learning-python-grpc

run-server:
	python server.py3

run-client:
	python client.py

docker-build:
	docker build . -t $(APP_NAME)

docker-run:
	docker run -d -p 50051:50051 --name $(APP_NAME) $(APP_NAME)

docker-stop:
	docker rm -f $(APP_NAME)

grpc-build:
	python -m grpc_tools.protoc -I./protos --python_out=./generado --grpc_python_out=./generado ./protos/*.proto