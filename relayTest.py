from gpiozero import OutputDevice
from time import sleep
import subprocess
import os, csv, re
import sys
import RPi.GPIO as GPIO
from datetime import datetime


zone1 = OutputDevice(16, active_high=False, initial_value=False)
zone2 = OutputDevice(20,active_high=False, initial_value=True)
zone3 = OutputDevice(21,active_high=False, initial_value=False)



print (zone1.value, zone2.value, zone3.value, end='\n')

while True:
    try:
        zone1.toggle()
        zone2.toggle()
        zone3.toggle()

        print (zone1.value, zone2.value, zone3.value, end='\n')

    except Exception as e:
        print (e)

    finally:
        sleep(5)

