# Copyright 2016 Google Inc.
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#     http://www.apache.org/licenses/LICENSE-2.0
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import os
import librosa
import numpy
ref_sounds = []
for root, dirs, files in os.walk("./ref_sounds", topdown = False):
    for name in files:
        ref_sounds.append(os.path.join(root, name))
for ref_sound in ref_sounds:
    sample_rate = 44100


    def scale(arr):
        # get the average
        avg = numpy.average(arr)
        # scale from 20,20000 to 0,1
        return (avg - 20) / (20000 - 20)


    def analyse(file):
        y, sr = librosa.load(file, sr=sample_rate, duration=0.25)
        centroid = scale(librosa.feature.spectral_centroid(y=y, sr=sr))
        bandwidth = scale(librosa.feature.spectral_bandwidth(y=y, sr=sr))
        # rolloff = scale(librosa.feature.spectral_rolloff(y=y, sr=sr))
        # contrast = scale(librosa.feature.spectral_contrast(y=y, sr=sr))
        return numpy.asarray([centroid, bandwidth])


    kick_values = analyse(ref_sound)
    closest = 1

    def get_distance(test_values):
        global closest
        global best_option
        test_values = numpy.asarray(test_values)
        kick_dist = numpy.linalg.norm(test_values - kick_values)
        prepared_file_name, useless_extension = os.path.splitext(os.path.basename(sample_file_name))
        if kick_dist < closest:
            closest = kick_dist
            best_option = prepared_file_name
        return [kick_dist]


    # print get_distance(snare_values)

    def process(file_name):
        global sample_file_name
        sample_file_name = file_name
        return get_distance(analyse(file_name))


    with open("./data/filenames.txt") as file_names:
        files = file_names.read().splitlines()
        for something in files:
            process(something)
    print(best_option, 'is the closest sample for', ref_sound)
    print('The difference is:', closest)
