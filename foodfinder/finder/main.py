from concurrent.futures import ThreadPoolExecutor
import grpc
from typing import Optional
from grpc_reflection.v1alpha import reflection
from foodfinder.util import filter_nulls
from foodfinder.finder import finder_pb2_grpc, finder_pb2
from foodfinder import foodfinder_pb2
from foodfinder.supplier import supplier_pb2_grpc, supplier_pb2
from foodfinder.vendor import vendor_pb2_grpc, vendor_pb2

TIMEOUT = 5

class FinderServicer(finder_pb2_grpc.FinderServicer):
    def findIngredient(
        self, request: finder_pb2.FindIngredientRequest, context: grpc.RpcContext,
    ) -> finder_pb2.FindIngredientResponse:
        # Call to Supplier service
        with grpc.insecure_channel("localhost:50053") as channel:
            supplier_stub = supplier_pb2_grpc.SupplierStub(channel)

            print("calling supplier service")
            search_vendors_response: supplier_pb2.SearchVendorsResponse = supplier_stub.searchVendors(
                supplier_pb2.SearchVendorsRequest(ingredient=request.ingredient),
                timeout=TIMEOUT,
            )

        # Call to vendor service
        with grpc.insecure_channel("localhost:50055") as channel:
            vendor_stub = vendor_pb2_grpc.VendorStub(channel)

            # TODO: call for each vendor in parallel
            vendor_inventories = [
                self._query_vendor(vendor_stub, vendor_id, request.ingredient,)
                for vendor_id in search_vendors_response.vendorIds
            ]

        return finder_pb2.FindIngredientResponse(
            vendorInventories=filter_nulls(vendor_inventories)
        )

    @staticmethod
    def _query_vendor(
        vendor_stub: vendor_pb2_grpc.VendorStub, vendor_id: int, ingredient: str,
    ) -> Optional[foodfinder_pb2.VendorInventory]:
        print("calling vendor service")
        res: vendor_pb2.QueryInventoryResponse = vendor_stub.queryInventory(
            vendor_pb2.QueryInventoryRequest(vendorId=vendor_id, ingredient=ingredient),
            timeout=TIMEOUT,
        )

        if res.HasField("vendorInventory"):
            return res.vendorInventory
        else:
            return None


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
