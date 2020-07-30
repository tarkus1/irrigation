#!/usr/bin/python3
# coding: utf-8


import logging
import os, sys, subprocess
import csv
import re
import mysql.connector
from time import sleep
from datetime import datetime

logging.basicConfig(filename='/home/pi/Documents/irrig.log',level=logging.DEBUG)

p = subprocess.Popen(["owdir"], stdout=subprocess.PIPE)
(names,errcode) = p.communicate()
temp=names.decode()
address=temp.split("/")

add1=(str(address[1]).strip())
logging.info(add1)

try:
    add2=(str(address[2]).strip())
except IOerror:
    logging.error("didn't work")
else:
    logging.info(add2)


theAddress = add1


while True:

    try:
             
        p = subprocess.Popen(["owwrite",theAddress+"/date", "0"])

        p = subprocess.Popen(["owread",theAddress+"/date"], stdout=subprocess.PIPE)

        (date,errcode) = p.communicate()
        dateObj = datetime.strptime(date.decode(),'%a %b %d %H:%M:%S %Y')
        dateS = datetime.strftime(dateObj,'%Y-%m-%d %X')
        # print(datetime.strftime(dateObj,'%Y%m%d %X'))

        ##        print("Time: ",dateS)

        p = subprocess.Popen(["owread", theAddress+"/temperature"], stdout=subprocess.PIPE)

        (temp,errcode) = p.communicate()
        ##        print("Temp: ", float(temp))

        p = subprocess.Popen(["owread", theAddress+"/humidity"], stdout=subprocess.PIPE)

        (output,errcode) = p.communicate()
        #print(output)

        humid = float(output)
        ##        print("Moisture: ", humid)

        therow=(dateS,float(temp),float(humid))
        # print(therow)
            
        #    f = open('/home/pi/irrigation/test.csv', 'a', newline='')
        #    writer = csv.writer(f)
        #    writer.writerow(therow)



        cnx = mysql.connector.connect(user='pi', password='Skram1Skram1',
                                      host='127.0.0.1',
                                      database='irrigation')

        curs=cnx.cursor()

        sql="INSERT INTO moisture values(" + "'" + dateS + "'" + "," + str(float(temp)) + "," + str(humid) +")"

        logging.info(sql)
        
        curs.execute(sql)

        cnx.commit()
        cnx.close()
        
    except IOerror:
        logging.warning(" this read didn't work")
        continue
    else:
        sleep(300)

#close(f)
