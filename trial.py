import subprocess
import os

ip_path="input_raw/"
op_path="output_raw/"

for filename in os.listdir(ip_path):
    filename=os.path.splitext(filename)[0]
    #print(filename)
    subprocess.call(["./examples/rnnoise_demo", ip_path+filename+".raw", op_path+filename+"_proc.raw"])

ip_path="output_raw/"
op_path="output/"

for filename in os.listdir(ip_path):
    filename=os.path.splitext(filename)[0]
    #print(filename)
    subprocess.call(["sox","-r","44100","-e","signed","-b","16","-c","1",ip_path+filename+".raw",op_path+filename+".wav"])