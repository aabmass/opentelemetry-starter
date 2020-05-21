#!/bin/bash

# clean up old files
find foodfinder/ -regex ".*_pb2.*\.pyi?" -exec rm {} +

source venv/bin/activate
python -m grpc_tools.protoc \
    -Iprotos \
    --python_out=. \
    --mypy_out=. \
    --grpc_python_out=. \
    `find protos/ -iname "*.proto"`
