# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: property.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='property.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0eproperty.proto\"&\n\x0fPropertyRequest\x12\x13\n\x0bproperty_id\x18\x01 \x01(\x05\"R\n\rPropertyReply\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\t\x12\x0c\n\x04\x63ity\x18\x02 \x01(\t\x12\r\n\x05price\x18\x03 \x01(\x02\x12\x13\n\x0b\x64\x65scription\x18\x04 \x01(\t2<\n\x08Property\x12\x30\n\nProperties\x12\x10.PropertyRequest\x1a\x0e.PropertyReply\"\x00\x62\x06proto3'
)




_PROPERTYREQUEST = _descriptor.Descriptor(
  name='PropertyRequest',
  full_name='PropertyRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='property_id', full_name='PropertyRequest.property_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=18,
  serialized_end=56,
)


_PROPERTYREPLY = _descriptor.Descriptor(
  name='PropertyReply',
  full_name='PropertyReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='address', full_name='PropertyReply.address', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='city', full_name='PropertyReply.city', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='price', full_name='PropertyReply.price', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='description', full_name='PropertyReply.description', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=58,
  serialized_end=140,
)

DESCRIPTOR.message_types_by_name['PropertyRequest'] = _PROPERTYREQUEST
DESCRIPTOR.message_types_by_name['PropertyReply'] = _PROPERTYREPLY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PropertyRequest = _reflection.GeneratedProtocolMessageType('PropertyRequest', (_message.Message,), {
  'DESCRIPTOR' : _PROPERTYREQUEST,
  '__module__' : 'property_pb2'
  # @@protoc_insertion_point(class_scope:PropertyRequest)
  })
_sym_db.RegisterMessage(PropertyRequest)

PropertyReply = _reflection.GeneratedProtocolMessageType('PropertyReply', (_message.Message,), {
  'DESCRIPTOR' : _PROPERTYREPLY,
  '__module__' : 'property_pb2'
  # @@protoc_insertion_point(class_scope:PropertyReply)
  })
_sym_db.RegisterMessage(PropertyReply)



_PROPERTY = _descriptor.ServiceDescriptor(
  name='Property',
  full_name='Property',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=142,
  serialized_end=202,
  methods=[
  _descriptor.MethodDescriptor(
    name='Properties',
    full_name='Property.Properties',
    index=0,
    containing_service=None,
    input_type=_PROPERTYREQUEST,
    output_type=_PROPERTYREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_PROPERTY)

DESCRIPTOR.services_by_name['Property'] = _PROPERTY

# @@protoc_insertion_point(module_scope)
