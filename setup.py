# Copyright 2022 The Magenta Authors.
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

"""A setuptools based setup module for note-seq."""

from setuptools import find_packages
from setuptools import setup

with open('note_seq/version.py') as in_file:
  exec(in_file.read())  # pylint: disable=exec-used

REQUIRED_PACKAGES = [
    'absl-py',
    'attrs',
    'bokeh >= 0.12.0',
    'intervaltree >= 2.1.0',
    'IPython == 8.12.0',
    'librosa >= 0.6.2',
    'numpy',
    'pandas >= 0.18.1',
    'pretty_midi >= 0.2.6',
    'protobuf >= 4.21.2',
    'pydub',
    'scipy >= 0.18.1',
]

setup(
    name='note-seq',
    version=__version__,  # pylint: disable=undefined-variable
    description='Use machine learning to create art and music',
    long_description='',
    url='https://magenta.tensorflow.org/',
    author='Google Inc.',
    author_email='magenta-discuss@gmail.com',
    license='Apache 2',
    # PyPI package information.
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3',
        'Topic :: Scientific/Engineering :: Mathematics',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Libraries',
    ],
    keywords='note_seq note sequences',
    packages=find_packages(),
    package_data={'note_seq': ['*.pyi', '**/*.pyi']},
    install_requires=REQUIRED_PACKAGES,
    setup_requires=['pytest-runner', 'pytest-pylint'],
    tests_require=[
        'pytest >= 5.2.0',
        'pytest-xdist < 1.30.0',  # 1.30 has problems working with pylint plugin
        'pylint >= 2.4.2',
    ],
)
