from concurrent.futures import ThreadPoolExecutor

import grpc
from grpc_reflection.v1alpha import reflection

from foodfinder import foodfinder_pb2, inventory_db, util

from . import vendor_pb2, vendor_pb2_grpc


class VendorServicer(vendor_pb2_grpc.VendorServicer):
    def queryInventory(
        self, request: vendor_pb2.QueryInventoryRequest, context: grpc.RpcContext,
    ) -> vendor_pb2.QueryInventoryResponse:
        return vendor_pb2.QueryInventoryResponse(
            vendorInventory=inventory_db.get_vendor_inventory(request.vendorId).get(
                request.ingredient
            )
        )


def main() -> None:
    parser = util.get_base_parser()
    args = parser.parse_args()
    server = util.create_grpc_server(args.is_prod)

    vendor_pb2_grpc.add_VendorServicer_to_server(VendorServicer(), server)
    hostname = util.address_for_server("vendor", args.is_prod)
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
