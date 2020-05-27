from typing import Dict, List, Optional

from foodfinder import foodfinder_pb2

"""
Mocks accessing a database to get vendor information
"""

_MOCK_VENDOR_INVENTORIES = {
    88765432: {
        "flour": foodfinder_pb2.VendorInventory(
            vendorName="Baking Supply Co",
            vendorId=88765432,
            quantity=2,
            unitPrice=foodfinder_pb2.Money(currencyCode="USD", amount=1000),
        ),
        "yeast": foodfinder_pb2.VendorInventory(
            vendorName="Baking Supply Co",
            vendorId=88765432,
            quantity=10,
            unitPrice=foodfinder_pb2.Money(currencyCode="USD", amount=500),
        ),
    },
    654311: {
        "flour": foodfinder_pb2.VendorInventory(
            vendorName="Costmart",
            vendorId=654311,
            quantity=10,
            unitPrice=foodfinder_pb2.Money(currencyCode="USD", amount=999),
        ),
        "yeast": foodfinder_pb2.VendorInventory(
            vendorName="Costmart",
            vendorId=654311,
            quantity=20,
            unitPrice=foodfinder_pb2.Money(currencyCode="USD", amount=249),
        ),
        "butter": foodfinder_pb2.VendorInventory(
            vendorName="Costmart",
            vendorId=654311,
            quantity=5,
            unitPrice=foodfinder_pb2.Money(currencyCode="USD", amount=499),
        ),
    },
    4442315: {
        "flour": foodfinder_pb2.VendorInventory(
            vendorName="Costshop",
            vendorId=4442315,
            quantity=4,
            unitPrice=foodfinder_pb2.Money(currencyCode="USD", amount=1199),
        ),
    },
}


def all_vendor_ids() -> List[int]:
    return list(_MOCK_VENDOR_INVENTORIES.keys())


def get_vendor_inventory(vendor_id: int) -> Dict[str, foodfinder_pb2.VendorInventory]:
    return _MOCK_VENDOR_INVENTORIES[vendor_id]
