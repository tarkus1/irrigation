#!/usr/bin/env python
# coding: utf-8

# In[5]:


#import pymysql
#conn = pymysql.connect(host='localhost',user='pi', passwd='Skram1Skram1', db='irrigation')
#cur = conn.cursor()
#cur.execute("SELECT * FROM moisture")


# In[2]:


import pandas as pd
import datetime

moist = pd.read_csv('/home/pi/irrigation/test.csv')

moist.columns = ["Timetemp", "Temp", "Humidity"]
# moist

moist['Time'] = pd.to_datetime(moist["Timetemp"])
moist = moist.drop(columns='Timetemp')
moist.dtypes

moist = moist.set_index('Time')

moist['Week']=moist.index.weekofyear

testdb = moist.tail()

startDate = datetime.datetime.now()-datetime.timedelta(5)


# In[3]:


print(testdb)

import mysql.connector
from mysql.connector import Error
try:
    connection = mysql.connector.connect(host='localhost',
                             database='irrigation',
                             user='pi',
                             password='Skram1Skram1')
    if connection.is_connected():
       db_Info = connection.get_server_info()
       print("Connected to MySQL database... MySQL Server version on ",db_Info)

       cursor = connection.cursor()
       cursor.execute("select database();")
       record = cursor.fetchone()
       print ("Your connected to - ", record)

except Error as e :
    print ("Error while connecting to MySQL", e)


testdb.to_sql('test',connection)
