from gpiozero import OutputDevice
import time
import os
import sys
import RPi.GPIO as GPIO
zone1 = OutputDevice(16,initial_value=False)
zone2 = OutputDevice(20,initial_value=False)
zone3 = OutputDevice(21,initial_value=False)

print (zone1.value, zone2.value, zone3.value, end='\n')

zone1.off()
zone2.off()
zone3.off()

print (zone1.value, zone2.value, zone3.value, end='\n')
