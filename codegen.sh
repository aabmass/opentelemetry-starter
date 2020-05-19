#!/bin/bash
source venv/bin/activate
python -m grpc_tools.protoc \
    -Iprotos \
    --python_out=foodfinder \
    --grpc_python_out=foodfinder \
    protos/*.proto
