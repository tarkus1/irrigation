#!/usr/bin/python3.5 

# In[1]:


import pandas as pd
import numpy as np
import moistFunc
import datetime


def trendline(data, order=1):
    coeffs = np.polyfit(data.index.values, list(data), order)
    slope = coeffs[-2]
    return float(slope)

import sqlalchemy


startDate = datetime.datetime.now()-datetime.timedelta(3)
print (startDate.strftime('%Y-%m-%d %H:%M:%S'),'\n\n')

strtDate =startDate.strftime('%Y-%m-%d %H:%M:%S')


engine = sqlalchemy.create_engine('mysql+pymysql://pi:Skram1Skram1@localhost:3306/irrigation')

sql = "SELECT * FROM moisture where (Time > '" + strtDate + "');"


moist = pd.read_sql_query(sql,engine)

moist = moist.set_index('Time')

print(moist.tail())

print('\nWhat the sprinkler module sees\n', moistFunc.humid())
