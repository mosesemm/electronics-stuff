import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)

GPIO.setup(17,GPIO.OUT)
GPIO.output(17,GPIO.HIGH)
sleep(4)
GPIO.output(17,GPIO.LOW)
GPIO.cleanup()
