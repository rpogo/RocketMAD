# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/settings/master/onboarding_settings.proto

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
  name='pogoprotos/settings/master/onboarding_settings.proto',
  package='pogoprotos.settings.master',
  syntax='proto3',
  serialized_pb=_b('\n4pogoprotos/settings/master/onboarding_settings.proto\x12\x1apogoprotos.settings.master\"z\n\x12OnboardingSettings\x12!\n\x19skip_avatar_customization\x18\x01 \x01(\x08\x12!\n\x19\x64isable_initial_ar_prompt\x18\x02 \x01(\x08\x12\x1e\n\x16\x61r_prompt_player_level\x18\x03 \x01(\rb\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_ONBOARDINGSETTINGS = _descriptor.Descriptor(
  name='OnboardingSettings',
  full_name='pogoprotos.settings.master.OnboardingSettings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='skip_avatar_customization', full_name='pogoprotos.settings.master.OnboardingSettings.skip_avatar_customization', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='disable_initial_ar_prompt', full_name='pogoprotos.settings.master.OnboardingSettings.disable_initial_ar_prompt', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ar_prompt_player_level', full_name='pogoprotos.settings.master.OnboardingSettings.ar_prompt_player_level', index=2,
      number=3, type=13, cpp_type=3, label=1,
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
  serialized_start=84,
  serialized_end=206,
)

DESCRIPTOR.message_types_by_name['OnboardingSettings'] = _ONBOARDINGSETTINGS

OnboardingSettings = _reflection.GeneratedProtocolMessageType('OnboardingSettings', (_message.Message,), dict(
  DESCRIPTOR = _ONBOARDINGSETTINGS,
  __module__ = 'pogoprotos.settings.master.onboarding_settings_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.settings.master.OnboardingSettings)
  ))
_sym_db.RegisterMessage(OnboardingSettings)


# @@protoc_insertion_point(module_scope)