import RPi.GPIO as GPIO
import time

PIN_IR = 17
PIN_OUT = 18                    # LED or Buzzer

GPIO.setmode(GPIO.BCM)          # use BCM numbers
GPIO.setup(PIN_OUT, GPIO.OUT)   # set the PIN_LED OUTPUT mode
GPIO.output(PIN_OUT, GPIO.LOW)  # make PIN_OUT output LOW level
GPIO.setup(PIN_IR, GPIO.IN)     # set the PIN_OUT OUTPUT mode

try:
    while True:
        ir = GPIO.input(PIN_IR)
        print("ir input: " + str(ir))
        if ir:
            GPIO.output(PIN_OUT, GPIO.HIGH)
        else:
            GPIO.output(PIN_OUT, GPIO.LOW)
        time.sleep(0.2)

finally:
    GPIO.cleanup()