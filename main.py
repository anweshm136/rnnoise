import subprocess
import os
from pydub import AudioSegment
from scipy.io import wavfile    
import numpy as np

ip_path="input/"
wav_path="wav/"
os.mkdir(wav_path)
ipraw_path="input_raw/"
os.mkdir(ipraw_path)
opraw_path="output_raw/"
os.mkdir(opraw_path)
op_path="output/"

for filename in os.listdir(ip_path):
    f1=os.path.splitext(filename)[0]
    f2=os.path.splitext(filename)[1]
    subprocess.call(["ffmpeg","-i",ip_path+filename,wav_path+f1+".wav"])
    fs, data=wavfile.read(wav_path+f1+".wav")
    if data.ndim==2:
        sound=data.mean(axis=1)
        sound=np.asarray(sound,dtype=np.int16)
        wavfile.write(wav_path+f1+".wav",fs,sound)

    subprocess.call(["ffmpeg","-i",wav_path+f1+".wav","-f","s16le","-acodec","pcm_s16le",ipraw_path+f1+".raw"])
    subprocess.call(["./examples/rnnoise_demo", ipraw_path+f1+".raw", opraw_path+f1+".raw"])
    subprocess.call(["sox","-r",str(fs),"-e","signed","-b","16","-c","1",opraw_path+f1+".raw",op_path+f1+".wav"])
