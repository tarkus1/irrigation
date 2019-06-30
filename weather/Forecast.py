#!/usr/bin/python3
# coding: utf-8


import logging
import pandas as pd
import feedparser
from datetime import datetime
import dateutil
from pytz import timezone

d = feedparser.parse('https://weather.gc.ca/rss/city/ab-52_e.xml')
##print(d.feed.title)
len(d['items'])

fcstutc = dateutil.parser.parse(d['items'][2]['published'])
##print(fcstutc)

fcstupd = fcstutc.astimezone(timezone('America/Edmonton'))

popDF =  pd.DataFrame(columns=['Day', 'DayNight', 'POP','Date'])

for i in range(0,14):
    e = d['items'][i]
##    print("\nNew Day ", e['title'],"\n")
    fcst=e['title'].split(':')
##    print(len(fcst),'\n')
            
    
    dayNight = fcst[0].split(' ')
    
##    print(len(dayNight))
    
    theDay = dayNight[0]
    if len(dayNight)>1:
        if (dayNight[1] == 'night'):
            timeofDay = 'night'
    else:
        timeofDay = 'day'
    
#     print(theDay, timeofDay)
    
    if len(fcst)>1:
##        print('second part ',fcst[1])
        if fcst[1].find('POP') > 0:
            pop = fcst[1].split('POP')
##            print('\nPOP ',pop[1])
            popDF = popDF.append({'Day': theDay, 'DayNight': timeofDay, 'POP': pop[1]}, ignore_index=True)

        
##print('\nPOP days\n',popDF)



from datetime import timedelta
def get_next_monday():
    date0 = datetime.now()
#     date0 = datetime.date(year, month, day)
    next_monday = date0 + timedelta(7 - date0.weekday() or 7)
    return next_monday

##print (get_next_monday())

import calendar
import pandas as pd

fcstDays = pd.DataFrame(columns=['Day', 'Date'])

for dd in range(0,7):
    
    dayN = datetime.now() + timedelta(days=dd)
    dayName = calendar.day_name[dayN.weekday()]
    dayDt = dayN.date()
    
    fcstDays = fcstDays.append({'Day': dayName, 'Date': dayDt}, ignore_index=True)

##fcstDays

fcstwk = pd.merge(popDF, fcstDays, on='Day')

fcstwk.sort_values('Date_y')
fcstwk.Date_x=fcstupd

fcstwk = fcstwk.rename(columns={'Date_x':'Forecast Date','Date_y':'Date Forecasted'})

##print(fcstwk)

fcstHist = pd.read_pickle('./FcstHistory.pkl')

fcstHist = fcstHist.append(fcstwk, ignore_index=True)

fcstHist = fcstHist.drop_duplicates()


fcstHist.to_pickle('./FcstHistory.pkl')

print(fcstHist)

