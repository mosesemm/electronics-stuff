from gpiozero import LED
from time import sleep

red = LED(27)

while True:
  red.on()

  sleep(5)

  red.off()

  sleep(5)
