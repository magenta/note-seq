from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GeneratorDetails(_message.Message):
    __slots__ = ["id", "description"]
    ID_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    id: str
    description: str
    def __init__(self, id: _Optional[str] = ..., description: _Optional[str] = ...) -> None: ...

class GeneratorOptions(_message.Message):
    __slots__ = ["input_sections", "generate_sections", "args"]
    class SequenceSection(_message.Message):
        __slots__ = ["start_time", "end_time"]
        START_TIME_FIELD_NUMBER: _ClassVar[int]
        END_TIME_FIELD_NUMBER: _ClassVar[int]
        start_time: float
        end_time: float
        def __init__(self, start_time: _Optional[float] = ..., end_time: _Optional[float] = ...) -> None: ...
    class ArgValue(_message.Message):
        __slots__ = ["byte_value", "int_value", "float_value", "bool_value", "string_value"]
        BYTE_VALUE_FIELD_NUMBER: _ClassVar[int]
        INT_VALUE_FIELD_NUMBER: _ClassVar[int]
        FLOAT_VALUE_FIELD_NUMBER: _ClassVar[int]
        BOOL_VALUE_FIELD_NUMBER: _ClassVar[int]
        STRING_VALUE_FIELD_NUMBER: _ClassVar[int]
        byte_value: bytes
        int_value: int
        float_value: float
        bool_value: bool
        string_value: str
        def __init__(self, byte_value: _Optional[bytes] = ..., int_value: _Optional[int] = ..., float_value: _Optional[float] = ..., bool_value: bool = ..., string_value: _Optional[str] = ...) -> None: ...
    class ArgsEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: GeneratorOptions.ArgValue
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[GeneratorOptions.ArgValue, _Mapping]] = ...) -> None: ...
    INPUT_SECTIONS_FIELD_NUMBER: _ClassVar[int]
    GENERATE_SECTIONS_FIELD_NUMBER: _ClassVar[int]
    ARGS_FIELD_NUMBER: _ClassVar[int]
    input_sections: _containers.RepeatedCompositeFieldContainer[GeneratorOptions.SequenceSection]
    generate_sections: _containers.RepeatedCompositeFieldContainer[GeneratorOptions.SequenceSection]
    args: _containers.MessageMap[str, GeneratorOptions.ArgValue]
    def __init__(self, input_sections: _Optional[_Iterable[_Union[GeneratorOptions.SequenceSection, _Mapping]]] = ..., generate_sections: _Optional[_Iterable[_Union[GeneratorOptions.SequenceSection, _Mapping]]] = ..., args: _Optional[_Mapping[str, GeneratorOptions.ArgValue]] = ...) -> None: ...

class GeneratorBundle(_message.Message):
    __slots__ = ["generator_details", "bundle_details", "checkpoint_file", "metagraph_file"]
    class BundleDetails(_message.Message):
        __slots__ = ["description"]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        description: str
        def __init__(self, description: _Optional[str] = ...) -> None: ...
    GENERATOR_DETAILS_FIELD_NUMBER: _ClassVar[int]
    BUNDLE_DETAILS_FIELD_NUMBER: _ClassVar[int]
    CHECKPOINT_FILE_FIELD_NUMBER: _ClassVar[int]
    METAGRAPH_FILE_FIELD_NUMBER: _ClassVar[int]
    generator_details: GeneratorDetails
    bundle_details: GeneratorBundle.BundleDetails
    checkpoint_file: _containers.RepeatedScalarFieldContainer[bytes]
    metagraph_file: bytes
    def __init__(self, generator_details: _Optional[_Union[GeneratorDetails, _Mapping]] = ..., bundle_details: _Optional[_Union[GeneratorBundle.BundleDetails, _Mapping]] = ..., checkpoint_file: _Optional[_Iterable[bytes]] = ..., metagraph_file: _Optional[bytes] = ...) -> None: ...
