#!/usr/bin/python3
# coding: utf-8

import pandas as pd
import datetime
import sqlalchemy

engine = sqlalchemy.create_engine('mysql+pymysql://pi:Skram1Skram1@localhost:3306/irrigation')

#moist = pd.read_sql_table("moisture",engine)

startDate = datetime.datetime.now()-datetime.timedelta(1)
##print (startDate.strftime('%Y-%m-%d'),'\n\n')

strtDate =startDate.strftime('%Y-%m-%d')

print("startdate ",strtDate)

sql = "SELECT * FROM moisture where (Time > '" + strtDate + "');"

moist = pd.read_sql_query(sql,engine)

moist = moist.set_index('Time')

submoist=moist[strtDate:]
m=submoist[1:].Humidity.values
tt=submoist.index-submoist.index[0]
tt=tt[1:]
tf=tt.to_frame()

daysfcst = 3

tt1=tf.Time.values.astype('float64')
tt1
mt=tt1.reshape(-1,1)
# print(mt, mt.max())
mtmro=mt.max()+(24*3600*daysfcst)
# print(mtmro.reshape(-1,1))
# mt=tt.to_pytimedelta
# print(mt.dtype,mt)
# print( m.dtype,m)


fdate=submoist.index.max() + datetime.timedelta(daysfcst)
print("future date ",fdate)
##hourly = moist.resample('15Min').mean()
##hourly['2019-06':].Humidity.plot(legend=True)
##hourly['2019-06':].Temp.plot(secondary_y=True,legend=True)

def humid():
    hourly = moist.resample('1H').mean()
    hourly.dropna()
    print('All data mean ', hourly.Humidity.mean())
##    print(hourly[startDate:])

    print('ZonesRun sees this - Since start date ',hourly[startDate:].Humidity.mean())
    return(hourly[startDate:].Humidity.mean())


humid()


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


whatsSo()
