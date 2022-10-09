import RPi.GPIO as GPIO
import time

PIN_IR = 17
PIN_LED = 18

GPIO.setmode(GPIO.BCM)        # use BCM numbers
GPIO.setup(PIN_LED, GPIO.OUT)   # set the PIN_LED OUTPUT mode
GPIO.output(PIN_LED, GPIO.LOW)  # make PIN_LED output LOW level
GPIO.setup(PIN_IR, GPIO.IN)   # set the PIN_LED OUTPUT mode

try:
    while True:
        ir = GPIO.input(PIN_IR)
        if ir:
            GPIO.output(PIN_LED, GPIO.HIGH)
        time.sleep(1)

finally:
    GPIO.cleanup()