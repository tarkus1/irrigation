#!/usr/bin/python3
# coding: utf-8

import pandas as pd
import datetime
import sqlalchemy
import matplotlib.pyplot as plt
from matplotlib import interactive
interactive(True)


startDate = datetime.datetime.now()-datetime.timedelta(3)
print (startDate.strftime('%Y-%m-%d %H:%M:%S'),'\n\n')

strtDate =startDate.strftime('%Y-%m-%d %H:%M:%S')

engine = sqlalchemy.create_engine('mysql+pymysql://pi:Skram1Skram1@localhost:3306/irrigation')

##moist = pd.read_sql_table("moisture",engine)

sql = "SELECT * FROM moisture where (Time > '" + strtDate + "');"


moist = pd.read_sql_query(sql,engine)


moist = moist.set_index('Time')

moist.tail()



submoist=moist[strtDate:]
m=submoist[1:].Humidity.values
tt=submoist.index-submoist.index[0]
tt=tt[1:]
tf=tt.to_frame()

daysfcst = 3

tt1=tf.Time.values.astype('float64')
# tt1
mt=tt1.reshape(-1,1)
# print(mt, mt.max())
mtmro=mt.max()+(24*3600*daysfcst)
# print(mtmro.reshape(-1,1))
# mt=tt.to_pytimedelta
# print(mt.dtype,mt)
# print( m.dtype,m)


fdate=submoist.index.max() + datetime.timedelta(daysfcst)

# In[19]:


from sklearn import datasets, linear_model
import numpy as np
regr = linear_model.LinearRegression()
regr.fit(mt,m)
mtmro=mt.max()+(24*3600*10)
print(mt.max(), '\n',np.array(mtmro))
newmt=np.array(mtmro).reshape(-1,1)
z=regr.predict(newmt)
print('New future time\t',fdate,'\npredicted\t',z,'\nslope\t',regr.coef_)

##hours=[4,5,6]
##sprinkHr = moist[moist.index.hour.isin(hours)]

sprinkHr = moist

print('\n\nMean humidity between 4 and 7am\t',sprinkHr.Humidity.mean())

print('\nLatest values\n',sprinkHr.tail())

target_date_time_ms = 200000 # or whatever
base_datetime = datetime.datetime( 1970, 1, 1 )
delta = datetime.timedelta( 0, 0, 0, target_date_time_ms )
target_date = base_datetime + delta


import matplotlib.pyplot as plt
from matplotlib import interactive
interactive(True)
sprinkHr.Humidity.plot(legend=True)
sprinkHr.Temp.plot(secondary_y=True,legend=True)

plt.plot(mt,m)
plt.plot(mt,regr.predict(mt))

