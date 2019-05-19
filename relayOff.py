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



print (zone1.value, zone2.value, zone3.value, end='\n')

