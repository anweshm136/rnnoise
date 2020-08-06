import subprocess
import os
from pydub import AudioSegment

ip_path="input/"
ipraw_path="input_raw/"
opraw_path="output_raw/"
op_path="output/"

for filename in os.listdir(ip_path):
    f1=os.path.splitext(filename)[0]
    f2=os.path.splitext(filename)[1]
    subprocess.call(["ffmpeg","-i",ip_path+filename,"-f","s16le","-acodec","pcm_s16le",ipraw_path+f1+".raw"])
    subprocess.call(["./examples/rnnoise_demo", ipraw_path+f1+".raw", opraw_path+f1+".raw"])
    subprocess.call(["sox","-r","44100","-e","signed","-b","16","-c","1",opraw_path+f1+".raw",op_path+f1+".wav"])
