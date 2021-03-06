# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ReportTemplateResponsePb.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import ProtobufPy.ReportTemplateDetailResponsePb_pb2 as ReportTemplateDetailResponsePb__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='ReportTemplateResponsePb.proto',
  package='',
  syntax='proto3',
  serialized_options=_b('\252\002\025TomTaw.eWordRIS.Proto'),
  serialized_pb=_b('\n\x1eReportTemplateResponsePb.proto\x1a$ReportTemplateDetailResponsePb.proto\"3\n\x18ReportTemplateResponsePb\x12\x17\n\x0ftemplateClassID\x18\x01 \x03(\t\"s\n%ReportTemplateServiceSectIDResponsePb\x12\x33\n\x08\x62odyPart\x18\x01 \x03(\x0b\x32!.ReportTemplateBodyPartResponsePb\x12\x15\n\rserviceSectID\x18\x02 \x01(\t\"k\n ReportTemplateBodyPartResponsePb\x12\x35\n\tprocedure\x18\x01 \x03(\x0b\x32\".ReportTemplateProcedureResponsePb\x12\x10\n\x08\x62odyPart\x18\x02 \x01(\t\"i\n!ReportTemplateProcedureResponsePb\x12\x31\n\x08template\x18\x01 \x03(\x0b\x32\x1f.ReportTemplateDetailResponsePb\x12\x11\n\tprocedure\x18\x02 \x01(\tB\x18\xaa\x02\x15TomTaw.eWordRIS.Protob\x06proto3')
  ,
  dependencies=[ReportTemplateDetailResponsePb__pb2.DESCRIPTOR,])




_REPORTTEMPLATERESPONSEPB = _descriptor.Descriptor(
  name='ReportTemplateResponsePb',
  full_name='ReportTemplateResponsePb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='templateClassID', full_name='ReportTemplateResponsePb.templateClassID', index=0,
      number=1, type=9, cpp_type=9, label=3,
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
  serialized_start=72,
  serialized_end=123,
)


_REPORTTEMPLATESERVICESECTIDRESPONSEPB = _descriptor.Descriptor(
  name='ReportTemplateServiceSectIDResponsePb',
  full_name='ReportTemplateServiceSectIDResponsePb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='bodyPart', full_name='ReportTemplateServiceSectIDResponsePb.bodyPart', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='serviceSectID', full_name='ReportTemplateServiceSectIDResponsePb.serviceSectID', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=125,
  serialized_end=240,
)


_REPORTTEMPLATEBODYPARTRESPONSEPB = _descriptor.Descriptor(
  name='ReportTemplateBodyPartResponsePb',
  full_name='ReportTemplateBodyPartResponsePb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='procedure', full_name='ReportTemplateBodyPartResponsePb.procedure', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bodyPart', full_name='ReportTemplateBodyPartResponsePb.bodyPart', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=242,
  serialized_end=349,
)


_REPORTTEMPLATEPROCEDURERESPONSEPB = _descriptor.Descriptor(
  name='ReportTemplateProcedureResponsePb',
  full_name='ReportTemplateProcedureResponsePb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='template', full_name='ReportTemplateProcedureResponsePb.template', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='procedure', full_name='ReportTemplateProcedureResponsePb.procedure', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=351,
  serialized_end=456,
)

_REPORTTEMPLATESERVICESECTIDRESPONSEPB.fields_by_name['bodyPart'].message_type = _REPORTTEMPLATEBODYPARTRESPONSEPB
_REPORTTEMPLATEBODYPARTRESPONSEPB.fields_by_name['procedure'].message_type = _REPORTTEMPLATEPROCEDURERESPONSEPB
_REPORTTEMPLATEPROCEDURERESPONSEPB.fields_by_name['template'].message_type = ReportTemplateDetailResponsePb__pb2._REPORTTEMPLATEDETAILRESPONSEPB
DESCRIPTOR.message_types_by_name['ReportTemplateResponsePb'] = _REPORTTEMPLATERESPONSEPB
DESCRIPTOR.message_types_by_name['ReportTemplateServiceSectIDResponsePb'] = _REPORTTEMPLATESERVICESECTIDRESPONSEPB
DESCRIPTOR.message_types_by_name['ReportTemplateBodyPartResponsePb'] = _REPORTTEMPLATEBODYPARTRESPONSEPB
DESCRIPTOR.message_types_by_name['ReportTemplateProcedureResponsePb'] = _REPORTTEMPLATEPROCEDURERESPONSEPB
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ReportTemplateResponsePb = _reflection.GeneratedProtocolMessageType('ReportTemplateResponsePb', (_message.Message,), dict(
  DESCRIPTOR = _REPORTTEMPLATERESPONSEPB,
  __module__ = 'ReportTemplateResponsePb_pb2'
  # @@protoc_insertion_point(class_scope:ReportTemplateResponsePb)
  ))
_sym_db.RegisterMessage(ReportTemplateResponsePb)

ReportTemplateServiceSectIDResponsePb = _reflection.GeneratedProtocolMessageType('ReportTemplateServiceSectIDResponsePb', (_message.Message,), dict(
  DESCRIPTOR = _REPORTTEMPLATESERVICESECTIDRESPONSEPB,
  __module__ = 'ReportTemplateResponsePb_pb2'
  # @@protoc_insertion_point(class_scope:ReportTemplateServiceSectIDResponsePb)
  ))
_sym_db.RegisterMessage(ReportTemplateServiceSectIDResponsePb)

ReportTemplateBodyPartResponsePb = _reflection.GeneratedProtocolMessageType('ReportTemplateBodyPartResponsePb', (_message.Message,), dict(
  DESCRIPTOR = _REPORTTEMPLATEBODYPARTRESPONSEPB,
  __module__ = 'ReportTemplateResponsePb_pb2'
  # @@protoc_insertion_point(class_scope:ReportTemplateBodyPartResponsePb)
  ))
_sym_db.RegisterMessage(ReportTemplateBodyPartResponsePb)

ReportTemplateProcedureResponsePb = _reflection.GeneratedProtocolMessageType('ReportTemplateProcedureResponsePb', (_message.Message,), dict(
  DESCRIPTOR = _REPORTTEMPLATEPROCEDURERESPONSEPB,
  __module__ = 'ReportTemplateResponsePb_pb2'
  # @@protoc_insertion_point(class_scope:ReportTemplateProcedureResponsePb)
  ))
_sym_db.RegisterMessage(ReportTemplateProcedureResponsePb)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
