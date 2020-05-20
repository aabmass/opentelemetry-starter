from typing import List, Optional
from foodfinder import foodfinder_pb2

"""
Mocks accessing a database to get vendor information
"""

_MOCK_VENDOR_INVENTORIES = {
    88765432: foodfinder_pb2.VendorInventory(
        vendorName="Costco",
        vendorId=88765432,
        quantity=2,
        unitPrice=foodfinder_pb2.Money(currencyCode="USD", amount=1000),
    )
}


def all_vendor_ids() -> List[int]:
    return list(_MOCK_VENDOR_INVENTORIES.keys())


def get_vendor_inventory(vendor_id: int) -> Optional[foodfinder_pb2.VendorInventory]:
    return _MOCK_VENDOR_INVENTORIES.get(vendor_id)
