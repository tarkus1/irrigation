from gpiozero import OutputDevice
from time import sleep
import subprocess
import os, csv, re
import sys
import RPi.GPIO as GPIO
from datetime import datetime, timedelta


zone1 = OutputDevice(16, active_high=False, initial_value=False)
zone2 = OutputDevice(20,active_high=False, initial_value=False)
zone3 = OutputDevice(21,active_high=False, initial_value=False)

off = datetime.now()+timedelta(seconds=300)
print('Time off ', off.strftime('%H:%M:%S'))

print(zone1.value, zone2.value, zone3.value, end='\n')


while (datetime.now() < off):
    try:
        # zone1.toggle()
        # zone2.toggle()
        zone3.on()
        print("zone 3 on ", zone3.value)

        print (zone1.value, zone2.value, zone3.value, end='\n')

    except Exception as e:
        print (e)

    finally:
        sleep(20)
        print('Running', datetime.now().strftime('%H:%M:%S'))

        


zone1.off()
zone2.off()
zone3.off()
print("zone 3 off ", zone3.value)
print('Actual time off ', datetime.now().strftime('%H:%M:%S'))
