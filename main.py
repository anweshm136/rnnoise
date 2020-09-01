import subprocess
import os
from scipy.io import wavfile    
import numpy as np
import time
import csv

ip_path="input/"
wav_path="wav/"
#os.mkdir(wav_path)
ipraw_path="input_raw/"
#os.mkdir(ipraw_path)
opraw_path="output_raw/"
#os.mkdir(opraw_path)
op_path="output/"

exec_time=[]
exec_time.append(["File Number", "MP3 to WAV", "WAV to RAW", "RNNoise", "RAW to Output WAV"])

for filename in os.listdir(ip_path):
    t0=time.time()
    f1=os.path.splitext(filename)[0]
    f2=os.path.splitext(filename)[1]
    t1=time.time()
    subprocess.call(["ffmpeg","-i",ip_path+filename,wav_path+f1+".wav"])
    t2=time.time()
    fs, data=wavfile.read(wav_path+f1+".wav")
    if data.ndim==2:
        sound=data.mean(axis=1)
        sound=np.asarray(sound,dtype=np.int16)
        wavfile.write(wav_path+f1+".wav",fs,sound)
    t3=time.time()
    subprocess.call(["ffmpeg","-i",wav_path+f1+".wav","-f","s16le","-acodec","pcm_s16le",ipraw_path+f1+".raw"])
    t4=time.time()
    subprocess.call(["./examples/rnnoise_demo", ipraw_path+f1+".raw", opraw_path+f1+".raw"])
    t5=time.time()
    subprocess.call(["sox","-r",str(fs),"-e","signed","-b","16","-c","1",opraw_path+f1+".raw",op_path+f1+".wav"])
    t6=time.time()
    exec_time.append([filename,t2-t1,t4-t3,t5-t4,t6-t5])
    #print(exec_time)

with open("execution_time.csv","w", newline="") as f:
    writer=csv.writer(f)
    writer.writerows(exec_time)
