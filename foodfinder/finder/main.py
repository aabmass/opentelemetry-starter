from concurrent.futures import ThreadPoolExecutor
from typing import Optional

import grpc
from grpc_reflection.v1alpha import reflection
from opencensus.ext.grpc import client_interceptor
from opencensus.ext.stackdriver import trace_exporter as stackdriver_exporter
from opencensus.trace.tracer import Tracer

from foodfinder import foodfinder_pb2, util
from foodfinder.finder import finder_pb2, finder_pb2_grpc
from foodfinder.supplier import supplier_pb2, supplier_pb2_grpc
from foodfinder.util import filter_nulls
from foodfinder.vendor import vendor_pb2, vendor_pb2_grpc

TIMEOUT = 5


class FinderServicer(finder_pb2_grpc.FinderServicer):
    def __init__(self, is_prod: bool) -> None:
        super().__init__()
        self.is_prod = is_prod

        exporter = stackdriver_exporter.StackdriverExporter()
        tracer = Tracer(exporter=exporter)

        supplier_address = util.address_for_client("supplier", self.is_prod)
        self.supplier_tracer_interceptor = client_interceptor.OpenCensusClientInterceptor(
            tracer, host_port=supplier_address,
        )

        vendor_address = util.address_for_client("vendor", self.is_prod)
        self.vendor_tracer_interceptor = client_interceptor.OpenCensusClientInterceptor(
            tracer, host_port=vendor_address,
        )
    
    def _supplier_channel(self) -> grpc.Channel:
        channel = grpc.insecure_channel(
            util.address_for_client("supplier", self.is_prod)
        )
        return grpc.intercept_channel(channel, self.supplier_tracer_interceptor)

    def _vendor_channel(self) -> grpc.Channel:
        channel = grpc.insecure_channel(
            util.address_for_client("vendor", self.is_prod)
        )
        return grpc.intercept_channel(channel, self.vendor_tracer_interceptor)

    def findIngredient(
        self, request: finder_pb2.FindIngredientRequest, context: grpc.RpcContext,
    ) -> finder_pb2.FindIngredientResponse:
        # Call to Supplier service
        with self._supplier_channel() as channel:
            supplier_stub = supplier_pb2_grpc.SupplierStub(channel)

            print("calling supplier service")
            search_vendors_response: supplier_pb2.SearchVendorsResponse = supplier_stub.searchVendors(
                supplier_pb2.SearchVendorsRequest(ingredient=request.ingredient),
                timeout=TIMEOUT,
            )

        # Call to vendor service
        with self._vendor_channel() as channel:
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
    parser = util.get_base_parser()
    args = parser.parse_args()
    server = util.create_grpc_server(args.is_prod)

    finder_pb2_grpc.add_FinderServicer_to_server(FinderServicer(args.is_prod), server)
    hostname = util.address_for_server("finder", args.is_prod)
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
