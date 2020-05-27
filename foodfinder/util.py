from typing import List, Optional, TypeVar, Literal, Dict
from concurrent.futures import ThreadPoolExecutor
from argparse import ArgumentParser
import grpc
from opencensus.ext.grpc import server_interceptor
from opencensus.ext.stackdriver import trace_exporter as stackdriver_exporter
from opencensus.trace import samplers

ServiceName = Literal["finder", "supplier", "vendor"]

_T = TypeVar("_T")

_PROD_PORT = 50051
_TEST_PORTS: Dict[ServiceName, int] = {
    "finder": 50051,
    "supplier": 50053,
    "vendor": 50055,
}


def filter_nulls(ts: List[Optional[_T]]) -> List[_T]:
    return [t for t in ts if t is not None]


def address_for_server(service: ServiceName, is_prod: bool) -> str:
    # All services on same prod port
    port = _PROD_PORT if is_prod else _TEST_PORTS[service]
    return f"[::]:{port}"


def address_for_client(service: ServiceName, is_prod: bool) -> str:
    if is_prod:
        return f"{service}:{_PROD_PORT}"
    else:
        return f"[::]:{_TEST_PORTS[service]}"


def get_base_parser() -> ArgumentParser:
    parser = ArgumentParser()
    parser.add_argument("--is_prod", action="store_true")
    return parser


def create_grpc_server(is_prod: bool) -> grpc.Server:
    interceptors = []
    if is_prod:
        sampler = samplers.AlwaysOnSampler()
        exporter = stackdriver_exporter.StackdriverExporter()
        tracer_interceptor = server_interceptor.OpenCensusServerInterceptor(
            sampler, exporter
        )
        interceptors.append(tracer_interceptor)

    return grpc.server(
        ThreadPoolExecutor(max_workers=10), interceptors=interceptors,
    )
