#!/bin/bash
grpc_cli_local call localhost:50051 findIngredient "ingredient: '$1'"
