from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NoteSequence(_message.Message):
    __slots__ = ["collection_name", "control_changes", "filename", "id", "instrument_infos", "key_signatures", "notes", "part_infos", "pitch_bends", "quantization_info", "reference_number", "section_annotations", "section_groups", "sequence_metadata", "source_info", "subsequence_info", "tempos", "text_annotations", "ticks_per_quarter", "time_signatures", "total_quantized_steps", "total_time"]
    class PitchName(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class ControlChange(_message.Message):
        __slots__ = ["control_number", "control_value", "instrument", "is_drum", "program", "quantized_step", "time"]
        CONTROL_NUMBER_FIELD_NUMBER: _ClassVar[int]
        CONTROL_VALUE_FIELD_NUMBER: _ClassVar[int]
        INSTRUMENT_FIELD_NUMBER: _ClassVar[int]
        IS_DRUM_FIELD_NUMBER: _ClassVar[int]
        PROGRAM_FIELD_NUMBER: _ClassVar[int]
        QUANTIZED_STEP_FIELD_NUMBER: _ClassVar[int]
        TIME_FIELD_NUMBER: _ClassVar[int]
        control_number: int
        control_value: int
        instrument: int
        is_drum: bool
        program: int
        quantized_step: int
        time: float
        def __init__(self, time: _Optional[float] = ..., quantized_step: _Optional[int] = ..., control_number: _Optional[int] = ..., control_value: _Optional[int] = ..., instrument: _Optional[int] = ..., program: _Optional[int] = ..., is_drum: bool = ...) -> None: ...
    class InstrumentInfo(_message.Message):
        __slots__ = ["instrument", "name"]
        INSTRUMENT_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        instrument: int
        name: str
        def __init__(self, instrument: _Optional[int] = ..., name: _Optional[str] = ...) -> None: ...
    class KeySignature(_message.Message):
        __slots__ = ["key", "mode", "time"]
        class Key(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = []
        class Mode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = []
        A: NoteSequence.KeySignature.Key
        A_FLAT: NoteSequence.KeySignature.Key
        A_SHARP: NoteSequence.KeySignature.Key
        B: NoteSequence.KeySignature.Key
        B_FLAT: NoteSequence.KeySignature.Key
        C: NoteSequence.KeySignature.Key
        C_SHARP: NoteSequence.KeySignature.Key
        D: NoteSequence.KeySignature.Key
        DORIAN: NoteSequence.KeySignature.Mode
        D_FLAT: NoteSequence.KeySignature.Key
        D_SHARP: NoteSequence.KeySignature.Key
        E: NoteSequence.KeySignature.Key
        E_FLAT: NoteSequence.KeySignature.Key
        F: NoteSequence.KeySignature.Key
        F_SHARP: NoteSequence.KeySignature.Key
        G: NoteSequence.KeySignature.Key
        G_FLAT: NoteSequence.KeySignature.Key
        G_SHARP: NoteSequence.KeySignature.Key
        KEY_FIELD_NUMBER: _ClassVar[int]
        LOCRIAN: NoteSequence.KeySignature.Mode
        LYDIAN: NoteSequence.KeySignature.Mode
        MAJOR: NoteSequence.KeySignature.Mode
        MINOR: NoteSequence.KeySignature.Mode
        MIXOLYDIAN: NoteSequence.KeySignature.Mode
        MODE_FIELD_NUMBER: _ClassVar[int]
        NOT_SPECIFIED: NoteSequence.KeySignature.Mode
        PHRYGIAN: NoteSequence.KeySignature.Mode
        TIME_FIELD_NUMBER: _ClassVar[int]
        key: NoteSequence.KeySignature.Key
        mode: NoteSequence.KeySignature.Mode
        time: float
        def __init__(self, time: _Optional[float] = ..., key: _Optional[_Union[NoteSequence.KeySignature.Key, str]] = ..., mode: _Optional[_Union[NoteSequence.KeySignature.Mode, str]] = ...) -> None: ...
    class Note(_message.Message):
        __slots__ = ["denominator", "end_time", "instrument", "is_drum", "numerator", "part", "pitch", "pitch_name", "program", "quantized_end_step", "quantized_start_step", "start_time", "velocity", "voice"]
        DENOMINATOR_FIELD_NUMBER: _ClassVar[int]
        END_TIME_FIELD_NUMBER: _ClassVar[int]
        INSTRUMENT_FIELD_NUMBER: _ClassVar[int]
        IS_DRUM_FIELD_NUMBER: _ClassVar[int]
        NUMERATOR_FIELD_NUMBER: _ClassVar[int]
        PART_FIELD_NUMBER: _ClassVar[int]
        PITCH_FIELD_NUMBER: _ClassVar[int]
        PITCH_NAME_FIELD_NUMBER: _ClassVar[int]
        PROGRAM_FIELD_NUMBER: _ClassVar[int]
        QUANTIZED_END_STEP_FIELD_NUMBER: _ClassVar[int]
        QUANTIZED_START_STEP_FIELD_NUMBER: _ClassVar[int]
        START_TIME_FIELD_NUMBER: _ClassVar[int]
        VELOCITY_FIELD_NUMBER: _ClassVar[int]
        VOICE_FIELD_NUMBER: _ClassVar[int]
        denominator: int
        end_time: float
        instrument: int
        is_drum: bool
        numerator: int
        part: int
        pitch: int
        pitch_name: NoteSequence.PitchName
        program: int
        quantized_end_step: int
        quantized_start_step: int
        start_time: float
        velocity: int
        voice: int
        # chord field should be a one hot encoding of the notes in the chord. 
        chord: [int]
        def __init__(self, pitch: _Optional[int] = ..., pitch_name: _Optional[_Union[NoteSequence.PitchName, str]] = ..., velocity: _Optional[int] = ..., start_time: _Optional[float] = ..., quantized_start_step: _Optional[int] = ..., end_time: _Optional[float] = ..., quantized_end_step: _Optional[int] = ..., numerator: _Optional[int] = ..., denominator: _Optional[int] = ..., instrument: _Optional[int] = ..., program: _Optional[int] = ..., is_drum: bool = ..., part: _Optional[int] = ..., voice: _Optional[int] = ...) -> None: ...
    class PartInfo(_message.Message):
        __slots__ = ["name", "part"]
        NAME_FIELD_NUMBER: _ClassVar[int]
        PART_FIELD_NUMBER: _ClassVar[int]
        name: str
        part: int
        def __init__(self, part: _Optional[int] = ..., name: _Optional[str] = ...) -> None: ...
    class PitchBend(_message.Message):
        __slots__ = ["bend", "instrument", "is_drum", "program", "time"]
        BEND_FIELD_NUMBER: _ClassVar[int]
        INSTRUMENT_FIELD_NUMBER: _ClassVar[int]
        IS_DRUM_FIELD_NUMBER: _ClassVar[int]
        PROGRAM_FIELD_NUMBER: _ClassVar[int]
        TIME_FIELD_NUMBER: _ClassVar[int]
        bend: int
        instrument: int
        is_drum: bool
        program: int
        time: float
        def __init__(self, time: _Optional[float] = ..., bend: _Optional[int] = ..., instrument: _Optional[int] = ..., program: _Optional[int] = ..., is_drum: bool = ...) -> None: ...
    class QuantizationInfo(_message.Message):
        __slots__ = ["steps_per_quarter", "steps_per_second"]
        STEPS_PER_QUARTER_FIELD_NUMBER: _ClassVar[int]
        STEPS_PER_SECOND_FIELD_NUMBER: _ClassVar[int]
        steps_per_quarter: int
        steps_per_second: int
        def __init__(self, steps_per_quarter: _Optional[int] = ..., steps_per_second: _Optional[int] = ...) -> None: ...
    class Section(_message.Message):
        __slots__ = ["section_group", "section_id"]
        SECTION_GROUP_FIELD_NUMBER: _ClassVar[int]
        SECTION_ID_FIELD_NUMBER: _ClassVar[int]
        section_group: NoteSequence.SectionGroup
        section_id: int
        def __init__(self, section_id: _Optional[int] = ..., section_group: _Optional[_Union[NoteSequence.SectionGroup, _Mapping]] = ...) -> None: ...
    class SectionAnnotation(_message.Message):
        __slots__ = ["section_id", "time"]
        SECTION_ID_FIELD_NUMBER: _ClassVar[int]
        TIME_FIELD_NUMBER: _ClassVar[int]
        section_id: int
        time: float
        def __init__(self, time: _Optional[float] = ..., section_id: _Optional[int] = ...) -> None: ...
    class SectionGroup(_message.Message):
        __slots__ = ["num_times", "sections"]
        NUM_TIMES_FIELD_NUMBER: _ClassVar[int]
        SECTIONS_FIELD_NUMBER: _ClassVar[int]
        num_times: int
        sections: _containers.RepeatedCompositeFieldContainer[NoteSequence.Section]
        def __init__(self, sections: _Optional[_Iterable[_Union[NoteSequence.Section, _Mapping]]] = ..., num_times: _Optional[int] = ...) -> None: ...
    class SourceInfo(_message.Message):
        __slots__ = ["encoding_type", "parser", "source_type"]
        class EncodingType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = []
        class Parser(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = []
        class SourceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = []
        ABC: NoteSequence.SourceInfo.EncodingType
        ENCODING_TYPE_FIELD_NUMBER: _ClassVar[int]
        MAGENTA_ABC: NoteSequence.SourceInfo.Parser
        MAGENTA_MUSICNET: NoteSequence.SourceInfo.Parser
        MAGENTA_MUSIC_XML: NoteSequence.SourceInfo.Parser
        MIDI: NoteSequence.SourceInfo.EncodingType
        MUSIC21: NoteSequence.SourceInfo.Parser
        MUSICNET: NoteSequence.SourceInfo.EncodingType
        MUSIC_XML: NoteSequence.SourceInfo.EncodingType
        PARSER_FIELD_NUMBER: _ClassVar[int]
        PERFORMANCE_BASED: NoteSequence.SourceInfo.SourceType
        PRETTY_MIDI: NoteSequence.SourceInfo.Parser
        SCORE_BASED: NoteSequence.SourceInfo.SourceType
        SOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
        TONEJS_MIDI_CONVERT: NoteSequence.SourceInfo.Parser
        UNKNOWN_ENCODING_TYPE: NoteSequence.SourceInfo.EncodingType
        UNKNOWN_PARSER: NoteSequence.SourceInfo.Parser
        UNKNOWN_SOURCE_TYPE: NoteSequence.SourceInfo.SourceType
        encoding_type: NoteSequence.SourceInfo.EncodingType
        parser: NoteSequence.SourceInfo.Parser
        source_type: NoteSequence.SourceInfo.SourceType
        def __init__(self, source_type: _Optional[_Union[NoteSequence.SourceInfo.SourceType, str]] = ..., encoding_type: _Optional[_Union[NoteSequence.SourceInfo.EncodingType, str]] = ..., parser: _Optional[_Union[NoteSequence.SourceInfo.Parser, str]] = ...) -> None: ...
    class SubsequenceInfo(_message.Message):
        __slots__ = ["end_time_offset", "start_time_offset"]
        END_TIME_OFFSET_FIELD_NUMBER: _ClassVar[int]
        START_TIME_OFFSET_FIELD_NUMBER: _ClassVar[int]
        end_time_offset: float
        start_time_offset: float
        def __init__(self, start_time_offset: _Optional[float] = ..., end_time_offset: _Optional[float] = ...) -> None: ...
    class Tempo(_message.Message):
        __slots__ = ["qpm", "time"]
        QPM_FIELD_NUMBER: _ClassVar[int]
        TIME_FIELD_NUMBER: _ClassVar[int]
        qpm: float
        time: float
        def __init__(self, time: _Optional[float] = ..., qpm: _Optional[float] = ...) -> None: ...
    class TextAnnotation(_message.Message):
        __slots__ = ["annotation_type", "quantized_step", "text", "time"]
        class TextAnnotationType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = []
        ANNOTATION_TYPE_FIELD_NUMBER: _ClassVar[int]
        BEAT: NoteSequence.TextAnnotation.TextAnnotationType
        CHORD_SYMBOL: NoteSequence.TextAnnotation.TextAnnotationType
        QUANTIZED_STEP_FIELD_NUMBER: _ClassVar[int]
        TEXT_FIELD_NUMBER: _ClassVar[int]
        TIME_FIELD_NUMBER: _ClassVar[int]
        UNKNOWN: NoteSequence.TextAnnotation.TextAnnotationType
        annotation_type: NoteSequence.TextAnnotation.TextAnnotationType
        quantized_step: int
        text: str
        time: float
        def __init__(self, time: _Optional[float] = ..., quantized_step: _Optional[int] = ..., text: _Optional[str] = ..., annotation_type: _Optional[_Union[NoteSequence.TextAnnotation.TextAnnotationType, str]] = ...) -> None: ...
    class TimeSignature(_message.Message):
        __slots__ = ["denominator", "numerator", "time"]
        DENOMINATOR_FIELD_NUMBER: _ClassVar[int]
        NUMERATOR_FIELD_NUMBER: _ClassVar[int]
        TIME_FIELD_NUMBER: _ClassVar[int]
        denominator: int
        numerator: int
        time: float
        def __init__(self, time: _Optional[float] = ..., numerator: _Optional[int] = ..., denominator: _Optional[int] = ...) -> None: ...
    A: NoteSequence.PitchName
    A_FLAT: NoteSequence.PitchName
    A_FLAT_FLAT: NoteSequence.PitchName
    A_SHARP: NoteSequence.PitchName
    A_SHARP_SHARP: NoteSequence.PitchName
    B: NoteSequence.PitchName
    B_FLAT: NoteSequence.PitchName
    B_FLAT_FLAT: NoteSequence.PitchName
    B_SHARP: NoteSequence.PitchName
    B_SHARP_SHARP: NoteSequence.PitchName
    C: NoteSequence.PitchName
    COLLECTION_NAME_FIELD_NUMBER: _ClassVar[int]
    CONTROL_CHANGES_FIELD_NUMBER: _ClassVar[int]
    C_FLAT: NoteSequence.PitchName
    C_FLAT_FLAT: NoteSequence.PitchName
    C_SHARP: NoteSequence.PitchName
    C_SHARP_SHARP: NoteSequence.PitchName
    D: NoteSequence.PitchName
    D_FLAT: NoteSequence.PitchName
    D_FLAT_FLAT: NoteSequence.PitchName
    D_SHARP: NoteSequence.PitchName
    D_SHARP_SHARP: NoteSequence.PitchName
    E: NoteSequence.PitchName
    E_FLAT: NoteSequence.PitchName
    E_FLAT_FLAT: NoteSequence.PitchName
    E_SHARP: NoteSequence.PitchName
    E_SHARP_SHARP: NoteSequence.PitchName
    F: NoteSequence.PitchName
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    F_FLAT: NoteSequence.PitchName
    F_FLAT_FLAT: NoteSequence.PitchName
    F_SHARP: NoteSequence.PitchName
    F_SHARP_SHARP: NoteSequence.PitchName
    G: NoteSequence.PitchName
    G_FLAT: NoteSequence.PitchName
    G_FLAT_FLAT: NoteSequence.PitchName
    G_SHARP: NoteSequence.PitchName
    G_SHARP_SHARP: NoteSequence.PitchName
    ID_FIELD_NUMBER: _ClassVar[int]
    INSTRUMENT_INFOS_FIELD_NUMBER: _ClassVar[int]
    KEY_SIGNATURES_FIELD_NUMBER: _ClassVar[int]
    NOTES_FIELD_NUMBER: _ClassVar[int]
    PART_INFOS_FIELD_NUMBER: _ClassVar[int]
    PITCH_BENDS_FIELD_NUMBER: _ClassVar[int]
    QUANTIZATION_INFO_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    SECTION_ANNOTATIONS_FIELD_NUMBER: _ClassVar[int]
    SECTION_GROUPS_FIELD_NUMBER: _ClassVar[int]
    SEQUENCE_METADATA_FIELD_NUMBER: _ClassVar[int]
    SOURCE_INFO_FIELD_NUMBER: _ClassVar[int]
    SUBSEQUENCE_INFO_FIELD_NUMBER: _ClassVar[int]
    TEMPOS_FIELD_NUMBER: _ClassVar[int]
    TEXT_ANNOTATIONS_FIELD_NUMBER: _ClassVar[int]
    TICKS_PER_QUARTER_FIELD_NUMBER: _ClassVar[int]
    TIME_SIGNATURES_FIELD_NUMBER: _ClassVar[int]
    TOTAL_QUANTIZED_STEPS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_TIME_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN_PITCH_NAME: NoteSequence.PitchName
    collection_name: str
    control_changes: _containers.RepeatedCompositeFieldContainer[NoteSequence.ControlChange]
    filename: str
    id: str
    instrument_infos: _containers.RepeatedCompositeFieldContainer[NoteSequence.InstrumentInfo]
    key_signatures: _containers.RepeatedCompositeFieldContainer[NoteSequence.KeySignature]
    notes: _containers.RepeatedCompositeFieldContainer[NoteSequence.Note]
    part_infos: _containers.RepeatedCompositeFieldContainer[NoteSequence.PartInfo]
    pitch_bends: _containers.RepeatedCompositeFieldContainer[NoteSequence.PitchBend]
    quantization_info: NoteSequence.QuantizationInfo
    reference_number: int
    section_annotations: _containers.RepeatedCompositeFieldContainer[NoteSequence.SectionAnnotation]
    section_groups: _containers.RepeatedCompositeFieldContainer[NoteSequence.SectionGroup]
    sequence_metadata: SequenceMetadata
    source_info: NoteSequence.SourceInfo
    subsequence_info: NoteSequence.SubsequenceInfo
    tempos: _containers.RepeatedCompositeFieldContainer[NoteSequence.Tempo]
    text_annotations: _containers.RepeatedCompositeFieldContainer[NoteSequence.TextAnnotation]
    ticks_per_quarter: int
    time_signatures: _containers.RepeatedCompositeFieldContainer[NoteSequence.TimeSignature]
    total_quantized_steps: int
    total_time: float
    def __init__(self, id: _Optional[str] = ..., filename: _Optional[str] = ..., reference_number: _Optional[int] = ..., collection_name: _Optional[str] = ..., ticks_per_quarter: _Optional[int] = ..., time_signatures: _Optional[_Iterable[_Union[NoteSequence.TimeSignature, _Mapping]]] = ..., key_signatures: _Optional[_Iterable[_Union[NoteSequence.KeySignature, _Mapping]]] = ..., tempos: _Optional[_Iterable[_Union[NoteSequence.Tempo, _Mapping]]] = ..., notes: _Optional[_Iterable[_Union[NoteSequence.Note, _Mapping]]] = ..., total_time: _Optional[float] = ..., total_quantized_steps: _Optional[int] = ..., pitch_bends: _Optional[_Iterable[_Union[NoteSequence.PitchBend, _Mapping]]] = ..., control_changes: _Optional[_Iterable[_Union[NoteSequence.ControlChange, _Mapping]]] = ..., part_infos: _Optional[_Iterable[_Union[NoteSequence.PartInfo, _Mapping]]] = ..., source_info: _Optional[_Union[NoteSequence.SourceInfo, _Mapping]] = ..., text_annotations: _Optional[_Iterable[_Union[NoteSequence.TextAnnotation, _Mapping]]] = ..., section_annotations: _Optional[_Iterable[_Union[NoteSequence.SectionAnnotation, _Mapping]]] = ..., section_groups: _Optional[_Iterable[_Union[NoteSequence.SectionGroup, _Mapping]]] = ..., quantization_info: _Optional[_Union[NoteSequence.QuantizationInfo, _Mapping]] = ..., subsequence_info: _Optional[_Union[NoteSequence.SubsequenceInfo, _Mapping]] = ..., sequence_metadata: _Optional[_Union[SequenceMetadata, _Mapping]] = ..., instrument_infos: _Optional[_Iterable[_Union[NoteSequence.InstrumentInfo, _Mapping]]] = ...) -> None: ...

class SequenceMetadata(_message.Message):
    __slots__ = ["artist", "composers", "genre", "title"]
    ARTIST_FIELD_NUMBER: _ClassVar[int]
    COMPOSERS_FIELD_NUMBER: _ClassVar[int]
    GENRE_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    artist: str
    composers: _containers.RepeatedScalarFieldContainer[str]
    genre: _containers.RepeatedScalarFieldContainer[str]
    title: str
    def __init__(self, title: _Optional[str] = ..., artist: _Optional[str] = ..., genre: _Optional[_Iterable[str]] = ..., composers: _Optional[_Iterable[str]] = ...) -> None: ...

class VelocityRange(_message.Message):
    __slots__ = ["max", "min"]
    MAX_FIELD_NUMBER: _ClassVar[int]
    MIN_FIELD_NUMBER: _ClassVar[int]
    max: int
    min: int
    def __init__(self, min: _Optional[int] = ..., max: _Optional[int] = ...) -> None: ...
