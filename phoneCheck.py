#!/usr/bin/python3.5 

# In[1]:


import pandas as pd
import numpy as np
import moistFunc

def trendline(data, order=1):
    coeffs = np.polyfit(data.index.values, list(data), order)
    slope = coeffs[-2]
    return float(slope)

import sqlalchemy

engine = sqlalchemy.create_engine('mysql+pymysql://pi:Skram1Skram1@localhost:3306/irrigation')

moist = pd.read_sql_table("moisture",engine)

moist = moist.set_index('Time')

print(moist.tail())

print('\nWhat the sprinkler module sees\n', moistFunc.humid())
