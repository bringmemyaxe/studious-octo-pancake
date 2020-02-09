Inspired by and based on https://github.com/googlecreativelab/aiexperiments-drum-machine

Sources:

The following files were edited by me:

https://github.com/googlecreativelab/aiexperiments-drum-machine/blob/master/scripts/analysis.py

https://github.com/kylemcdonald/AudioNotebooks/blob/master/Collect%20Samples.ipynb

https://github.com/kylemcdonald/AudioNotebooks/blob/master/utils/__init__.py

https://github.com/kylemcdonald/AudioNotebooks/blob/master/utils/list_all_files.py

https://github.com/kylemcdonald/AudioNotebooks/blob/master/utils/ffmpeg_load_audio.py

Steps:

1. (if you don't have PIP for Python 3.x) install PIP:

`sudo apt install python3-pip`

2. (if you don't have librosa module for Python 3.x) Install librosa:

`pip3 install librosa`

3. Put your *.wav sounds replacing them with names `ref_sound1.wav` / `ref_sound2.wav` / `ref_sound3.wav` / `ref_sound4.wav` in the folder `ref_sounds`

4. (if you don't have Python 2.x) Install Python 2.x:

`sudo apt install python`

5. Put your *.wav sounds into /data/samples/

6. (if you don't have PIP for Python 2.x) install PIP:

`sudo apt install python-pip`

7. (if you don't have numpy module for Python 2.x) install numpy:

`pip install numpy`

8. (if you don't have ffmpeg package) install ffmpeg:

`sudo apt install ffmpeg`

9. Run CollectSamples.py in Python 2.x

10. Run analysis.py in Python 3.x

I'm going to make it more convenient for using with multiple ref_files 
