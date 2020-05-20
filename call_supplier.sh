#!/bin/bash
grpc_cli_local call localhost:50053 searchVendors "ingredient: 'test'"
