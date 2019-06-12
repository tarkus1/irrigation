#!/usr/bin/python3.5 

# In[1]:


import pandas as pd
import numpy as np

def trendline(data, order=1):
    coeffs = np.polyfit(data.index.values, list(data), order)
    slope = coeffs[-2]
    return float(slope)

moist = pd.read_csv('~/irrigation/test.csv')


# In[2]:


moist.columns = ["Timetemp", "Temp", "Humidity"]
moist


# In[4]:


moist['Time'] = pd.to_datetime(moist["Timetemp"])
moist = moist.drop(columns='Timetemp')


# In[5]:


moist = moist.set_index('Time')
print(moist.tail())


#print(trendline(moist['Humidity']))
