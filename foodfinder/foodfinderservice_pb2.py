# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: foodfinderservice.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import foodfinder_pb2 as foodfinder__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='foodfinderservice.proto',
  package='foodfinder.finder',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\x17\x66oodfinderservice.proto\x12\x11\x66oodfinder.finder\x1a\x10\x66oodfinder.proto\"+\n\x15\x46indIngredientRequest\x12\x12\n\ningredient\x18\x01 \x01(\t\"P\n\x16\x46indIngredientResponse\x12\x36\n\x11vendorInventories\x18\x01 \x03(\x0b\x32\x1b.foodfinder.VendorInventory2q\n\x06\x46inder\x12g\n\x0e\x66indIngredient\x12(.foodfinder.finder.FindIngredientRequest\x1a).foodfinder.finder.FindIngredientResponse\"\x00\x62\x06proto3'
  ,
  dependencies=[foodfinder__pb2.DESCRIPTOR,])




_FINDINGREDIENTREQUEST = _descriptor.Descriptor(
  name='FindIngredientRequest',
  full_name='foodfinder.finder.FindIngredientRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ingredient', full_name='foodfinder.finder.FindIngredientRequest.ingredient', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=64,
  serialized_end=107,
)


_FINDINGREDIENTRESPONSE = _descriptor.Descriptor(
  name='FindIngredientResponse',
  full_name='foodfinder.finder.FindIngredientResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='vendorInventories', full_name='foodfinder.finder.FindIngredientResponse.vendorInventories', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=109,
  serialized_end=189,
)

_FINDINGREDIENTRESPONSE.fields_by_name['vendorInventories'].message_type = foodfinder__pb2._VENDORINVENTORY
DESCRIPTOR.message_types_by_name['FindIngredientRequest'] = _FINDINGREDIENTREQUEST
DESCRIPTOR.message_types_by_name['FindIngredientResponse'] = _FINDINGREDIENTRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FindIngredientRequest = _reflection.GeneratedProtocolMessageType('FindIngredientRequest', (_message.Message,), {
  'DESCRIPTOR' : _FINDINGREDIENTREQUEST,
  '__module__' : 'foodfinderservice_pb2'
  # @@protoc_insertion_point(class_scope:foodfinder.finder.FindIngredientRequest)
  })
_sym_db.RegisterMessage(FindIngredientRequest)

FindIngredientResponse = _reflection.GeneratedProtocolMessageType('FindIngredientResponse', (_message.Message,), {
  'DESCRIPTOR' : _FINDINGREDIENTRESPONSE,
  '__module__' : 'foodfinderservice_pb2'
  # @@protoc_insertion_point(class_scope:foodfinder.finder.FindIngredientResponse)
  })
_sym_db.RegisterMessage(FindIngredientResponse)



_FINDER = _descriptor.ServiceDescriptor(
  name='Finder',
  full_name='foodfinder.finder.Finder',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=191,
  serialized_end=304,
  methods=[
  _descriptor.MethodDescriptor(
    name='findIngredient',
    full_name='foodfinder.finder.Finder.findIngredient',
    index=0,
    containing_service=None,
    input_type=_FINDINGREDIENTREQUEST,
    output_type=_FINDINGREDIENTRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_FINDER)

DESCRIPTOR.services_by_name['Finder'] = _FINDER

# @@protoc_insertion_point(module_scope)
