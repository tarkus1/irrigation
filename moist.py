#!/usr/bin/python3
# coding: utf-8

import pandas as pd
import datetime

moist = pd.read_csv('/home/pi/irrigation/test.csv')
# moist = pd.read_csv('test.csv')


# In[2]:


moist.columns = ["Timetemp", "Temp", "Humidity"]
# moist

moist['Time'] = pd.to_datetime(moist["Timetemp"])
moist = moist.drop(columns='Timetemp')
moist.dtypes

moist = moist.set_index('Time')

moist['Week']=moist.index.weekofyear

moist.tail()

startDate = datetime.datetime.now()-datetime.timedelta(3)
print (startDate.strftime('%Y-%m-%d'),'\n\n')

strtDate =startDate.strftime('%Y-%m-%d')


##hourly = moist.resample('15Min').mean()
##hourly['2019-06':].Humidity.plot(legend=True)
##hourly['2019-06':].Temp.plot(secondary_y=True,legend=True)

##hourly = moist.resample('1H').mean()
##hourly.dropna()
##print(hourly['2019-05-30':])
##hourly['2019-05-30':].Humidity.plot(legend=True)
##hourly['2019-05-30':].Temp.plot(secondary_y=True,legend=True)

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


##target_date_time_ms = 200000 # or whatever
##base_datetime = datetime.datetime( 1970, 1, 1 )
##delta = datetime.timedelta( 0, 0, 0, target_date_time_ms )
##target_date = base_datetime + delta


# In[13]:


##import matplotlib.pyplot as plt
##from matplotlib import interactive
##interactive(True)
##plt.plot(mt,m)
##plt.plot(mt,regr.predict(mt))

