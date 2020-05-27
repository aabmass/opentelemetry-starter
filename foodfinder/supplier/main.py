from concurrent.futures import ThreadPoolExecutor

import grpc
from grpc_reflection.v1alpha import reflection

from foodfinder import inventory_db, util
from foodfinder.supplier import supplier_pb2, supplier_pb2_grpc


class SupplierServicer(supplier_pb2_grpc.SupplierServicer):
    def searchVendors(
        self, request: supplier_pb2.SearchVendorsRequest, context: grpc.RpcContext,
    ) -> supplier_pb2.SearchVendorsResponse:
        print("Got request -", request)
        # mocked for now
        return supplier_pb2.SearchVendorsResponse(
            vendorIds=inventory_db.all_vendor_ids()
        )


def main() -> None:
    parser = util.get_base_parser()
    args = parser.parse_args()
    server = util.create_grpc_server(args.is_prod)

    supplier_pb2_grpc.add_SupplierServicer_to_server(SupplierServicer(), server)
    hostname = util.address_for_server("supplier", args.is_prod)
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
