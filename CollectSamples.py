from utils import *
from os.path import join
from multiprocessing import Pool
import numpy as np
data_root = 'data/'
sr = 44100
max_length = sr*4 # ignore samples longer than 4 seconds
fixed_length = sr/4 # trim all samples to 250 milliseconds
limit = None # set this to 100 to only load the first 100 samples
files = list(list_all_files(join(data_root, 'samples'), ['.wav']))
len(files)
def load_sample(fn, sr=None,
                max_length=None, fixed_length=None, normalize=True):
    if fn == '': # ignore empty filenames
        return None
    audio, _ = ffmpeg_load_audio(fn, sr, mono=True)
    duration = len(audio)
    if duration == 0: # ignore zero-length samples
        return None
    if max_length and duration >= max_length: # ignore long samples
        return None
    if fixed_length:
        audio.resize(fixed_length)
    max_val = np.abs(audio).max()
    if max_val == 0: # ignore completely silent sounds
        return None
    if normalize:
        audio /= max_val
    return (fn, audio, duration)
def job(fn):
    return load_sample(fn, sr=sr,
                       max_length=max_length, fixed_length=fixed_length)
pool = Pool()
results = pool.map(job, files[:limit])
print 'Processed', len(results), 'samples'
valid = filter(None, results)
filenames = [x[0] for x in valid]
samples = [x[1] for x in valid]
durations = [x[2] for x in valid]
samples = np.asarray(samples)
np.savetxt(join(data_root, 'filenames.txt'), filenames, fmt='%s')
np.savetxt(join(data_root, 'durations.txt'), durations, fmt='%i')
np.save(join(data_root, 'samples.npy'), samples)
print 'Saved', len(valid), 'samples'

