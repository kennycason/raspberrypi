import RPi.GPIO as GPIO
import time

PIN_IN = 17                     # IR or Button
PIN_OUT = 18                    # LED or Buzzer

GPIO.setmode(GPIO.BCM)          # use BCM numbers
GPIO.setup(PIN_OUT, GPIO.OUT)   # set the PIN_OUT OUTPUT mode
GPIO.output(PIN_OUT, GPIO.LOW)  # make PIN_OUT OUTPUT LOW level
GPIO.setup(PIN_IN, GPIO.IN)     # set the PIN_IN INPUT mode

try:
    while True:
        ir = GPIO.input(PIN_IN)
        if not ir:
            GPIO.output(PIN_OUT, GPIO.HIGH)
        else:
            GPIO.output(PIN_OUT, GPIO.LOW)

        time.sleep(0.02)
finally:
    GPIO.cleanup()