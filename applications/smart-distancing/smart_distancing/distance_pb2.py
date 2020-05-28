# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: distance.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='distance.proto',
  package='distanceproto',
  syntax='proto3',
  serialized_pb=_b('\n\x0e\x64istance.proto\x12\rdistanceproto\"A\n\x05\x42\x61tch\x12\x12\n\nmax_frames\x18\x01 \x01(\r\x12$\n\x06\x66rames\x18\x02 \x03(\x0b\x32\x14.distanceproto.Frame\"h\n\x05\x46rame\x12\x11\n\tframe_num\x18\x01 \x01(\x05\x12\x11\n\tsource_id\x18\x02 \x01(\r\x12%\n\x06people\x18\x03 \x03(\x0b\x32\x15.distanceproto.Person\x12\x12\n\nsum_danger\x18\x04 \x01(\x02\"_\n\x06Person\x12\x0b\n\x03uid\x18\x01 \x01(\x05\x12\x11\n\tis_danger\x18\x02 \x01(\x08\x12\x12\n\ndanger_val\x18\x03 \x01(\x02\x12!\n\x04\x62\x62ox\x18\x04 \x01(\x0b\x32\x13.distanceproto.BBox\"@\n\x04\x42\x42ox\x12\x0c\n\x04left\x18\x01 \x01(\r\x12\x0b\n\x03top\x18\x02 \x01(\r\x12\x0e\n\x06height\x18\x03 \x01(\r\x12\r\n\x05width\x18\x04 \x01(\rb\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_BATCH = _descriptor.Descriptor(
  name='Batch',
  full_name='distanceproto.Batch',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='max_frames', full_name='distanceproto.Batch.max_frames', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='frames', full_name='distanceproto.Batch.frames', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=33,
  serialized_end=98,
)


_FRAME = _descriptor.Descriptor(
  name='Frame',
  full_name='distanceproto.Frame',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='frame_num', full_name='distanceproto.Frame.frame_num', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='source_id', full_name='distanceproto.Frame.source_id', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='people', full_name='distanceproto.Frame.people', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sum_danger', full_name='distanceproto.Frame.sum_danger', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=100,
  serialized_end=204,
)


_PERSON = _descriptor.Descriptor(
  name='Person',
  full_name='distanceproto.Person',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='uid', full_name='distanceproto.Person.uid', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='is_danger', full_name='distanceproto.Person.is_danger', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='danger_val', full_name='distanceproto.Person.danger_val', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bbox', full_name='distanceproto.Person.bbox', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=206,
  serialized_end=301,
)


_BBOX = _descriptor.Descriptor(
  name='BBox',
  full_name='distanceproto.BBox',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='left', full_name='distanceproto.BBox.left', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='top', full_name='distanceproto.BBox.top', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='height', full_name='distanceproto.BBox.height', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='width', full_name='distanceproto.BBox.width', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=303,
  serialized_end=367,
)

_BATCH.fields_by_name['frames'].message_type = _FRAME
_FRAME.fields_by_name['people'].message_type = _PERSON
_PERSON.fields_by_name['bbox'].message_type = _BBOX
DESCRIPTOR.message_types_by_name['Batch'] = _BATCH
DESCRIPTOR.message_types_by_name['Frame'] = _FRAME
DESCRIPTOR.message_types_by_name['Person'] = _PERSON
DESCRIPTOR.message_types_by_name['BBox'] = _BBOX

Batch = _reflection.GeneratedProtocolMessageType('Batch', (_message.Message,), dict(
  DESCRIPTOR = _BATCH,
  __module__ = 'distance_pb2'
  # @@protoc_insertion_point(class_scope:distanceproto.Batch)
  ))
_sym_db.RegisterMessage(Batch)

Frame = _reflection.GeneratedProtocolMessageType('Frame', (_message.Message,), dict(
  DESCRIPTOR = _FRAME,
  __module__ = 'distance_pb2'
  # @@protoc_insertion_point(class_scope:distanceproto.Frame)
  ))
_sym_db.RegisterMessage(Frame)

Person = _reflection.GeneratedProtocolMessageType('Person', (_message.Message,), dict(
  DESCRIPTOR = _PERSON,
  __module__ = 'distance_pb2'
  # @@protoc_insertion_point(class_scope:distanceproto.Person)
  ))
_sym_db.RegisterMessage(Person)

BBox = _reflection.GeneratedProtocolMessageType('BBox', (_message.Message,), dict(
  DESCRIPTOR = _BBOX,
  __module__ = 'distance_pb2'
  # @@protoc_insertion_point(class_scope:distanceproto.BBox)
  ))
_sym_db.RegisterMessage(BBox)


# @@protoc_insertion_point(module_scope)