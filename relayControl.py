from gpiozero import OutputDevice
import time
import os, csv, re
import sys
import RPi.GPIO as GPIO
from datetime import datetime


zone1 = OutputDevice(16, active_high=False, initial_value=False)
zone2 = OutputDevice(20,active_high=False, initial_value=False)
zone3 = OutputDevice(21,active_high=False, initial_value=False)

print (zone1.value, zone2.value, zone3.value, end='\n')

zone1.off()
zone2.off()
zone3.off()

print (zone1.value, zone2.value, zone3.value, end='\n')

haveWatered=False

while True:

    try:
            
        p = subprocess.Popen(["owwrite", "26.76249D010000/date", "0"])

        p = subprocess.Popen(["owread", "26.76249D010000/date"], stdout=subprocess.PIPE)

        (date,errcode) = p.communicate()
        dateObj = datetime.strptime(date.decode(),'%a %b %d %H:%M:%S %Y')
        dateS = datetime.strftime(dateObj,'%Y-%m-%d %X')
        # print(datetime.strftime(dateObj,'%Y%m%d %X'))

        print("Time: ",dateS)

        p = subprocess.Popen(["owread", "26.76249D010000/temperature"], stdout=subprocess.PIPE)

        (temp,errcode) = p.communicate()
        print("Temp: ", float(temp))

        p = subprocess.Popen(["owread", "26.76249D010000/humidity"], stdout=subprocess.PIPE)

        (output,errcode) = p.communicate()
        #print(output)

        humid = float(output)
        print("Moisture: ", humid)

        if humid < 200 and humid > 10:
            print('okay')
            # red.off()
            # gr.on()
            haveWatered=False
        else :
            print('dry');
            # gr.off();
            # red.on()
            if not haveWatered :
                timeToWater(dateS)
                haveWatered=True

        therow=(dateS,float(temp),float(humid))
        # print(therow)
        
        f = open('kitchenPlant.csv', 'a', newline='')
        writer = csv.writer(f)
        writer.writerow(therow)
        f.close()

    except Exception as e:
        print (e)

    finally:    
        sleep(60)
