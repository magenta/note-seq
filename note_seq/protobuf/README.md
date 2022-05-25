# Protobuf

This page describe how to update the protobuf generated python file. By
default, the protobuf is already compiled into python file so you won't have to
do anything. Those steps are required only if you update the `.proto` file.

Install the proto compiler (version 3.6.1):

```bash
./install_protoc.sh <linux|osx>
```

Install dev dependencies for stub files generation

- protobuf==3.6.1
- grpc-stubs>=1.24.9
- mypy-protobuf==3.2.0
- types-protobuf>=3.19.12
- grpcio>=1.44.0
- grpcio-tools>=1.44.0
- grpc-stubs>=1.24.9
- mypy
- pytest

Re-generate the python file:

```bash
./generate_pb2_py.sh
```
