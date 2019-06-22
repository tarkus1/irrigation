#!/usr/bin/python3
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
import mysql.connector
from time import sleep
from datetime import datetime

theAddress = add1


while True:




    p = subprocess.Popen(["owwrite",theAddress+"/date", "0"])

    p = subprocess.Popen(["owread",theAddress+"/date"], stdout=subprocess.PIPE)

    (date,errcode) = p.communicate()
    dateObj = datetime.strptime(date.decode(),'%a %b %d %H:%M:%S %Y')
    dateS = datetime.strftime(dateObj,'%Y-%m-%d %X')
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

    therow=(dateS,float(temp),float(humid))
    # print(therow)
    
    f = open('/home/pi/irrigation/test.csv', 'a', newline='')
    writer = csv.writer(f)
    writer.writerow(therow)



    cnx = mysql.connector.connect(user='pi', password='Skram1Skram1',
                                  host='127.0.0.1',
                                  database='irrigation')

    curs=cnx.cursor()

    sql="INSERT INTO moisture values(" + "'" + dateS + "'" + "," + str(float(temp)) + "," + str(humid) +")"

    print(sql)
    
    curs.execute(sql)

    cnx.commit()
    cnx.close()

    sleep(60)

close(f)
