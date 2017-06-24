# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/data/raid/raid.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.enums import pokemon_id_pb2 as pogoprotos_dot_enums_dot_pokemon__id__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/data/raid/raid.proto',
  package='pogoprotos.data.raid',
  syntax='proto3',
  serialized_pb=_b('\n\x1fpogoprotos/data/raid/raid.proto\x12\x14pogoprotos.data.raid\x1a!pogoprotos/enums/pokemon_id.proto\"\xce\x01\n\x04Raid\x12\x11\n\traid_seed\x18\x01 \x01(\x03\x12\x12\n\nstarted_ms\x18\x02 \x01(\x03\x12\x14\n\x0c\x63ompleted_ms\x18\x03 \x01(\x03\x12\x39\n\x14\x65ncounter_pokemon_id\x18\x04 \x01(\x0e\x32\x1b.pogoprotos.enums.PokemonId\x12\x18\n\x10\x63ompleted_battle\x18\x05 \x01(\x08\x12\x18\n\x10received_rewards\x18\x06 \x01(\x08\x12\x1a\n\x12\x66inished_encounter\x18\x07 \x01(\x08\x62\x06proto3')
  ,
  dependencies=[pogoprotos_dot_enums_dot_pokemon__id__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_RAID = _descriptor.Descriptor(
  name='Raid',
  full_name='pogoprotos.data.raid.Raid',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='raid_seed', full_name='pogoprotos.data.raid.Raid.raid_seed', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='started_ms', full_name='pogoprotos.data.raid.Raid.started_ms', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='completed_ms', full_name='pogoprotos.data.raid.Raid.completed_ms', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='encounter_pokemon_id', full_name='pogoprotos.data.raid.Raid.encounter_pokemon_id', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='completed_battle', full_name='pogoprotos.data.raid.Raid.completed_battle', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='received_rewards', full_name='pogoprotos.data.raid.Raid.received_rewards', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='finished_encounter', full_name='pogoprotos.data.raid.Raid.finished_encounter', index=6,
      number=7, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=93,
  serialized_end=299,
)

_RAID.fields_by_name['encounter_pokemon_id'].enum_type = pogoprotos_dot_enums_dot_pokemon__id__pb2._POKEMONID
DESCRIPTOR.message_types_by_name['Raid'] = _RAID

Raid = _reflection.GeneratedProtocolMessageType('Raid', (_message.Message,), dict(
  DESCRIPTOR = _RAID,
  __module__ = 'pogoprotos.data.raid.raid_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.data.raid.Raid)
  ))
_sym_db.RegisterMessage(Raid)


# @@protoc_insertion_point(module_scope)
