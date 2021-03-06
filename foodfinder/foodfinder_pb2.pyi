# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
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

class Money(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    currencyCode: typing___Text = ...
    amount: builtin___int = ...

    def __init__(self,
        *,
        currencyCode : typing___Optional[typing___Text] = None,
        amount : typing___Optional[builtin___int] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> Money: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> Money: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"amount",b"amount",u"currencyCode",b"currencyCode"]) -> None: ...
type___Money = Money

class VendorInventory(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    vendorName: typing___Text = ...
    quantity: builtin___int = ...
    vendorId: builtin___int = ...

    @property
    def unitPrice(self) -> type___Money: ...

    def __init__(self,
        *,
        vendorName : typing___Optional[typing___Text] = None,
        quantity : typing___Optional[builtin___int] = None,
        unitPrice : typing___Optional[type___Money] = None,
        vendorId : typing___Optional[builtin___int] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> VendorInventory: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> VendorInventory: ...
    def HasField(self, field_name: typing_extensions___Literal[u"unitPrice",b"unitPrice"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"quantity",b"quantity",u"unitPrice",b"unitPrice",u"vendorId",b"vendorId",u"vendorName",b"vendorName"]) -> None: ...
type___VendorInventory = VendorInventory
