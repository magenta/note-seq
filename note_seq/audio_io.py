# Copyright 2021 The Magenta Authors.
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

"""Audio file helper functions."""

import io
import math
import tempfile

import librosa
import numpy as np
import pydub
import scipy.io.wavfile


class AudioIOError(BaseException):  # pylint:disable=g-bad-exception-name
  pass


class AudioIOReadError(AudioIOError):
  pass


class AudioIODataTypeError(AudioIOError):
  pass


def int16_samples_to_float32(y):
  """Convert int16 numpy array of audio samples to float32."""
  if y.dtype != np.int16:
    raise ValueError('input samples not int16')
  return y.astype(np.float32) / np.iinfo(np.int16).max


def float_samples_to_int16(y):
  """Convert floating-point numpy array of audio samples to int16."""
  if not issubclass(y.dtype.type, np.floating):
    raise ValueError('input samples not floating-point')
  return (y * np.iinfo(np.int16).max).astype(np.int16)


def wav_data_to_samples_pydub(wav_data: bytes,
                              sample_rate: int,
                              remove_dc_bias: bool = False,
                              num_channels: int = None,
                              normalize_db: float = None):
  """Convert audio file data (in bytes) into a numpy array using Pydub.

  Args:
    wav_data: A byte stream of audio data.
    sample_rate: Resample recorded audio to this sample rate.
    remove_dc_bias: If true, will remove DC bias from audio.
    num_channels: If not specified, output shape will be based on the contents
      of wav_data. Otherwise, will force to be 1 or 2 channels.
    normalize_db: Normalize the audio to this many decibels. Set to None to skip
      normalization step.

  Returns:
    An array of the recorded audio at sample_rate. If mono, will be shape
    [samples], otherwise [channels, samples].
  """
  # Parse and normalize the audio.
  aseg = pydub.AudioSegment.from_file(io.BytesIO(wav_data))
  if num_channels:
    aseg = aseg.set_channels(num_channels)
  if remove_dc_bias:
    aseg = aseg.remove_dc_offset()
  if normalize_db is not None:
    aseg.normalize(headroom=normalize_db)
  aseg = aseg.set_frame_rate(sample_rate)

  # Convert to numpy array.
  channel_asegs = aseg.split_to_mono()
  samples = [s.get_array_of_samples() for s in channel_asegs]
  fp_arr = np.array(samples).astype(np.float32)
  fp_arr /= np.iinfo(samples[0].typecode).max

  # If only 1 channel, remove extra dim.
  if fp_arr.shape[0] == 1:
    fp_arr = fp_arr[0]

  return fp_arr


def wav_data_to_samples(wav_data, sample_rate):
  """Read PCM-formatted WAV data and return a NumPy array of samples.

  Uses scipy to read and librosa to process WAV data. Audio will be converted to
  mono if necessary.

  Args:
    wav_data: WAV audio data to read.
    sample_rate: The number of samples per second at which the audio will be
        returned. Resampling will be performed if necessary.

  Returns:
    A numpy array of audio samples, single-channel (mono) and sampled at the
    specified rate, in float32 format.

  Raises:
    AudioIOReadError: If scipy is unable to read the WAV data.
    AudioIOError: If audio processing fails.
  """
  try:
    # Read the wav file, converting sample rate & number of channels.
    native_sr, y = scipy.io.wavfile.read(io.BytesIO(wav_data))
  except Exception as e:  # pylint: disable=broad-except
    raise AudioIOReadError(e)

  if y.dtype == np.int16:
    # Convert to float32.
    y = int16_samples_to_float32(y)
  elif y.dtype == np.float32:
    # Already float32.
    pass
  else:
    raise AudioIOError(
        'WAV file not 16-bit or 32-bit float PCM, unsupported')
  try:
    # Convert to mono and the desired sample rate.
    if y.ndim == 2 and y.shape[1] == 2:
      y = y.T
      y = librosa.to_mono(y)
    if native_sr != sample_rate:
      y = librosa.resample(y, native_sr, sample_rate)
  except Exception as e:  # pylint: disable=broad-except
    raise AudioIOError(e)
  return y


def wav_data_to_samples_librosa(audio_file, sample_rate):
  """Loads an in-memory audio file with librosa.

  Use this instead of wav_data_to_samples if the wav is 24-bit, as that's
  incompatible with wav_data_to_samples internal scipy call.

  Will copy to a local temp file before loading so that librosa can read a file
  path. Librosa does not currently read in-memory files.

  It will be treated as a .wav file.

  Args:
    audio_file: Wav file to load.
    sample_rate: The number of samples per second at which the audio will be
        returned. Resampling will be performed if necessary.

  Returns:
    A numpy array of audio samples, single-channel (mono) and sampled at the
    specified rate, in float32 format.

  Raises:
    AudioIOReadException: If librosa is unable to load the audio data.
  """
  with tempfile.NamedTemporaryFile(suffix='.wav') as wav_input_file:
    wav_input_file.write(audio_file)
    # Before copying the file, flush any contents
    wav_input_file.flush()
    # And back the file position to top (not need for Copy but for certainty)
    wav_input_file.seek(0)
    return load_audio(wav_input_file.name, sample_rate)


def samples_to_wav_data(samples, sample_rate):
  """Converts floating point samples to wav data."""
  wav_io = io.BytesIO()
  scipy.io.wavfile.write(wav_io, sample_rate, float_samples_to_int16(samples))
  return wav_io.getvalue()


def crop_samples(samples, sample_rate, crop_beginning_seconds,
                 total_length_seconds):
  """Crop WAV data.

  Args:
    samples: Numpy Array containing samples.
    sample_rate: The sample rate at which to interpret the samples.
    crop_beginning_seconds: How many seconds to crop from the beginning of the
        audio.
    total_length_seconds: The desired duration of the audio. After cropping the
        beginning of the audio, any audio longer than this value will be
        deleted.

  Returns:
    A cropped version of the samples.
  """
  samples_to_crop = int(crop_beginning_seconds * sample_rate)
  total_samples = int(total_length_seconds * sample_rate)
  cropped_samples = samples[samples_to_crop:(samples_to_crop + total_samples)]
  return cropped_samples


def repeat_samples_to_duration(samples, sample_rate, duration):
  """Repeat a sequence of samples until it is a given duration, trimming extra.

  Args:
    samples: The sequence to repeat
    sample_rate: The sample rate at which to interpret the samples.
    duration: The desired duration

  Returns:
    The repeated and possibly trimmed sequence.
  """
  sequence_duration = len(samples) / sample_rate
  num_repeats = int(math.ceil(duration / sequence_duration))
  repeated_samples = np.concatenate([samples] * num_repeats)
  trimmed = crop_samples(
      repeated_samples, sample_rate,
      crop_beginning_seconds=0, total_length_seconds=duration)
  return trimmed


def crop_wav_data(wav_data, sample_rate, crop_beginning_seconds,
                  total_length_seconds):
  """Crop WAV data.

  Args:
    wav_data: WAV audio data to crop.
    sample_rate: The sample rate at which to read the WAV data.
    crop_beginning_seconds: How many seconds to crop from the beginning of the
        audio.
    total_length_seconds: The desired duration of the audio. After cropping the
        beginning of the audio, any audio longer than this value will be
        deleted.

  Returns:
    A cropped version of the WAV audio.
  """
  y = wav_data_to_samples(wav_data, sample_rate=sample_rate)
  samples_to_crop = int(crop_beginning_seconds * sample_rate)
  total_samples = int(total_length_seconds * sample_rate)
  cropped_samples = y[samples_to_crop:(samples_to_crop + total_samples)]
  return samples_to_wav_data(cropped_samples, sample_rate)


def jitter_wav_data(wav_data, sample_rate, jitter_seconds):
  """Add silence to the beginning of the file.

  Args:
     wav_data: WAV audio data to prepend with silence.
     sample_rate: The sample rate at which to read the WAV data.
     jitter_seconds: Seconds of silence to prepend.

  Returns:
     A version of the WAV audio with jitter_seconds silence prepended.
  """

  y = wav_data_to_samples(wav_data, sample_rate=sample_rate)
  silence_samples = jitter_seconds * sample_rate
  new_y = np.concatenate((np.zeros(np.int(silence_samples)), y))
  return samples_to_wav_data(new_y, sample_rate)


def load_audio(audio_filename, sample_rate):
  """Loads an audio file.

  Args:
    audio_filename: File path to load.
    sample_rate: The number of samples per second at which the audio will be
        returned. Resampling will be performed if necessary.

  Returns:
    A numpy array of audio samples, single-channel (mono) and sampled at the
    specified rate, in float32 format.

  Raises:
    AudioIOReadError: If librosa is unable to load the audio data.
  """
  try:
    y, unused_sr = librosa.load(audio_filename, sr=sample_rate, mono=True)
  except Exception as e:  # pylint: disable=broad-except
    raise AudioIOReadError(e)
  return y


def make_stereo(left, right):
  """Combine two mono signals into one stereo signal.

  Both signals must have the same data type. The resulting track will be the
  length of the longer of the two signals.

  Args:
    left: Samples for the left channel.
    right: Samples for the right channel.

  Returns:
    The two channels combined into a stereo signal.

  Raises:
    AudioIODataTypeError: if the two signals have different data types.
  """
  if left.dtype != right.dtype:
    raise AudioIODataTypeError(
        'left channel is of type {}, but right channel is {}'.format(
            left.dtype, right.dtype))

  # Mask of valid places in each row
  lens = np.array([len(left), len(right)])
  mask = np.arange(lens.max()) < lens[:, None]

  # Setup output array and put elements from data into masked positions
  out = np.zeros(mask.shape, dtype=left.dtype)
  out[mask] = np.concatenate([left, right])
  return out.T


def normalize_wav_data(wav_data, sample_rate, norm=np.inf):
  """Normalizes wav data.

  Args:
     wav_data: WAV audio data to prepend with silence.
     sample_rate: The sample rate at which to read the WAV data.
     norm: See the norm argument of librosa.util.normalize.

  Returns:
     A version of the WAV audio that has been normalized.
  """

  y = wav_data_to_samples(wav_data, sample_rate=sample_rate)
  new_y = librosa.util.normalize(y, norm=norm)
  return samples_to_wav_data(new_y, sample_rate)
