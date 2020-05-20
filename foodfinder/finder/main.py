from concurrent.futures import ThreadPoolExecutor
import grpc
from grpc_reflection.v1alpha import reflection
from foodfinder.finder import finder_pb2_grpc, finder_pb2
from foodfinder import foodfinder_pb2
from foodfinder.supplier import supplier_pb2_grpc, supplier_pb2


MOCK_VENDOR_INVENTORIES = [
    foodfinder_pb2.VendorInventory(
        vendorName="Costco",
        vendorId=88765432,
        quantity=2,
        unitPrice=foodfinder_pb2.Money(currencyCode="USD", amount=1000),
    )
]


class FinderServicer(finder_pb2_grpc.FinderServicer):
    def findIngredient(
        self, request: finder_pb2.FindIngredientRequest, context: grpc.RpcContext,
    ) -> finder_pb2.FindIngredientResponse:
        with grpc.insecure_channel("localhost:50053") as channel:
            stub = supplier_pb2_grpc.SupplierStub(channel)

            print("calling supplier service")
            search_vendors_response: supplier_pb2.SearchVendorsResponse = stub.searchVendors(
                supplier_pb2.SearchVendorsRequest(ingredient=request.ingredient),
                timeout=5,
            )

        # mocked for now
        vendor_inventories = [
            foodfinder_pb2.VendorInventory(
                vendorName=f"Vendor {vendor_id}",
                vendorId=vendor_id,
                # these parts mocked, need to call vendor service
                quantity=2,
                unitPrice=foodfinder_pb2.Money(currencyCode="USD", amount=1000),
            )
            for vendor_id in search_vendors_response.vendorIds
        ]

        return finder_pb2.FindIngredientResponse(vendorInventories=vendor_inventories)


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
