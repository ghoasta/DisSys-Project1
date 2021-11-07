# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: spelling_bee.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='spelling_bee.proto',
  package='app',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x12spelling_bee.proto\x12\x03\x61pp\"\x07\n\x05\x45mpty\"\x1e\n\x0bWorkPangram\x12\x0f\n\x07pangram\x18\x01 \x01(\t\"\x14\n\x04Word\x12\x0c\n\x04word\x18\x01 \x01(\t\":\n\x06Points\x12\x0f\n\x07messege\x18\x01 \x01(\t\x12\x0e\n\x06points\x18\x02 \x01(\x05\x12\x0f\n\x07pangram\x18\x03 \x01(\t2_\n\x0bSpellingBee\x12*\n\x08sayHello\x12\n.app.Empty\x1a\x10.app.WorkPangram\"\x00\x12$\n\x08sendWork\x12\t.app.Word\x1a\x0b.app.Points\"\x00\x62\x06proto3'
)




_EMPTY = _descriptor.Descriptor(
  name='Empty',
  full_name='app.Empty',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
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
  serialized_start=27,
  serialized_end=34,
)


_WORKPANGRAM = _descriptor.Descriptor(
  name='WorkPangram',
  full_name='app.WorkPangram',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='pangram', full_name='app.WorkPangram.pangram', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=36,
  serialized_end=66,
)


_WORD = _descriptor.Descriptor(
  name='Word',
  full_name='app.Word',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='word', full_name='app.Word.word', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=68,
  serialized_end=88,
)


_POINTS = _descriptor.Descriptor(
  name='Points',
  full_name='app.Points',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='messege', full_name='app.Points.messege', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='points', full_name='app.Points.points', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='pangram', full_name='app.Points.pangram', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=90,
  serialized_end=148,
)

DESCRIPTOR.message_types_by_name['Empty'] = _EMPTY
DESCRIPTOR.message_types_by_name['WorkPangram'] = _WORKPANGRAM
DESCRIPTOR.message_types_by_name['Word'] = _WORD
DESCRIPTOR.message_types_by_name['Points'] = _POINTS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Empty = _reflection.GeneratedProtocolMessageType('Empty', (_message.Message,), {
  'DESCRIPTOR' : _EMPTY,
  '__module__' : 'spelling_bee_pb2'
  # @@protoc_insertion_point(class_scope:app.Empty)
  })
_sym_db.RegisterMessage(Empty)

WorkPangram = _reflection.GeneratedProtocolMessageType('WorkPangram', (_message.Message,), {
  'DESCRIPTOR' : _WORKPANGRAM,
  '__module__' : 'spelling_bee_pb2'
  # @@protoc_insertion_point(class_scope:app.WorkPangram)
  })
_sym_db.RegisterMessage(WorkPangram)

Word = _reflection.GeneratedProtocolMessageType('Word', (_message.Message,), {
  'DESCRIPTOR' : _WORD,
  '__module__' : 'spelling_bee_pb2'
  # @@protoc_insertion_point(class_scope:app.Word)
  })
_sym_db.RegisterMessage(Word)

Points = _reflection.GeneratedProtocolMessageType('Points', (_message.Message,), {
  'DESCRIPTOR' : _POINTS,
  '__module__' : 'spelling_bee_pb2'
  # @@protoc_insertion_point(class_scope:app.Points)
  })
_sym_db.RegisterMessage(Points)



_SPELLINGBEE = _descriptor.ServiceDescriptor(
  name='SpellingBee',
  full_name='app.SpellingBee',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=150,
  serialized_end=245,
  methods=[
  _descriptor.MethodDescriptor(
    name='sayHello',
    full_name='app.SpellingBee.sayHello',
    index=0,
    containing_service=None,
    input_type=_EMPTY,
    output_type=_WORKPANGRAM,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='sendWork',
    full_name='app.SpellingBee.sendWork',
    index=1,
    containing_service=None,
    input_type=_WORD,
    output_type=_POINTS,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_SPELLINGBEE)

DESCRIPTOR.services_by_name['SpellingBee'] = _SPELLINGBEE

# @@protoc_insertion_point(module_scope)
