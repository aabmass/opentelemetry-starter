#!/bin/bash
grpc_cli_local call localhost:50055 queryInventory "ingredient: 'test', vendorId: 88765432"
