#!/usr/bin/python3.5 

# In[1]:


import pandas as pd
import numpy as np
import moistFunc

def trendline(data, order=1):
    coeffs = np.polyfit(data.index.values, list(data), order)
    slope = coeffs[-2]
    return float(slope)

moist = pd.read_csv('~/irrigation/test.csv')


moist.columns = ["Timetemp", "Temp", "Humidity"]
moist

moist['Time'] = pd.to_datetime(moist["Timetemp"])
moist = moist.drop(columns='Timetemp')

##print('trendline slope results ',trendline(moist,1))

moist = moist.set_index('Time')
print(moist.tail())

print('\nWhat the sprinkler module sees\n', moistFunc.humid())
