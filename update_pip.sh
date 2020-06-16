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

#!/bin/bash
set -ex

orig_dir=$(pwd)
tmp_dir=$(mktemp -d -t note_seq-XXXX)
git clone https://github.com/magenta/note_seq.git $tmp_dir
cd $tmp_dir

python setup.py sdist
python setup.py bdist_wheel --universal
twine upload dist/*

cd $orig_dir
rm -rf $tmp_dir
