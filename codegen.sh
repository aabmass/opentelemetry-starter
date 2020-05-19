#!/bin/bash
source venv/bin/activate
python -m grpc_tools.protoc \
    -Iprotos \
    --python_out=. \
    --mypy_out=. \
    --grpc_python_out=. \
    `find protos/ -iname "*.proto"`
