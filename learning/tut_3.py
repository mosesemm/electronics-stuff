import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)

pwm = GPIO.PWM(17, 50)
pwm.start(0)

pwm.ChangeDutyCycle(2)
sleep(1)
pwm.ChangeDutyCycle(6)
sleep(1)
pwm.ChangeDutyCycle(12)
sleep(1)
pwm.stop()
GPIO.cleanup()
