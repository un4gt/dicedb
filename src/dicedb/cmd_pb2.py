# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cmd.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\tcmd.proto\x12\x04wire\x1a\x1cgoogle/protobuf/struct.proto\"$\n\x07\x43ommand\x12\x0b\n\x03\x63md\x18\x01 \x01(\t\x12\x0c\n\x04\x61rgs\x18\x02 \x03(\t\"\xa6\x02\n\x08Response\x12\x0b\n\x03\x65rr\x18\x01 \x01(\t\x12\x0f\n\x05v_nil\x18\x02 \x01(\x08H\x00\x12\x0f\n\x05v_int\x18\x03 \x01(\x03H\x00\x12\x0f\n\x05v_str\x18\x04 \x01(\tH\x00\x12\x11\n\x07v_float\x18\x05 \x01(\x01H\x00\x12\x11\n\x07v_bytes\x18\x06 \x01(\x0cH\x00\x12&\n\x05\x61ttrs\x18\x07 \x01(\x0b\x32\x17.google.protobuf.Struct\x12&\n\x06v_list\x18\x08 \x03(\x0b\x32\x16.google.protobuf.Value\x12,\n\x08v_ss_map\x18\t \x03(\x0b\x32\x1a.wire.Response.VSsMapEntry\x1a-\n\x0bVSsMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x42\x07\n\x05valueB\x08Z\x06./wireb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cmd_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z\006./wire'
  _RESPONSE_VSSMAPENTRY._options = None
  _RESPONSE_VSSMAPENTRY._serialized_options = b'8\001'
  _COMMAND._serialized_start=49
  _COMMAND._serialized_end=85
  _RESPONSE._serialized_start=88
  _RESPONSE._serialized_end=382
  _RESPONSE_VSSMAPENTRY._serialized_start=328
  _RESPONSE_VSSMAPENTRY._serialized_end=373
# @@protoc_insertion_point(module_scope)
