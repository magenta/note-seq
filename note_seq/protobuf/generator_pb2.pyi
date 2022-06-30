from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GeneratorBundle(_message.Message):
    __slots__ = ["bundle_details", "checkpoint_file", "generator_details", "metagraph_file"]
    class BundleDetails(_message.Message):
        __slots__ = ["description"]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        description: str
        def __init__(self, description: _Optional[str] = ...) -> None: ...
    BUNDLE_DETAILS_FIELD_NUMBER: _ClassVar[int]
    CHECKPOINT_FILE_FIELD_NUMBER: _ClassVar[int]
    GENERATOR_DETAILS_FIELD_NUMBER: _ClassVar[int]
    METAGRAPH_FILE_FIELD_NUMBER: _ClassVar[int]
    bundle_details: GeneratorBundle.BundleDetails
    checkpoint_file: _containers.RepeatedScalarFieldContainer[bytes]
    generator_details: GeneratorDetails
    metagraph_file: bytes
    def __init__(self, generator_details: _Optional[_Union[GeneratorDetails, _Mapping]] = ..., bundle_details: _Optional[_Union[GeneratorBundle.BundleDetails, _Mapping]] = ..., checkpoint_file: _Optional[_Iterable[bytes]] = ..., metagraph_file: _Optional[bytes] = ...) -> None: ...

class GeneratorDetails(_message.Message):
    __slots__ = ["description", "id"]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    description: str
    id: str
    def __init__(self, id: _Optional[str] = ..., description: _Optional[str] = ...) -> None: ...

class GeneratorOptions(_message.Message):
    __slots__ = ["args", "generate_sections", "input_sections"]
    class ArgValue(_message.Message):
        __slots__ = ["bool_value", "byte_value", "float_value", "int_value", "string_value"]
        BOOL_VALUE_FIELD_NUMBER: _ClassVar[int]
        BYTE_VALUE_FIELD_NUMBER: _ClassVar[int]
        FLOAT_VALUE_FIELD_NUMBER: _ClassVar[int]
        INT_VALUE_FIELD_NUMBER: _ClassVar[int]
        STRING_VALUE_FIELD_NUMBER: _ClassVar[int]
        bool_value: bool
        byte_value: bytes
        float_value: float
        int_value: int
        string_value: str
        def __init__(self, byte_value: _Optional[bytes] = ..., int_value: _Optional[int] = ..., float_value: _Optional[float] = ..., bool_value: bool = ..., string_value: _Optional[str] = ...) -> None: ...
    class ArgsEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: GeneratorOptions.ArgValue
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[GeneratorOptions.ArgValue, _Mapping]] = ...) -> None: ...
    class SequenceSection(_message.Message):
        __slots__ = ["end_time", "start_time"]
        END_TIME_FIELD_NUMBER: _ClassVar[int]
        START_TIME_FIELD_NUMBER: _ClassVar[int]
        end_time: float
        start_time: float
        def __init__(self, start_time: _Optional[float] = ..., end_time: _Optional[float] = ...) -> None: ...
    ARGS_FIELD_NUMBER: _ClassVar[int]
    GENERATE_SECTIONS_FIELD_NUMBER: _ClassVar[int]
    INPUT_SECTIONS_FIELD_NUMBER: _ClassVar[int]
    args: _containers.MessageMap[str, GeneratorOptions.ArgValue]
    generate_sections: _containers.RepeatedCompositeFieldContainer[GeneratorOptions.SequenceSection]
    input_sections: _containers.RepeatedCompositeFieldContainer[GeneratorOptions.SequenceSection]
    def __init__(self, input_sections: _Optional[_Iterable[_Union[GeneratorOptions.SequenceSection, _Mapping]]] = ..., generate_sections: _Optional[_Iterable[_Union[GeneratorOptions.SequenceSection, _Mapping]]] = ..., args: _Optional[_Mapping[str, GeneratorOptions.ArgValue]] = ...) -> None: ...
