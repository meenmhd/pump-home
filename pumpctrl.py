import RPi.GPIO as GPIO
from time import sleep

pt = 0
relay_pin = 26
GPIO.setmode(GPIO.BCM)
GPIO.setup(relay_pin, GPIO.OUT)

def relayon():
        GPIO.output(relay_pin, 1)
        sleep(pt)
        GPIO.output(relay_pin, 0)
        GPIO.cleanup()

