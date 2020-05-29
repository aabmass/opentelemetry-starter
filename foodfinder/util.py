from argparse import ArgumentParser
from concurrent.futures import ThreadPoolExecutor
from typing import Dict, List, Literal, Optional, TypeVar

import grpc
from opentelemetry import trace
from opentelemetry.ext.cloud_trace import CloudTraceSpanExporter
from opentelemetry.ext.grpc import server_interceptor
from opentelemetry.ext.grpc.grpcext import intercept_server
from opentelemetry.sdk.trace import MultiSpanProcessor, TracerProvider
from opentelemetry.sdk.trace.export import (BatchExportSpanProcessor,
                                            ConsoleSpanExporter,
                                            SimpleExportSpanProcessor)

trace.set_tracer_provider(TracerProvider())

# tracer = trace.get_tracer(__name__)

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
    console_span_processor = SimpleExportSpanProcessor(ConsoleSpanExporter())
    if is_prod:
        span_processor = MultiSpanProcessor()
        span_processor.add_span_processor(console_span_processor)
        span_processor.add_span_processor(
            BatchExportSpanProcessor(CloudTraceSpanExporter())
        )
    else:
        span_processor = console_span_processor

    # this should typecheck but the API interface doesn't have add_span_processor()
    trace.get_tracer_provider().add_span_processor(  # type: ignore
        span_processor
    )

    server = grpc.server(ThreadPoolExecutor(max_workers=10))
    server = intercept_server(server, server_interceptor())
    return server
