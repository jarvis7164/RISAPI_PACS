# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ParameterResponsePb.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='ParameterResponsePb.proto',
  package='',
  syntax='proto3',
  serialized_options=_b('\252\002\025TomTaw.eWordRIS.Proto'),
  serialized_pb=_b('\n\x19ParameterResponsePb.proto\"H\n\x13ParameterResponsePb\x12\x10\n\x08paramter\x18\x01 \x01(\t\x12\x0e\n\x06isTrue\x18\x02 \x01(\x08\x12\x0f\n\x07\x63ontent\x18\x03 \x01(\tB\x18\xaa\x02\x15TomTaw.eWordRIS.Protob\x06proto3')
)




_PARAMETERRESPONSEPB = _descriptor.Descriptor(
  name='ParameterResponsePb',
  full_name='ParameterResponsePb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='paramter', full_name='ParameterResponsePb.paramter', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='isTrue', full_name='ParameterResponsePb.isTrue', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='content', full_name='ParameterResponsePb.content', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=29,
  serialized_end=101,
)

DESCRIPTOR.message_types_by_name['ParameterResponsePb'] = _PARAMETERRESPONSEPB
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ParameterResponsePb = _reflection.GeneratedProtocolMessageType('ParameterResponsePb', (_message.Message,), dict(
  DESCRIPTOR = _PARAMETERRESPONSEPB,
  __module__ = 'ParameterResponsePb_pb2'
  # @@protoc_insertion_point(class_scope:ParameterResponsePb)
  ))
_sym_db.RegisterMessage(ParameterResponsePb)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
