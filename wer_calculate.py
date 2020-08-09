import pandas as pd
from jiwer import wer
import numpy as np
import re 
from tqdm import tqdm
import csv

train_df = pd.read_csv('output.csv')

err1 = []
err2 = []
wer_opt = []

for i in tqdm(range(train_df.shape[0])):
    wer1 = []
    wer2 = []
    data = train_df['flipkart transcriptions 1'][i]
    data1 = train_df['output transcriptions 1'][i]
    data2 = train_df['output transcriptions 2'][i]
    res = re.split('@|_', data) 
    boy = res[0]
    for i in range(1, len(res)):
        boy = boy + res[i]
    error1 = wer(boy, data1)
    error2 = wer(boy, data2)  
    for j in range(len(res)):
        if bool(res[j])==True:
            if res[j]!=' ':
                if res[j]!='  ':
                    if res[j]!='   ':
                        error11 = wer(res[j], data1)
                        error22 = wer(res[j], data2)
                        wer1.append(error11)
                        wer2.append(error22)
                        
    if bool(wer1)==True:
        error11 = min(wer1)
        error22 = min(wer2)
        err1.append(min(error11, error1))
        err2.append(min(error22, error2))
        wer_opt.append(min(min(error11, error1),min(error22, error2)))
    if bool(wer1)==False:
        print(i)
        print(data1)

err1 = np.array(err1)
err2 = np.array(err2)
wer_opt = np.array(wer_opt)

print(np.mean(err1))
print(np.mean(err2))
print(np.mean(wer_opt))

rows=[]
fields=[]
filename_i = 'output.csv'
with open(filename_i, 'r') as csvfile_i: 
    # creating a csv reader object 
    csvreader = csv.reader(csvfile_i) 
    # extracting field names through first row 
    fields = next(csvreader) 
    # extracting each data row one by one 
    for row in csvreader: 
        rows.append(row)  
    # get total number of rows 
    print("Total no. of rows: %d"%(csvreader.line_num)) 

#print(rows)
#print(fields)

fields.pop()
fields.append('error 1')
fields.append('error 2')
fields.append('final word error rate')
for i in range(len(rows)) :
    rows[i].pop()
    rows[i].append(err1[i])
    rows[i].append(err2[i])
    rows[i].append(wer_opt[i])

#print(rows)
#print(fields)

filename_o = 'final_output.csv'
with open(filename_o, 'w') as csvfile_o:  
    # creating a csv writer object  
    csvwriter = csv.writer(csvfile_o)  
    # writing the fields  
    csvwriter.writerow(fields)  
    # writing the data rows  
    csvwriter.writerows(rows) 