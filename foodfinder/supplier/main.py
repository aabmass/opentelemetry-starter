from concurrent.futures import ThreadPoolExecutor
import grpc
from grpc_reflection.v1alpha import reflection
from . import supplier_pb2, supplier_pb2_grpc

MOCK_VENDOR_IDS = [
    88765432,
    5432,
    82823,
    1011011012,
]


class SupplierServicer(supplier_pb2_grpc.SupplierServicer):
    def searchVendors(
        self, request: supplier_pb2.SearchVendorsRequest, context: grpc.RpcContext,
    ) -> supplier_pb2.SearchVendorsResponse:
        # mocked for now
        return supplier_pb2.SearchVendorsResponse(vendorIds=MOCK_VENDOR_IDS)


def main() -> None:
    server = grpc.server(ThreadPoolExecutor(max_workers=10))

    supplier_pb2_grpc.add_SupplierServicer_to_server(SupplierServicer(), server)
    hostname = "[::]:50053"
    server.add_insecure_port(hostname)

    # reflection for grpc_cli
    SERVICE_NAMES = (
        supplier_pb2.DESCRIPTOR.services_by_name["Supplier"].full_name,  # type: ignore
        reflection.SERVICE_NAME,
    )
    reflection.enable_server_reflection(SERVICE_NAMES, server)

    server.start()
    print(f"Listening on {hostname}")
    server.wait_for_termination()


if __name__ == "__main__":
    main()
