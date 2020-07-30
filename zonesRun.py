#!/usr/bin/python3.5

from gpiozero import OutputDevice
from time import sleep
import subprocess
import os, csv, re
import sys
import RPi.GPIO as GPIO
from datetime import datetime, timedelta


# new sensor is oposite. water is 134


print ("The arguments are: " , str(sys.argv))

if len(sys.argv) != 5:
    print("not correct info to start. need 3 times in minutes")
    exit()
    
elif int(sys.argv[1])>30 or int(sys.argv[2])>30 or int(sys.argv[3])>30:
    print("too long")
    exit()

# hardcoded moisture cut off for now
elif int(sys.argv[4]) > 0:
    import moistFunc
    if moistFunc.humid() < int(sys.argv[4]):
        print('Too wet')
        exit()
# does this continue?

else:
    print("starting to sprinkle\n")

zt1 = int(sys.argv[1]) *60
zt2 = int(sys.argv[2]) *60
zt3 = int(sys.argv[3]) *60
print('Started running', datetime.now().strftime('%H:%M:%S'),"\n")
print("Zone 1 for " ,zt1, "\nZone 2 for " ,zt2, "\nZone 3 for " ,zt3)

zone1 = OutputDevice(16, active_high=False, initial_value=False)
zone2 = OutputDevice(20,active_high=False, initial_value=False)
zone3 = OutputDevice(21,active_high=False, initial_value=False)


#off = datetime.now()+timedelta(seconds=1800)

sprinkle = True

#print('Time off ', off.strftime('%H:%M:%S'))


print(zone1.value, zone2.value, zone3.value, end='\n')


while (sprinkle):
    try:
        if zt1>0:
            print("run zone 1 for ",zt1)
            zone1.on()
            print("zone 1 on ", zone1.value)
            sleep(zt1)
            zone1.off()
            print("zone 1 off ", zone1.value)

        if zt2>0:
            print("run zone 2 for ",zt2)
            zone2.on()
            print("zone 2 on ", zone2.value)
            sleep(zt2)
            zone2.off()
            print("zone 2 off ", zone2.value)
        
        if zt3>0:
            print("run zone 3 for ",zt3)
            zone3.on()
            print("zone 3 on ", zone3.value)
            sleep(zt3)
            zone3.off()
            print("zone 3 off ", zone3.value)

        print ('All zones: ',zone1.value, zone2.value, zone3.value, end='\n')

        sprinkle = False 

    except Exception as e:
        print (e)

    finally:
        print('Finished running', datetime.now().strftime('%H:%M:%S'))

        

print('Actual time off ', datetime.now().strftime('%H:%M:%S'))
