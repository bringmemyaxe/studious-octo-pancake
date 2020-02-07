data_root = 'data/'
sr = 44100
max_length = sr*32 # ignore samples longer than 32 seconds
fixed_length = sr*32 # trim all samples to 32000 milliseconds
limit = None # set this to 100 to only load the first 100 samples
