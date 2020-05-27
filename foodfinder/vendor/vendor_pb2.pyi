# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from foodfinder.foodfinder_pb2 import (
    VendorInventory as foodfinder___foodfinder_pb2___VendorInventory,
)

from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
    FileDescriptor as google___protobuf___descriptor___FileDescriptor,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from typing import (
    Optional as typing___Optional,
    Text as typing___Text,
    Union as typing___Union,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


builtin___bool = bool
builtin___bytes = bytes
builtin___float = float
builtin___int = int
if sys.version_info < (3,):
    builtin___buffer = buffer
    builtin___unicode = unicode


DESCRIPTOR: google___protobuf___descriptor___FileDescriptor = ...

class QueryInventoryRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    vendorId: builtin___int = ...
    ingredient: typing___Text = ...

    def __init__(self,
        *,
        vendorId : typing___Optional[builtin___int] = None,
        ingredient : typing___Optional[typing___Text] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> QueryInventoryRequest: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> QueryInventoryRequest: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"ingredient",b"ingredient",u"vendorId",b"vendorId"]) -> None: ...
type___QueryInventoryRequest = QueryInventoryRequest

class QueryInventoryResponse(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    @property
    def vendorInventory(self) -> foodfinder___foodfinder_pb2___VendorInventory: ...

    def __init__(self,
        *,
        vendorInventory : typing___Optional[foodfinder___foodfinder_pb2___VendorInventory] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> QueryInventoryResponse: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> QueryInventoryResponse: ...
    def HasField(self, field_name: typing_extensions___Literal[u"vendorInventory",b"vendorInventory"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"vendorInventory",b"vendorInventory"]) -> None: ...
type___QueryInventoryResponse = QueryInventoryResponse
