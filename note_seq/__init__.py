# Copyright 2020 The Magenta Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Imports classes and utils into the top-level namespace."""

from note_seq.abc_parser import parse_abc_tunebook
from note_seq.abc_parser import parse_abc_tunebook_file

from note_seq.chord_inference import ChordInferenceError
from note_seq.chord_inference import infer_chords_for_sequence

from note_seq.chord_symbols_lib import chord_symbol_bass
from note_seq.chord_symbols_lib import chord_symbol_pitches
from note_seq.chord_symbols_lib import chord_symbol_quality
from note_seq.chord_symbols_lib import chord_symbol_root
from note_seq.chord_symbols_lib import ChordSymbolError
from note_seq.chord_symbols_lib import pitches_to_chord_symbol
from note_seq.chord_symbols_lib import transpose_chord_symbol

from note_seq.chords_encoder_decoder import ChordEncodingError
from note_seq.chords_encoder_decoder import MajorMinorChordOneHotEncoding
from note_seq.chords_encoder_decoder import PitchChordsEncoderDecoder
from note_seq.chords_encoder_decoder import TriadChordOneHotEncoding

from note_seq.chords_lib import BasicChordRenderer
from note_seq.chords_lib import ChordProgression

from note_seq.constants import *  # pylint: disable=wildcard-import

from note_seq.drums_encoder_decoder import MultiDrumOneHotEncoding

from note_seq.drums_lib import DrumTrack
from note_seq.drums_lib import midi_file_to_drum_track

from note_seq.encoder_decoder import ConditionalEventSequenceEncoderDecoder
from note_seq.encoder_decoder import EventSequenceEncoderDecoder
from note_seq.encoder_decoder import LookbackEventSequenceEncoderDecoder
from note_seq.encoder_decoder import MultipleEventSequenceEncoder
from note_seq.encoder_decoder import OneHotEncoding
from note_seq.encoder_decoder import OneHotEventSequenceEncoderDecoder
from note_seq.encoder_decoder import OneHotIndexEventSequenceEncoderDecoder
from note_seq.encoder_decoder import OptionalEventSequenceEncoder

from note_seq.events_lib import NonIntegerStepsPerBarError

from note_seq.lead_sheets_lib import LeadSheet

from note_seq.melodies_lib import BadNoteError
from note_seq.melodies_lib import Melody
from note_seq.melodies_lib import midi_file_to_melody
from note_seq.melodies_lib import PolyphonicMelodyError

from note_seq.melody_encoder_decoder import KeyMelodyEncoderDecoder
from note_seq.melody_encoder_decoder import MelodyOneHotEncoding

from note_seq.melody_inference import infer_melody_for_sequence
from note_seq.melody_inference import MelodyInferenceError

from note_seq.midi_io import midi_file_to_note_sequence
from note_seq.midi_io import midi_file_to_sequence_proto
from note_seq.midi_io import midi_to_note_sequence
from note_seq.midi_io import midi_to_sequence_proto
from note_seq.midi_io import MIDIConversionError
from note_seq.midi_io import sequence_proto_to_midi_file
from note_seq.midi_io import sequence_proto_to_pretty_midi

from note_seq.midi_synth import fluidsynth
from note_seq.midi_synth import synthesize

from note_seq.musicxml_parser import MusicXMLDocument
from note_seq.musicxml_parser import MusicXMLParseError

from note_seq.musicxml_reader import musicxml_file_to_sequence_proto
from note_seq.musicxml_reader import musicxml_to_sequence_proto
from note_seq.musicxml_reader import MusicXMLConversionError

from note_seq.notebook_utils import play_sequence
from note_seq.notebook_utils import plot_sequence

from note_seq.performance_controls import all_performance_control_signals
from note_seq.performance_controls import NoteDensityPerformanceControlSignal
from note_seq.performance_controls import PitchHistogramPerformanceControlSignal

from note_seq.performance_encoder_decoder import ModuloPerformanceEventSequenceEncoderDecoder
from note_seq.performance_encoder_decoder import NotePerformanceEventSequenceEncoderDecoder
from note_seq.performance_encoder_decoder import PerformanceModuloEncoding
from note_seq.performance_encoder_decoder import PerformanceOneHotEncoding

from note_seq.performance_lib import MetricPerformance
from note_seq.performance_lib import Performance
from note_seq.performance_lib import PerformanceEvent

from note_seq.pianoroll_encoder_decoder import PianorollEncoderDecoder

from note_seq.pianoroll_lib import PianorollSequence

from note_seq.protobuf import music_pb2
from note_seq.protobuf.music_pb2 import NoteSequence  # pylint:disable=g-importing-member

from note_seq.sequences_lib import apply_sustain_control_changes
from note_seq.sequences_lib import BadTimeSignatureError
from note_seq.sequences_lib import concatenate_sequences
from note_seq.sequences_lib import extract_subsequence
from note_seq.sequences_lib import infer_dense_chords_for_sequence
from note_seq.sequences_lib import MultipleTempoError
from note_seq.sequences_lib import MultipleTimeSignatureError
from note_seq.sequences_lib import NegativeTimeError
from note_seq.sequences_lib import quantize_note_sequence
from note_seq.sequences_lib import quantize_note_sequence_absolute
from note_seq.sequences_lib import quantize_to_step
from note_seq.sequences_lib import sequence_to_pianoroll
from note_seq.sequences_lib import split_note_sequence
from note_seq.sequences_lib import steps_per_bar_in_quantized_sequence
from note_seq.sequences_lib import steps_per_quarter_to_steps_per_second
from note_seq.sequences_lib import trim_note_sequence

