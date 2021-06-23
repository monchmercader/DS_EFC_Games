import RPi.GPIO as GPIO
import time
GPIO.cleanup
GPIO.setmode(GPIO.BCM)
GPIO.setup(9, GPIO.OUT)

while True:
    GPIO.output(9, True)
    time.sleep(0.5)
    GPIO.output(9, False)
    time.sleep(0.5)

    