from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NoteSequence(_message.Message):
    __slots__ = ["id", "filename", "reference_number", "collection_name", "ticks_per_quarter", "time_signatures", "key_signatures", "tempos", "notes", "total_time", "total_quantized_steps", "pitch_bends", "control_changes", "part_infos", "source_info", "text_annotations", "section_annotations", "section_groups", "quantization_info", "subsequence_info", "sequence_metadata", "instrument_infos", "fingering"]
    class PitchName(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
        UNKNOWN_PITCH_NAME: _ClassVar[NoteSequence.PitchName]
        F_FLAT_FLAT: _ClassVar[NoteSequence.PitchName]
        C_FLAT_FLAT: _ClassVar[NoteSequence.PitchName]
        G_FLAT_FLAT: _ClassVar[NoteSequence.PitchName]
        D_FLAT_FLAT: _ClassVar[NoteSequence.PitchName]
        A_FLAT_FLAT: _ClassVar[NoteSequence.PitchName]
        E_FLAT_FLAT: _ClassVar[NoteSequence.PitchName]
        B_FLAT_FLAT: _ClassVar[NoteSequence.PitchName]
        F_FLAT: _ClassVar[NoteSequence.PitchName]
        C_FLAT: _ClassVar[NoteSequence.PitchName]
        G_FLAT: _ClassVar[NoteSequence.PitchName]
        D_FLAT: _ClassVar[NoteSequence.PitchName]
        A_FLAT: _ClassVar[NoteSequence.PitchName]
        E_FLAT: _ClassVar[NoteSequence.PitchName]
        B_FLAT: _ClassVar[NoteSequence.PitchName]
        F: _ClassVar[NoteSequence.PitchName]
        C: _ClassVar[NoteSequence.PitchName]
        G: _ClassVar[NoteSequence.PitchName]
        D: _ClassVar[NoteSequence.PitchName]
        A: _ClassVar[NoteSequence.PitchName]
        E: _ClassVar[NoteSequence.PitchName]
        B: _ClassVar[NoteSequence.PitchName]
        F_SHARP: _ClassVar[NoteSequence.PitchName]
        C_SHARP: _ClassVar[NoteSequence.PitchName]
        G_SHARP: _ClassVar[NoteSequence.PitchName]
        D_SHARP: _ClassVar[NoteSequence.PitchName]
        A_SHARP: _ClassVar[NoteSequence.PitchName]
        E_SHARP: _ClassVar[NoteSequence.PitchName]
        B_SHARP: _ClassVar[NoteSequence.PitchName]
        F_SHARP_SHARP: _ClassVar[NoteSequence.PitchName]
        C_SHARP_SHARP: _ClassVar[NoteSequence.PitchName]
        G_SHARP_SHARP: _ClassVar[NoteSequence.PitchName]
        D_SHARP_SHARP: _ClassVar[NoteSequence.PitchName]
        A_SHARP_SHARP: _ClassVar[NoteSequence.PitchName]
        E_SHARP_SHARP: _ClassVar[NoteSequence.PitchName]
        B_SHARP_SHARP: _ClassVar[NoteSequence.PitchName]
    UNKNOWN_PITCH_NAME: NoteSequence.PitchName
    F_FLAT_FLAT: NoteSequence.PitchName
    C_FLAT_FLAT: NoteSequence.PitchName
    G_FLAT_FLAT: NoteSequence.PitchName
    D_FLAT_FLAT: NoteSequence.PitchName
    A_FLAT_FLAT: NoteSequence.PitchName
    E_FLAT_FLAT: NoteSequence.PitchName
    B_FLAT_FLAT: NoteSequence.PitchName
    F_FLAT: NoteSequence.PitchName
    C_FLAT: NoteSequence.PitchName
    G_FLAT: NoteSequence.PitchName
    D_FLAT: NoteSequence.PitchName
    A_FLAT: NoteSequence.PitchName
    E_FLAT: NoteSequence.PitchName
    B_FLAT: NoteSequence.PitchName
    F: NoteSequence.PitchName
    C: NoteSequence.PitchName
    G: NoteSequence.PitchName
    D: NoteSequence.PitchName
    A: NoteSequence.PitchName
    E: NoteSequence.PitchName
    B: NoteSequence.PitchName
    F_SHARP: NoteSequence.PitchName
    C_SHARP: NoteSequence.PitchName
    G_SHARP: NoteSequence.PitchName
    D_SHARP: NoteSequence.PitchName
    A_SHARP: NoteSequence.PitchName
    E_SHARP: NoteSequence.PitchName
    B_SHARP: NoteSequence.PitchName
    F_SHARP_SHARP: NoteSequence.PitchName
    C_SHARP_SHARP: NoteSequence.PitchName
    G_SHARP_SHARP: NoteSequence.PitchName
    D_SHARP_SHARP: NoteSequence.PitchName
    A_SHARP_SHARP: NoteSequence.PitchName
    E_SHARP_SHARP: NoteSequence.PitchName
    B_SHARP_SHARP: NoteSequence.PitchName
    class Note(_message.Message):
        __slots__ = ["pitch", "pitch_name", "velocity", "start_time", "quantized_start_step", "end_time", "quantized_end_step", "numerator", "denominator", "instrument", "program", "is_drum", "part", "voice"]
        PITCH_FIELD_NUMBER: _ClassVar[int]
        PITCH_NAME_FIELD_NUMBER: _ClassVar[int]
        VELOCITY_FIELD_NUMBER: _ClassVar[int]
        START_TIME_FIELD_NUMBER: _ClassVar[int]
        QUANTIZED_START_STEP_FIELD_NUMBER: _ClassVar[int]
        END_TIME_FIELD_NUMBER: _ClassVar[int]
        QUANTIZED_END_STEP_FIELD_NUMBER: _ClassVar[int]
        NUMERATOR_FIELD_NUMBER: _ClassVar[int]
        DENOMINATOR_FIELD_NUMBER: _ClassVar[int]
        INSTRUMENT_FIELD_NUMBER: _ClassVar[int]
        PROGRAM_FIELD_NUMBER: _ClassVar[int]
        IS_DRUM_FIELD_NUMBER: _ClassVar[int]
        PART_FIELD_NUMBER: _ClassVar[int]
        VOICE_FIELD_NUMBER: _ClassVar[int]
        pitch: int
        pitch_name: NoteSequence.PitchName
        velocity: int
        start_time: float
        quantized_start_step: int
        end_time: float
        quantized_end_step: int
        numerator: int
        denominator: int
        instrument: int
        program: int
        is_drum: bool
        part: int
        voice: int
        def __init__(self, pitch: _Optional[int] = ..., pitch_name: _Optional[_Union[NoteSequence.PitchName, str]] = ..., velocity: _Optional[int] = ..., start_time: _Optional[float] = ..., quantized_start_step: _Optional[int] = ..., end_time: _Optional[float] = ..., quantized_end_step: _Optional[int] = ..., numerator: _Optional[int] = ..., denominator: _Optional[int] = ..., instrument: _Optional[int] = ..., program: _Optional[int] = ..., is_drum: bool = ..., part: _Optional[int] = ..., voice: _Optional[int] = ...) -> None: ...
    class TimeSignature(_message.Message):
        __slots__ = ["time", "numerator", "denominator"]
        TIME_FIELD_NUMBER: _ClassVar[int]
        NUMERATOR_FIELD_NUMBER: _ClassVar[int]
        DENOMINATOR_FIELD_NUMBER: _ClassVar[int]
        time: float
        numerator: int
        denominator: int
        def __init__(self, time: _Optional[float] = ..., numerator: _Optional[int] = ..., denominator: _Optional[int] = ...) -> None: ...
    class KeySignature(_message.Message):
        __slots__ = ["time", "key", "mode"]
        class Key(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = []
            C: _ClassVar[NoteSequence.KeySignature.Key]
            C_SHARP: _ClassVar[NoteSequence.KeySignature.Key]
            D_FLAT: _ClassVar[NoteSequence.KeySignature.Key]
            D: _ClassVar[NoteSequence.KeySignature.Key]
            D_SHARP: _ClassVar[NoteSequence.KeySignature.Key]
            E_FLAT: _ClassVar[NoteSequence.KeySignature.Key]
            E: _ClassVar[NoteSequence.KeySignature.Key]
            F: _ClassVar[NoteSequence.KeySignature.Key]
            F_SHARP: _ClassVar[NoteSequence.KeySignature.Key]
            G_FLAT: _ClassVar[NoteSequence.KeySignature.Key]
            G: _ClassVar[NoteSequence.KeySignature.Key]
            G_SHARP: _ClassVar[NoteSequence.KeySignature.Key]
            A_FLAT: _ClassVar[NoteSequence.KeySignature.Key]
            A: _ClassVar[NoteSequence.KeySignature.Key]
            A_SHARP: _ClassVar[NoteSequence.KeySignature.Key]
            B_FLAT: _ClassVar[NoteSequence.KeySignature.Key]
            B: _ClassVar[NoteSequence.KeySignature.Key]
        C: NoteSequence.KeySignature.Key
        C_SHARP: NoteSequence.KeySignature.Key
        D_FLAT: NoteSequence.KeySignature.Key
        D: NoteSequence.KeySignature.Key
        D_SHARP: NoteSequence.KeySignature.Key
        E_FLAT: NoteSequence.KeySignature.Key
        E: NoteSequence.KeySignature.Key
        F: NoteSequence.KeySignature.Key
        F_SHARP: NoteSequence.KeySignature.Key
        G_FLAT: NoteSequence.KeySignature.Key
        G: NoteSequence.KeySignature.Key
        G_SHARP: NoteSequence.KeySignature.Key
        A_FLAT: NoteSequence.KeySignature.Key
        A: NoteSequence.KeySignature.Key
        A_SHARP: NoteSequence.KeySignature.Key
        B_FLAT: NoteSequence.KeySignature.Key
        B: NoteSequence.KeySignature.Key
        class Mode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = []
            MAJOR: _ClassVar[NoteSequence.KeySignature.Mode]
            MINOR: _ClassVar[NoteSequence.KeySignature.Mode]
            NOT_SPECIFIED: _ClassVar[NoteSequence.KeySignature.Mode]
            MIXOLYDIAN: _ClassVar[NoteSequence.KeySignature.Mode]
            DORIAN: _ClassVar[NoteSequence.KeySignature.Mode]
            PHRYGIAN: _ClassVar[NoteSequence.KeySignature.Mode]
            LYDIAN: _ClassVar[NoteSequence.KeySignature.Mode]
            LOCRIAN: _ClassVar[NoteSequence.KeySignature.Mode]
        MAJOR: NoteSequence.KeySignature.Mode
        MINOR: NoteSequence.KeySignature.Mode
        NOT_SPECIFIED: NoteSequence.KeySignature.Mode
        MIXOLYDIAN: NoteSequence.KeySignature.Mode
        DORIAN: NoteSequence.KeySignature.Mode
        PHRYGIAN: NoteSequence.KeySignature.Mode
        LYDIAN: NoteSequence.KeySignature.Mode
        LOCRIAN: NoteSequence.KeySignature.Mode
        TIME_FIELD_NUMBER: _ClassVar[int]
        KEY_FIELD_NUMBER: _ClassVar[int]
        MODE_FIELD_NUMBER: _ClassVar[int]
        time: float
        key: NoteSequence.KeySignature.Key
        mode: NoteSequence.KeySignature.Mode
        def __init__(self, time: _Optional[float] = ..., key: _Optional[_Union[NoteSequence.KeySignature.Key, str]] = ..., mode: _Optional[_Union[NoteSequence.KeySignature.Mode, str]] = ...) -> None: ...
    class Tempo(_message.Message):
        __slots__ = ["time", "qpm"]
        TIME_FIELD_NUMBER: _ClassVar[int]
        QPM_FIELD_NUMBER: _ClassVar[int]
        time: float
        qpm: float
        def __init__(self, time: _Optional[float] = ..., qpm: _Optional[float] = ...) -> None: ...
    class PitchBend(_message.Message):
        __slots__ = ["time", "bend", "instrument", "program", "is_drum"]
        TIME_FIELD_NUMBER: _ClassVar[int]
        BEND_FIELD_NUMBER: _ClassVar[int]
        INSTRUMENT_FIELD_NUMBER: _ClassVar[int]
        PROGRAM_FIELD_NUMBER: _ClassVar[int]
        IS_DRUM_FIELD_NUMBER: _ClassVar[int]
        time: float
        bend: int
        instrument: int
        program: int
        is_drum: bool
        def __init__(self, time: _Optional[float] = ..., bend: _Optional[int] = ..., instrument: _Optional[int] = ..., program: _Optional[int] = ..., is_drum: bool = ...) -> None: ...
    class ControlChange(_message.Message):
        __slots__ = ["time", "quantized_step", "control_number", "control_value", "instrument", "program", "is_drum"]
        TIME_FIELD_NUMBER: _ClassVar[int]
        QUANTIZED_STEP_FIELD_NUMBER: _ClassVar[int]
        CONTROL_NUMBER_FIELD_NUMBER: _ClassVar[int]
        CONTROL_VALUE_FIELD_NUMBER: _ClassVar[int]
        INSTRUMENT_FIELD_NUMBER: _ClassVar[int]
        PROGRAM_FIELD_NUMBER: _ClassVar[int]
        IS_DRUM_FIELD_NUMBER: _ClassVar[int]
        time: float
        quantized_step: int
        control_number: int
        control_value: int
        instrument: int
        program: int
        is_drum: bool
        def __init__(self, time: _Optional[float] = ..., quantized_step: _Optional[int] = ..., control_number: _Optional[int] = ..., control_value: _Optional[int] = ..., instrument: _Optional[int] = ..., program: _Optional[int] = ..., is_drum: bool = ...) -> None: ...
    class PartInfo(_message.Message):
        __slots__ = ["part", "name"]
        PART_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        part: int
        name: str
        def __init__(self, part: _Optional[int] = ..., name: _Optional[str] = ...) -> None: ...
    class InstrumentInfo(_message.Message):
        __slots__ = ["instrument", "name"]
        INSTRUMENT_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        instrument: int
        name: str
        def __init__(self, instrument: _Optional[int] = ..., name: _Optional[str] = ...) -> None: ...
    class SourceInfo(_message.Message):
        __slots__ = ["source_type", "encoding_type", "parser"]
        class SourceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = []
            UNKNOWN_SOURCE_TYPE: _ClassVar[NoteSequence.SourceInfo.SourceType]
            SCORE_BASED: _ClassVar[NoteSequence.SourceInfo.SourceType]
            PERFORMANCE_BASED: _ClassVar[NoteSequence.SourceInfo.SourceType]
        UNKNOWN_SOURCE_TYPE: NoteSequence.SourceInfo.SourceType
        SCORE_BASED: NoteSequence.SourceInfo.SourceType
        PERFORMANCE_BASED: NoteSequence.SourceInfo.SourceType
        class EncodingType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = []
            UNKNOWN_ENCODING_TYPE: _ClassVar[NoteSequence.SourceInfo.EncodingType]
            MUSIC_XML: _ClassVar[NoteSequence.SourceInfo.EncodingType]
            ABC: _ClassVar[NoteSequence.SourceInfo.EncodingType]
            MIDI: _ClassVar[NoteSequence.SourceInfo.EncodingType]
            MUSICNET: _ClassVar[NoteSequence.SourceInfo.EncodingType]
        UNKNOWN_ENCODING_TYPE: NoteSequence.SourceInfo.EncodingType
        MUSIC_XML: NoteSequence.SourceInfo.EncodingType
        ABC: NoteSequence.SourceInfo.EncodingType
        MIDI: NoteSequence.SourceInfo.EncodingType
        MUSICNET: NoteSequence.SourceInfo.EncodingType
        class Parser(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = []
            UNKNOWN_PARSER: _ClassVar[NoteSequence.SourceInfo.Parser]
            MUSIC21: _ClassVar[NoteSequence.SourceInfo.Parser]
            PRETTY_MIDI: _ClassVar[NoteSequence.SourceInfo.Parser]
            MAGENTA_MUSIC_XML: _ClassVar[NoteSequence.SourceInfo.Parser]
            MAGENTA_MUSICNET: _ClassVar[NoteSequence.SourceInfo.Parser]
            MAGENTA_ABC: _ClassVar[NoteSequence.SourceInfo.Parser]
            TONEJS_MIDI_CONVERT: _ClassVar[NoteSequence.SourceInfo.Parser]
        UNKNOWN_PARSER: NoteSequence.SourceInfo.Parser
        MUSIC21: NoteSequence.SourceInfo.Parser
        PRETTY_MIDI: NoteSequence.SourceInfo.Parser
        MAGENTA_MUSIC_XML: NoteSequence.SourceInfo.Parser
        MAGENTA_MUSICNET: NoteSequence.SourceInfo.Parser
        MAGENTA_ABC: NoteSequence.SourceInfo.Parser
        TONEJS_MIDI_CONVERT: NoteSequence.SourceInfo.Parser
        SOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
        ENCODING_TYPE_FIELD_NUMBER: _ClassVar[int]
        PARSER_FIELD_NUMBER: _ClassVar[int]
        source_type: NoteSequence.SourceInfo.SourceType
        encoding_type: NoteSequence.SourceInfo.EncodingType
        parser: NoteSequence.SourceInfo.Parser
        def __init__(self, source_type: _Optional[_Union[NoteSequence.SourceInfo.SourceType, str]] = ..., encoding_type: _Optional[_Union[NoteSequence.SourceInfo.EncodingType, str]] = ..., parser: _Optional[_Union[NoteSequence.SourceInfo.Parser, str]] = ...) -> None: ...
    class TextAnnotation(_message.Message):
        __slots__ = ["time", "quantized_step", "text", "annotation_type"]
        class TextAnnotationType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = []
            UNKNOWN: _ClassVar[NoteSequence.TextAnnotation.TextAnnotationType]
            CHORD_SYMBOL: _ClassVar[NoteSequence.TextAnnotation.TextAnnotationType]
            BEAT: _ClassVar[NoteSequence.TextAnnotation.TextAnnotationType]
        UNKNOWN: NoteSequence.TextAnnotation.TextAnnotationType
        CHORD_SYMBOL: NoteSequence.TextAnnotation.TextAnnotationType
        BEAT: NoteSequence.TextAnnotation.TextAnnotationType
        TIME_FIELD_NUMBER: _ClassVar[int]
        QUANTIZED_STEP_FIELD_NUMBER: _ClassVar[int]
        TEXT_FIELD_NUMBER: _ClassVar[int]
        ANNOTATION_TYPE_FIELD_NUMBER: _ClassVar[int]
        time: float
        quantized_step: int
        text: str
        annotation_type: NoteSequence.TextAnnotation.TextAnnotationType
        def __init__(self, time: _Optional[float] = ..., quantized_step: _Optional[int] = ..., text: _Optional[str] = ..., annotation_type: _Optional[_Union[NoteSequence.TextAnnotation.TextAnnotationType, str]] = ...) -> None: ...
    class QuantizationInfo(_message.Message):
        __slots__ = ["steps_per_quarter", "steps_per_second"]
        STEPS_PER_QUARTER_FIELD_NUMBER: _ClassVar[int]
        STEPS_PER_SECOND_FIELD_NUMBER: _ClassVar[int]
        steps_per_quarter: int
        steps_per_second: int
        def __init__(self, steps_per_quarter: _Optional[int] = ..., steps_per_second: _Optional[int] = ...) -> None: ...
    class SubsequenceInfo(_message.Message):
        __slots__ = ["start_time_offset", "end_time_offset"]
        START_TIME_OFFSET_FIELD_NUMBER: _ClassVar[int]
        END_TIME_OFFSET_FIELD_NUMBER: _ClassVar[int]
        start_time_offset: float
        end_time_offset: float
        def __init__(self, start_time_offset: _Optional[float] = ..., end_time_offset: _Optional[float] = ...) -> None: ...
    class SectionAnnotation(_message.Message):
        __slots__ = ["time", "section_id"]
        TIME_FIELD_NUMBER: _ClassVar[int]
        SECTION_ID_FIELD_NUMBER: _ClassVar[int]
        time: float
        section_id: int
        def __init__(self, time: _Optional[float] = ..., section_id: _Optional[int] = ...) -> None: ...
    class Section(_message.Message):
        __slots__ = ["section_id", "section_group"]
        SECTION_ID_FIELD_NUMBER: _ClassVar[int]
        SECTION_GROUP_FIELD_NUMBER: _ClassVar[int]
        section_id: int
        section_group: NoteSequence.SectionGroup
        def __init__(self, section_id: _Optional[int] = ..., section_group: _Optional[_Union[NoteSequence.SectionGroup, _Mapping]] = ...) -> None: ...
    class SectionGroup(_message.Message):
        __slots__ = ["sections", "num_times"]
        SECTIONS_FIELD_NUMBER: _ClassVar[int]
        NUM_TIMES_FIELD_NUMBER: _ClassVar[int]
        sections: _containers.RepeatedCompositeFieldContainer[NoteSequence.Section]
        num_times: int
        def __init__(self, sections: _Optional[_Iterable[_Union[NoteSequence.Section, _Mapping]]] = ..., num_times: _Optional[int] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    COLLECTION_NAME_FIELD_NUMBER: _ClassVar[int]
    TICKS_PER_QUARTER_FIELD_NUMBER: _ClassVar[int]
    TIME_SIGNATURES_FIELD_NUMBER: _ClassVar[int]
    KEY_SIGNATURES_FIELD_NUMBER: _ClassVar[int]
    TEMPOS_FIELD_NUMBER: _ClassVar[int]
    NOTES_FIELD_NUMBER: _ClassVar[int]
    TOTAL_TIME_FIELD_NUMBER: _ClassVar[int]
    TOTAL_QUANTIZED_STEPS_FIELD_NUMBER: _ClassVar[int]
    PITCH_BENDS_FIELD_NUMBER: _ClassVar[int]
    CONTROL_CHANGES_FIELD_NUMBER: _ClassVar[int]
    PART_INFOS_FIELD_NUMBER: _ClassVar[int]
    SOURCE_INFO_FIELD_NUMBER: _ClassVar[int]
    TEXT_ANNOTATIONS_FIELD_NUMBER: _ClassVar[int]
    SECTION_ANNOTATIONS_FIELD_NUMBER: _ClassVar[int]
    SECTION_GROUPS_FIELD_NUMBER: _ClassVar[int]
    QUANTIZATION_INFO_FIELD_NUMBER: _ClassVar[int]
    SUBSEQUENCE_INFO_FIELD_NUMBER: _ClassVar[int]
    SEQUENCE_METADATA_FIELD_NUMBER: _ClassVar[int]
    INSTRUMENT_INFOS_FIELD_NUMBER: _ClassVar[int]
    FINGERING_FIELD_NUMBER: _ClassVar[int]
    id: str
    filename: str
    reference_number: int
    collection_name: str
    ticks_per_quarter: int
    time_signatures: _containers.RepeatedCompositeFieldContainer[NoteSequence.TimeSignature]
    key_signatures: _containers.RepeatedCompositeFieldContainer[NoteSequence.KeySignature]
    tempos: _containers.RepeatedCompositeFieldContainer[NoteSequence.Tempo]
    notes: _containers.RepeatedCompositeFieldContainer[NoteSequence.Note]
    total_time: float
    total_quantized_steps: int
    pitch_bends: _containers.RepeatedCompositeFieldContainer[NoteSequence.PitchBend]
    control_changes: _containers.RepeatedCompositeFieldContainer[NoteSequence.ControlChange]
    part_infos: _containers.RepeatedCompositeFieldContainer[NoteSequence.PartInfo]
    source_info: NoteSequence.SourceInfo
    text_annotations: _containers.RepeatedCompositeFieldContainer[NoteSequence.TextAnnotation]
    section_annotations: _containers.RepeatedCompositeFieldContainer[NoteSequence.SectionAnnotation]
    section_groups: _containers.RepeatedCompositeFieldContainer[NoteSequence.SectionGroup]
    quantization_info: NoteSequence.QuantizationInfo
    subsequence_info: NoteSequence.SubsequenceInfo
    sequence_metadata: SequenceMetadata
    instrument_infos: _containers.RepeatedCompositeFieldContainer[NoteSequence.InstrumentInfo]
    fingering: int
    def __init__(self, id: _Optional[str] = ..., filename: _Optional[str] = ..., reference_number: _Optional[int] = ..., collection_name: _Optional[str] = ..., ticks_per_quarter: _Optional[int] = ..., time_signatures: _Optional[_Iterable[_Union[NoteSequence.TimeSignature, _Mapping]]] = ..., key_signatures: _Optional[_Iterable[_Union[NoteSequence.KeySignature, _Mapping]]] = ..., tempos: _Optional[_Iterable[_Union[NoteSequence.Tempo, _Mapping]]] = ..., notes: _Optional[_Iterable[_Union[NoteSequence.Note, _Mapping]]] = ..., total_time: _Optional[float] = ..., total_quantized_steps: _Optional[int] = ..., pitch_bends: _Optional[_Iterable[_Union[NoteSequence.PitchBend, _Mapping]]] = ..., control_changes: _Optional[_Iterable[_Union[NoteSequence.ControlChange, _Mapping]]] = ..., part_infos: _Optional[_Iterable[_Union[NoteSequence.PartInfo, _Mapping]]] = ..., source_info: _Optional[_Union[NoteSequence.SourceInfo, _Mapping]] = ..., text_annotations: _Optional[_Iterable[_Union[NoteSequence.TextAnnotation, _Mapping]]] = ..., section_annotations: _Optional[_Iterable[_Union[NoteSequence.SectionAnnotation, _Mapping]]] = ..., section_groups: _Optional[_Iterable[_Union[NoteSequence.SectionGroup, _Mapping]]] = ..., quantization_info: _Optional[_Union[NoteSequence.QuantizationInfo, _Mapping]] = ..., subsequence_info: _Optional[_Union[NoteSequence.SubsequenceInfo, _Mapping]] = ..., sequence_metadata: _Optional[_Union[SequenceMetadata, _Mapping]] = ..., instrument_infos: _Optional[_Iterable[_Union[NoteSequence.InstrumentInfo, _Mapping]]] = ..., fingering: _Optional[int] = ...) -> None: ...

class SequenceMetadata(_message.Message):
    __slots__ = ["title", "artist", "genre", "composers"]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    ARTIST_FIELD_NUMBER: _ClassVar[int]
    GENRE_FIELD_NUMBER: _ClassVar[int]
    COMPOSERS_FIELD_NUMBER: _ClassVar[int]
    title: str
    artist: str
    genre: _containers.RepeatedScalarFieldContainer[str]
    composers: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, title: _Optional[str] = ..., artist: _Optional[str] = ..., genre: _Optional[_Iterable[str]] = ..., composers: _Optional[_Iterable[str]] = ...) -> None: ...

class VelocityRange(_message.Message):
    __slots__ = ["min", "max"]
    MIN_FIELD_NUMBER: _ClassVar[int]
    MAX_FIELD_NUMBER: _ClassVar[int]
    min: int
    max: int
    def __init__(self, min: _Optional[int] = ..., max: _Optional[int] = ...) -> None: ...
