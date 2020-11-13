```bash
pip install -r requirements.txt
```

1. Crear los .proto con las definiciones
2. Generar el código de las interfaces del cliente y el servidor  
```bash
python -m grpc_tools.protoc -I./protos --python_out=. --grpc_python_out=./ ./protos/HelloWorld.proto
```
3. 



https://grpc.io/docs/languages/python/basics/