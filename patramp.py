#!/usr/bin/python3

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.OUT)

try:
    GPIO.output(24, True)
    time.sleep(4)
    GPIO.output(24, False)
    time.sleep(1)

except KeyboardInterrupt:
    pass

GPIO.cleanup()
