from concurrent.futures import ThreadPoolExecutor
import grpc
from grpc_reflection.v1alpha import reflection
from . import vendor_pb2, vendor_pb2_grpc

MOCK_VENDOR_IDS = [
    88765432,
    5432,
    82823,
    1011011012,
]


class VendorServicer(vendor_pb2_grpc.VendorServicer):
    def queryInventory(
        self, request: vendor_pb2.QueryInventoryRequest, context: grpc.RpcContext,
    ) -> vendor_pb2.QueryInventoryResponse:
        print("Got request -", request)
        # mocked for now
        return vendor_pb2.QueryInventoryResponse(vendorInventory=None)


def main() -> None:
    server = grpc.server(ThreadPoolExecutor(max_workers=10))

    vendor_pb2_grpc.add_VendorServicer_to_server(VendorServicer(), server)
    hostname = "[::]:50055"
    server.add_insecure_port(hostname)

    # reflection for grpc_cli
    SERVICE_NAMES = (
        vendor_pb2.DESCRIPTOR.services_by_name["Vendor"].full_name,  # type: ignore
        reflection.SERVICE_NAME,
    )
    reflection.enable_server_reflection(SERVICE_NAMES, server)

    server.start()
    print(f"Listening on {hostname}")
    server.wait_for_termination()


if __name__ == "__main__":
    main()
