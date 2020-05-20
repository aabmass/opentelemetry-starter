# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: foodfinder/foodfinder.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='foodfinder/foodfinder.proto',
  package='foodfinder',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\x1b\x66oodfinder/foodfinder.proto\x12\nfoodfinder\"-\n\x05Money\x12\x14\n\x0c\x63urrencyCode\x18\x01 \x01(\t\x12\x0e\n\x06\x61mount\x18\x02 \x01(\x03\"o\n\x0fVendorInventory\x12\x12\n\nvendorName\x18\x01 \x01(\t\x12\x10\n\x08quantity\x18\x02 \x01(\x03\x12$\n\tunitPrice\x18\x03 \x01(\x0b\x32\x11.foodfinder.Money\x12\x10\n\x08vendorId\x18\x04 \x01(\x03\x62\x06proto3'
)




_MONEY = _descriptor.Descriptor(
  name='Money',
  full_name='foodfinder.Money',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='currencyCode', full_name='foodfinder.Money.currencyCode', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='amount', full_name='foodfinder.Money.amount', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=43,
  serialized_end=88,
)


_VENDORINVENTORY = _descriptor.Descriptor(
  name='VendorInventory',
  full_name='foodfinder.VendorInventory',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='vendorName', full_name='foodfinder.VendorInventory.vendorName', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='quantity', full_name='foodfinder.VendorInventory.quantity', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='unitPrice', full_name='foodfinder.VendorInventory.unitPrice', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='vendorId', full_name='foodfinder.VendorInventory.vendorId', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=90,
  serialized_end=201,
)

_VENDORINVENTORY.fields_by_name['unitPrice'].message_type = _MONEY
DESCRIPTOR.message_types_by_name['Money'] = _MONEY
DESCRIPTOR.message_types_by_name['VendorInventory'] = _VENDORINVENTORY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Money = _reflection.GeneratedProtocolMessageType('Money', (_message.Message,), {
  'DESCRIPTOR' : _MONEY,
  '__module__' : 'foodfinder.foodfinder_pb2'
  # @@protoc_insertion_point(class_scope:foodfinder.Money)
  })
_sym_db.RegisterMessage(Money)

VendorInventory = _reflection.GeneratedProtocolMessageType('VendorInventory', (_message.Message,), {
  'DESCRIPTOR' : _VENDORINVENTORY,
  '__module__' : 'foodfinder.foodfinder_pb2'
  # @@protoc_insertion_point(class_scope:foodfinder.VendorInventory)
  })
_sym_db.RegisterMessage(VendorInventory)


# @@protoc_insertion_point(module_scope)
