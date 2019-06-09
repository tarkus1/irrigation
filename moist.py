#!/usr/bin/python3
# coding: utf-8

# In[1]:


import pandas as pd

moist = pd.read_csv('/home/pi/irrigation/test.csv')
# moist = pd.read_csv('test.csv')


# In[2]:


moist.columns = ["Timetemp", "Temp", "Humidity"]
# moist


# In[3]:


moist['Time'] = pd.to_datetime(moist["Timetemp"])
moist = moist.drop(columns='Timetemp')
moist.dtypes


# In[4]:


# moist['Time'].head()


# In[5]:


moist = moist.set_index('Time')
# moist.head()


# In[6]:


moist['Week']=moist.index.weekofyear
# moist['freq']=moist.index.freq
moist.tail()


# In[7]:


# import matplotlib.pyplot as plt

# moist['Humidity'].plot()


# In[8]:


# moist['2019-06-01 14:00':].Humidity.plot(legend=True)
# moist['2019-06-01 14:00':].Temp.plot(secondary_y=True,label='Temp',legend=True)


# In[9]:


##hourly = moist.resample('15Min').mean()
##hourly['2019-06':].Humidity.plot(legend=True)
##hourly['2019-06':].Temp.plot(secondary_y=True,legend=True)


# In[10]:


##hourly = moist.resample('1H').mean()
##hourly.dropna()
##print(hourly['2019-05-30':])
##hourly['2019-05-30':].Humidity.plot(legend=True)
##hourly['2019-05-30':].Temp.plot(secondary_y=True,legend=True)


# In[11]:


submoist=moist['2019-06-06':]
m=submoist[1:].Humidity.values
tt=submoist.index-submoist.index[0]
tt=tt[1:]
tf=tt.to_frame()
# tf
# tf.Time.values.astype('float64')
# mt=tt.astype('timedelta64[m]')
tt1=tf.Time.values.astype('float64')
# tt1
mt=tt1.reshape(-1,1)
# print(mt, mt.max())
mtmro=mt.max()+(24*3600)
# print(mtmro.reshape(-1,1))
# mt=tt.to_pytimedelta
# print(mt.dtype,mt)
# print( m.dtype,m)


# In[19]:


from sklearn import datasets, linear_model
import numpy as np
regr = linear_model.LinearRegression()
regr.fit(mt,m)
mtmro=mt.max()+(24*3600*10)
print(mt.max(), '\n',np.array(mtmro))
newmt=np.array(mtmro).reshape(-1,1)
z=regr.predict(newmt)
print('New future time\t',newmt,'\npredicted\t',z,'\nslope\t',regr.coef_)


# In[13]:


##import matplotlib.pyplot as plt
##from matplotlib import interactive
##interactive(True)
##plt.plot(mt,m)
##plt.plot(mt,regr.predict(mt))

