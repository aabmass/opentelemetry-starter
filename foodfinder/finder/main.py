from concurrent.futures import ThreadPoolExecutor
import grpc
from grpc_reflection.v1alpha import reflection
from . import finder_pb2_grpc, finder_pb2
from foodfinder import foodfinder_pb2


MOCK_VENDOR_INVENTORIES = [
    foodfinder_pb2.VendorInventory(
        vendorName="Costco",
        quantity=2,
        unitPrice=foodfinder_pb2.Money(currencyCode="USD", amount=1000),
    )
]


class FinderServicer(finder_pb2_grpc.FinderServicer):
    def findIngredient(
        self, request: finder_pb2.FindIngredientRequest, context: grpc.RpcContext,
    ) -> finder_pb2.FindIngredientResponse:
        # mocked for now
        return finder_pb2.FindIngredientResponse(
            vendorInventories=MOCK_VENDOR_INVENTORIES
        )


def main() -> None:
    server = grpc.server(ThreadPoolExecutor(max_workers=10))

    finder_pb2_grpc.add_FinderServicer_to_server(FinderServicer(), server)
    hostname = "[::]:50051"
    server.add_insecure_port(hostname)

    # reflection for grpc_cli
    SERVICE_NAMES = (
        finder_pb2.DESCRIPTOR.services_by_name["Finder"].full_name,  # type: ignore
        reflection.SERVICE_NAME,
    )
    reflection.enable_server_reflection(SERVICE_NAMES, server)

    server.start()
    print(f"Listening on {hostname}")
    server.wait_for_termination()


if __name__ == "__main__":
    main()
