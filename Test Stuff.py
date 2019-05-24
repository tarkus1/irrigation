#!/usr/bin/env python
# coding: utf-8

# In[1]:


# import pandas as pd


# In[1]:


import os, sys, subprocess

# read the owdir

p = subprocess.Popen(["owdir"], stdout=subprocess.PIPE)
(names,errcode) = p.communicate()
temp=names.decode()
address=temp.split("/")
# print("just decode "+names.decode())
# address=names.split("/")

add1=(str(address[1]).strip())
print(add1)

try:
    add2=(str(address[2]).strip())
except IOerror:
    print("didn't work")
else:
    print(add2)


# In[2]:


import subprocess
import csv
import re


from gpiozero import LED
from time import sleep
from datetime import datetime

# gr=LED(4)
# red=LED(14)

theAddress = add1


while True:
# if True:



    p = subprocess.Popen(["owwrite",theAddress+"/date", "0"])

    p = subprocess.Popen(["owread",theAddress+"/date"], stdout=subprocess.PIPE)

    (date,errcode) = p.communicate()
    dateObj = datetime.strptime(date.decode(),'%a %b %d %H:%M:%S %Y')
    dateS = datetime.strftime(dateObj,'%Y%m%d %X')
    # print(datetime.strftime(dateObj,'%Y%m%d %X'))

    print("Time: ",dateS)

    p = subprocess.Popen(["owread", theAddress+"/temperature"], stdout=subprocess.PIPE)

    (temp,errcode) = p.communicate()
    print("Temp: ", float(temp))

    p = subprocess.Popen(["owread", theAddress+"/humidity"], stdout=subprocess.PIPE)

    (output,errcode) = p.communicate()
    #print(output)

    humid = float(output)
    print("Moisture: ", humid)

#     if humid < 200 and humid > 10:
#         print('okay')
#         red.off()
#         gr.on()
#     else :
#         print('dry');
#         gr.off();
#         red.on()

    therow=(dateS,float(temp),float(humid))
    # print(therow)
    
    f = open('test.csv', 'a', newline='')
    writer = csv.writer(f)
    writer.writerow(therow)
#     close(f)
    sleep(60)

close(f)


# In[ ]:




