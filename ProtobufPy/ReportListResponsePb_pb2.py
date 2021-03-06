# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ReportListResponsePb.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import ProtobufPy.ViOrderReportResponsePb_pb2 as ViOrderReportResponsePb__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='ReportListResponsePb.proto',
  package='',
  syntax='proto3',
  serialized_options=_b('\252\002\025TomTaw.eWordRIS.Proto'),
  serialized_pb=_b('\n\x1aReportListResponsePb.proto\x1a\x1dViOrderReportResponsePb.proto\"\xad\x01\n\x14ReportListResponsePb\x12-\n\x0borderReport\x18\x01 \x03(\x0b\x32\x18.ViOrderReportResponsePb\x12\x37\n\x11reportStateNumber\x18\x02 \x01(\x0b\x32\x1c.ReportStateNumberResponsePb\x12-\n\x0creportStatic\x18\x03 \x01(\x0b\x32\x17.ReportStaticResponsePb\"\xbd\x01\n\x16ReportStaticResponsePb\x12\x12\n\norderCount\x18\x01 \x01(\t\x12\x15\n\rnotCheckCount\x18\x02 \x01(\t\x12\x1a\n\x12\x66inishCheckedCount\x18\x03 \x01(\t\x12\x17\n\x0funReportedCount\x18\x04 \x01(\t\x12\x14\n\x0cwrittenCount\x18\x05 \x01(\t\x12\x16\n\x0e\x63onfirmedCount\x18\x06 \x01(\t\x12\x15\n\rpositionCount\x18\x07 \x01(\t\"\xa1\x01\n\x1bReportStateNumberResponsePb\x12\x1c\n\x14waitOrderReportCount\x18\x01 \x01(\t\x12\x1f\n\x17onGoingOrderReportCount\x18\x02 \x01(\t\x12\x1e\n\x16\x66inishOrderReportCount\x18\x03 \x01(\t\x12#\n\x1bwriteFinishOrderReportCount\x18\x04 \x01(\tB\x18\xaa\x02\x15TomTaw.eWordRIS.Protob\x06proto3')
  ,
  dependencies=[ViOrderReportResponsePb__pb2.DESCRIPTOR,])




_REPORTLISTRESPONSEPB = _descriptor.Descriptor(
  name='ReportListResponsePb',
  full_name='ReportListResponsePb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='orderReport', full_name='ReportListResponsePb.orderReport', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='reportStateNumber', full_name='ReportListResponsePb.reportStateNumber', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='reportStatic', full_name='ReportListResponsePb.reportStatic', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=62,
  serialized_end=235,
)


_REPORTSTATICRESPONSEPB = _descriptor.Descriptor(
  name='ReportStaticResponsePb',
  full_name='ReportStaticResponsePb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='orderCount', full_name='ReportStaticResponsePb.orderCount', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='notCheckCount', full_name='ReportStaticResponsePb.notCheckCount', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='finishCheckedCount', full_name='ReportStaticResponsePb.finishCheckedCount', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='unReportedCount', full_name='ReportStaticResponsePb.unReportedCount', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='writtenCount', full_name='ReportStaticResponsePb.writtenCount', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='confirmedCount', full_name='ReportStaticResponsePb.confirmedCount', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='positionCount', full_name='ReportStaticResponsePb.positionCount', index=6,
      number=7, type=9, cpp_type=9, label=1,
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
  serialized_start=238,
  serialized_end=427,
)


_REPORTSTATENUMBERRESPONSEPB = _descriptor.Descriptor(
  name='ReportStateNumberResponsePb',
  full_name='ReportStateNumberResponsePb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='waitOrderReportCount', full_name='ReportStateNumberResponsePb.waitOrderReportCount', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='onGoingOrderReportCount', full_name='ReportStateNumberResponsePb.onGoingOrderReportCount', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='finishOrderReportCount', full_name='ReportStateNumberResponsePb.finishOrderReportCount', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='writeFinishOrderReportCount', full_name='ReportStateNumberResponsePb.writeFinishOrderReportCount', index=3,
      number=4, type=9, cpp_type=9, label=1,
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
  serialized_start=430,
  serialized_end=591,
)

_REPORTLISTRESPONSEPB.fields_by_name['orderReport'].message_type = ViOrderReportResponsePb__pb2._VIORDERREPORTRESPONSEPB
_REPORTLISTRESPONSEPB.fields_by_name['reportStateNumber'].message_type = _REPORTSTATENUMBERRESPONSEPB
_REPORTLISTRESPONSEPB.fields_by_name['reportStatic'].message_type = _REPORTSTATICRESPONSEPB
DESCRIPTOR.message_types_by_name['ReportListResponsePb'] = _REPORTLISTRESPONSEPB
DESCRIPTOR.message_types_by_name['ReportStaticResponsePb'] = _REPORTSTATICRESPONSEPB
DESCRIPTOR.message_types_by_name['ReportStateNumberResponsePb'] = _REPORTSTATENUMBERRESPONSEPB
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ReportListResponsePb = _reflection.GeneratedProtocolMessageType('ReportListResponsePb', (_message.Message,), {
  'DESCRIPTOR' : _REPORTLISTRESPONSEPB,
  '__module__' : 'ReportListResponsePb_pb2'
  # @@protoc_insertion_point(class_scope:ReportListResponsePb)
  })
_sym_db.RegisterMessage(ReportListResponsePb)

ReportStaticResponsePb = _reflection.GeneratedProtocolMessageType('ReportStaticResponsePb', (_message.Message,), {
  'DESCRIPTOR' : _REPORTSTATICRESPONSEPB,
  '__module__' : 'ReportListResponsePb_pb2'
  # @@protoc_insertion_point(class_scope:ReportStaticResponsePb)
  })
_sym_db.RegisterMessage(ReportStaticResponsePb)

ReportStateNumberResponsePb = _reflection.GeneratedProtocolMessageType('ReportStateNumberResponsePb', (_message.Message,), {
  'DESCRIPTOR' : _REPORTSTATENUMBERRESPONSEPB,
  '__module__' : 'ReportListResponsePb_pb2'
  # @@protoc_insertion_point(class_scope:ReportStateNumberResponsePb)
  })
_sym_db.RegisterMessage(ReportStateNumberResponsePb)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
