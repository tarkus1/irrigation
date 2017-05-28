#!/usr/bin/python

# Reading an analogue sensor with
# a single GPIO pin

# Author : Matt Hawkins
# Distribution : Raspbian
# Python : 2.7
# GPIO   : RPi.GPIO v3.1.0a

from gpiozero import *
from time import *


led =LED(17)


# Main program loop
while True:
  
  led.on()
    sleep(1)
    led.off()
    sleep(1)
