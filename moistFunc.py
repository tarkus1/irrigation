#!/usr/bin/python3
# coding: utf-8

import pandas as pd
import datetime
import sqlalchemy

engine = sqlalchemy.create_engine('mysql+pymysql://pi:Skram1Skram1@localhost:3306/irrigation')

moist = pd.read_sql_table("moisture",engine)

moist = moist.set_index('Time')

##moist['Week']=moist.index.weekofyear

##moist.tail()

startDate = datetime.datetime.now()-datetime.timedelta(1)
##print (startDate.strftime('%Y-%m-%d'),'\n\n')

strtDate =startDate.strftime('%Y-%m-%d')


##hourly = moist.resample('15Min').mean()
##hourly['2019-06':].Humidity.plot(legend=True)
##hourly['2019-06':].Temp.plot(secondary_y=True,legend=True)
def humid():
    hourly = moist.resample('1H').mean()
    hourly.dropna()
    print('All data mean ', hourly.Humidity.mean())
##    print(hourly[startDate:])

    print('Since start date ',hourly[startDate:].Humidity.mean())
    return(hourly[startDate:].Humidity.mean())


##humid()


##
##
##fdate=submoist.index.max() + datetime.timedelta(daysfcst)
##
### In[19]:

def whatsSo():
    from sklearn import datasets, linear_model
    import numpy as np
    regr = linear_model.LinearRegression()
    regr.fit(mt,m)
    mtmro=mt.max()+(24*3600*10)
    print(mt.max(), '\n',np.array(mtmro))
    newmt=np.array(mtmro).reshape(-1,1)
    z=regr.predict(newmt)
    print('New future time\t',fdate,'\npredicted\t',z,'\nslope\t',regr.coef_)


