# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: robot_server.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='robot_server.proto',
  package='robot_server',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x12robot_server.proto\x12\x0crobot_server\"\x1a\n\x07Success\x12\x0f\n\x07success\x18\x01 \x01(\x08\"\x07\n\x05\x45mpty\")\n\x06\x41\x63tion\x12\x0e\n\x06\x61\x63tion\x18\x01 \x03(\x02\x12\x0f\n\x07success\x18\x02 \x01(\x08\"\x92\x03\n\x05State\x12\r\n\x05state\x18\x01 \x03(\x02\x12:\n\x0c\x66loat_params\x18\x02 \x03(\x0b\x32$.robot_server.State.FloatParamsEntry\x12<\n\rstring_params\x18\x03 \x03(\x0b\x32%.robot_server.State.StringParamsEntry\x12\x36\n\nstate_dict\x18\x04 \x03(\x0b\x32\".robot_server.State.StateDictEntry\x12\x0f\n\x07success\x18\x05 \x01(\x08\x12\r\n\x05image\x18\x06 \x01(\x0c\x12\r\n\x05\x64\x65pth\x18\x07 \x01(\x0c\x1a\x32\n\x10\x46loatParamsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x02:\x02\x38\x01\x1a\x33\n\x11StringParamsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a\x30\n\x0eStateDictEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x02:\x02\x38\x01\x32\xff\x01\n\x0bRobotServer\x12\x36\n\x08GetState\x12\x13.robot_server.Empty\x1a\x13.robot_server.State\"\x00\x12\x38\n\x08SetState\x12\x13.robot_server.State\x1a\x15.robot_server.Success\"\x00\x12;\n\nSendAction\x12\x14.robot_server.Action\x1a\x15.robot_server.Success\"\x00\x12\x41\n\x12SendActionGetState\x12\x14.robot_server.Action\x1a\x13.robot_server.State\"\x00\x62\x06proto3')
)




_SUCCESS = _descriptor.Descriptor(
  name='Success',
  full_name='robot_server.Success',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='robot_server.Success.success', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=36,
  serialized_end=62,
)


_EMPTY = _descriptor.Descriptor(
  name='Empty',
  full_name='robot_server.Empty',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
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
  serialized_start=64,
  serialized_end=71,
)


_ACTION = _descriptor.Descriptor(
  name='Action',
  full_name='robot_server.Action',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='action', full_name='robot_server.Action.action', index=0,
      number=1, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='success', full_name='robot_server.Action.success', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=73,
  serialized_end=114,
)


_STATE_FLOATPARAMSENTRY = _descriptor.Descriptor(
  name='FloatParamsEntry',
  full_name='robot_server.State.FloatParamsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='robot_server.State.FloatParamsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='robot_server.State.FloatParamsEntry.value', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=366,
  serialized_end=416,
)

_STATE_STRINGPARAMSENTRY = _descriptor.Descriptor(
  name='StringParamsEntry',
  full_name='robot_server.State.StringParamsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='robot_server.State.StringParamsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='robot_server.State.StringParamsEntry.value', index=1,
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
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=418,
  serialized_end=469,
)

_STATE_STATEDICTENTRY = _descriptor.Descriptor(
  name='StateDictEntry',
  full_name='robot_server.State.StateDictEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='robot_server.State.StateDictEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='robot_server.State.StateDictEntry.value', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=471,
  serialized_end=519,
)

_STATE = _descriptor.Descriptor(
  name='State',
  full_name='robot_server.State',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='state', full_name='robot_server.State.state', index=0,
      number=1, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='float_params', full_name='robot_server.State.float_params', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='string_params', full_name='robot_server.State.string_params', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='state_dict', full_name='robot_server.State.state_dict', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='success', full_name='robot_server.State.success', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='image', full_name='robot_server.State.image', index=5,
      number=6, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='depth', full_name='robot_server.State.depth', index=6,
      number=7, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_STATE_FLOATPARAMSENTRY, _STATE_STRINGPARAMSENTRY, _STATE_STATEDICTENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=117,
  serialized_end=519,
)

_STATE_FLOATPARAMSENTRY.containing_type = _STATE
_STATE_STRINGPARAMSENTRY.containing_type = _STATE
_STATE_STATEDICTENTRY.containing_type = _STATE
_STATE.fields_by_name['float_params'].message_type = _STATE_FLOATPARAMSENTRY
_STATE.fields_by_name['string_params'].message_type = _STATE_STRINGPARAMSENTRY
_STATE.fields_by_name['state_dict'].message_type = _STATE_STATEDICTENTRY
DESCRIPTOR.message_types_by_name['Success'] = _SUCCESS
DESCRIPTOR.message_types_by_name['Empty'] = _EMPTY
DESCRIPTOR.message_types_by_name['Action'] = _ACTION
DESCRIPTOR.message_types_by_name['State'] = _STATE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Success = _reflection.GeneratedProtocolMessageType('Success', (_message.Message,), dict(
  DESCRIPTOR = _SUCCESS,
  __module__ = 'robot_server_pb2'
  # @@protoc_insertion_point(class_scope:robot_server.Success)
  ))
_sym_db.RegisterMessage(Success)

Empty = _reflection.GeneratedProtocolMessageType('Empty', (_message.Message,), dict(
  DESCRIPTOR = _EMPTY,
  __module__ = 'robot_server_pb2'
  # @@protoc_insertion_point(class_scope:robot_server.Empty)
  ))
_sym_db.RegisterMessage(Empty)

Action = _reflection.GeneratedProtocolMessageType('Action', (_message.Message,), dict(
  DESCRIPTOR = _ACTION,
  __module__ = 'robot_server_pb2'
  # @@protoc_insertion_point(class_scope:robot_server.Action)
  ))
_sym_db.RegisterMessage(Action)

State = _reflection.GeneratedProtocolMessageType('State', (_message.Message,), dict(

  FloatParamsEntry = _reflection.GeneratedProtocolMessageType('FloatParamsEntry', (_message.Message,), dict(
    DESCRIPTOR = _STATE_FLOATPARAMSENTRY,
    __module__ = 'robot_server_pb2'
    # @@protoc_insertion_point(class_scope:robot_server.State.FloatParamsEntry)
    ))
  ,

  StringParamsEntry = _reflection.GeneratedProtocolMessageType('StringParamsEntry', (_message.Message,), dict(
    DESCRIPTOR = _STATE_STRINGPARAMSENTRY,
    __module__ = 'robot_server_pb2'
    # @@protoc_insertion_point(class_scope:robot_server.State.StringParamsEntry)
    ))
  ,

  StateDictEntry = _reflection.GeneratedProtocolMessageType('StateDictEntry', (_message.Message,), dict(
    DESCRIPTOR = _STATE_STATEDICTENTRY,
    __module__ = 'robot_server_pb2'
    # @@protoc_insertion_point(class_scope:robot_server.State.StateDictEntry)
    ))
  ,
  DESCRIPTOR = _STATE,
  __module__ = 'robot_server_pb2'
  # @@protoc_insertion_point(class_scope:robot_server.State)
  ))
_sym_db.RegisterMessage(State)
_sym_db.RegisterMessage(State.FloatParamsEntry)
_sym_db.RegisterMessage(State.StringParamsEntry)
_sym_db.RegisterMessage(State.StateDictEntry)


_STATE_FLOATPARAMSENTRY._options = None
_STATE_STRINGPARAMSENTRY._options = None
_STATE_STATEDICTENTRY._options = None

_ROBOTSERVER = _descriptor.ServiceDescriptor(
  name='RobotServer',
  full_name='robot_server.RobotServer',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=522,
  serialized_end=777,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetState',
    full_name='robot_server.RobotServer.GetState',
    index=0,
    containing_service=None,
    input_type=_EMPTY,
    output_type=_STATE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='SetState',
    full_name='robot_server.RobotServer.SetState',
    index=1,
    containing_service=None,
    input_type=_STATE,
    output_type=_SUCCESS,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='SendAction',
    full_name='robot_server.RobotServer.SendAction',
    index=2,
    containing_service=None,
    input_type=_ACTION,
    output_type=_SUCCESS,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='SendActionGetState',
    full_name='robot_server.RobotServer.SendActionGetState',
    index=3,
    containing_service=None,
    input_type=_ACTION,
    output_type=_STATE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_ROBOTSERVER)

DESCRIPTOR.services_by_name['RobotServer'] = _ROBOTSERVER

# @@protoc_insertion_point(module_scope)
