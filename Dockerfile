FROM grpc/python:1.13

MAINTAINER Martin Alexis Saman Arata

COPY generado generado
COPY server.py server.py
COPY requirements.txt requirements.txt

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 50051

CMD ["python","./server.py"]