from gpiozero import OutputDevice
from time import sleep
import subprocess
import os, csv, re
import sys
import RPi.GPIO as GPIO
from datetime import datetime


zone1 = OutputDevice(16, active_high=False, initial_value=False)
zone2 = OutputDevice(20,active_high=False, initial_value=False)
zone3 = OutputDevice(21,active_high=False, initial_value=False)

device = "26.76249D010000/date"

print (zone1.value, zone2.value, zone3.value, end='\n')

zone1.on()
zone2.on()
zone3.on()

print (zone1.value, zone2.value, zone3.value, end='\n')

            
p = subprocess.Popen(["owwrite", device, "0"])

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

sleep(5)

