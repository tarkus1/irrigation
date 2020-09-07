#!/usr/bin/python3
# coding: utf-8

# In[14]:


import logging
import pandas as pd

import feedparser
from datetime import datetime
import dateutil
from pytz import timezone
import mysql.connector
import sqlalchemy

d = feedparser.parse('https://weather.gc.ca/rss/city/ab-52_e.xml')
print("title ",d.feed.title)
len(d['items'])

fcstutc = dateutil.parser.parse(d['items'][2]['published'])
print("time ",fcstutc)

fcstupd = fcstutc.astimezone(timezone('America/Edmonton'))

popDF =  pd.DataFrame(columns=['Day', 'DayNight', 'POP','Date'])

timeofDay ="undef"

for i in range(0,14):
    e = d['items'][i]
    print("\nNew Day ", e['title'],"\n")
    fcst=e['title'].split(':')
    print("fcst ", len(fcst),'\n', "fcst is ", fcst)
            
    # F = fcst[0].split(' ')
    dayNight = fcst[0].split(' ')
    
    print("length of daynight ", len(dayNight), "and daynight ", dayNight)
    theDay = dayNight[0]
    if len(dayNight)>1:
        if (dayNight[1] == 'night'):
            timeofDay = 'night'
    else:
        timeofDay = 'day'
    
    print("the day ",theDay, "time of day ", timeofDay)
    
    if len(fcst)>1:
        print('second part ',fcst[1])
        theDirt = fcst[1].split(' ')
        print("the dirt ", theDirt)
        
        if fcst[1].find('Rain') > 0:
            #pop = fcst[1].split('POP')
            #print('\nPOP ',pop[1])
            pop = 100
            print('\nPOP ',pop)
        
        elif fcst[1].find('Showers') > 0 or fcst[1].find('Periods of rain') > 0:
            pop = 50
        else:
            pop = 0
        
        popDF = popDF.append({'Day': theDay, 'DayNight': timeofDay, 'POP': pop}, ignore_index=True)

        
print('\nPOP days\n',popDF)


# In[15]:


from datetime import timedelta
def get_next_monday():
    date0 = datetime.now()
#     date0 = datetime.date(year, month, day)
    next_monday = date0 + timedelta(7 - date0.weekday() or 7)
    return next_monday

print ("next monday ", get_next_monday())

import calendar
import pandas as pd
import pandas as pd

fcstDays = pd.DataFrame(columns=['Day', 'Date'])

for dd in range(0,7):
    
    dayN = datetime.now() + timedelta(days=dd)
    dayName = calendar.day_name[dayN.weekday()]
    dayDt = dayN.date()
    
    fcstDays = fcstDays.append({'Day': dayName, 'Date': dayDt}, ignore_index=True)

print(fcstDays)

fcstwk = pd.merge(popDF, fcstDays, on='Day')

fcstwk.sort_values('Date_y')
fcstwk.Date_x=fcstupd

fcstwk = fcstwk.rename(columns={'Date_x':'Forecast Date','Date_y':'Date Forecasted'})

print(fcstwk)


# In[29]:


fcstHist = pd.read_pickle('/home/pi/irrigation/weather/FcstHistoryNew.pkl')

fcstHist = fcstHist.append(fcstwk, ignore_index=True)

fcstHist = fcstHist.drop_duplicates()


fcstHist.to_pickle('/home/pi/irrigation/weather/FcstHistoryNew.pkl')

pfcst = fcstHist.sort_values(by=['Forecast Date','Date Forecasted','DayNight'],ascending=[True, True,True])

print(pfcst[['Forecast Date','Day','DayNight','Date Forecasted','POP']].tail(50))

#wfcst = fcstwk.sort_values(by=['Forecast Date','Date Forecasted','DayNight'],ascending=[True, False,True])

#print(wfcst[['Forecast Date','Day','DayNight','Date Forecasted','POP']].tail(50))



engine = sqlalchemy.create_engine('mysql+pymysql://pi:Skram1Skram1@localhost:3306/irrigation')

##moist = pd.read_sql_table("moisture",engine)

fcstHist.to_sql("Forecast",engine,if_exists='replace')