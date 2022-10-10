import RPi.GPIO as GPIO
import smbus
import time

PIN_OUT: int = 18  # LED or Buzzer

GPIO.setmode(GPIO.BCM)          # use BCM numbers
GPIO.setup(PIN_OUT, GPIO.OUT)   # set the PIN_OUT OUTPUT mode
GPIO.output(PIN_OUT, GPIO.LOW)  # make PIN_OUT OUTPUT LOW level

address = 0x48  # address  -> device address
cmd = 0x40  # DA converter command
A0 = 0x40  # A0  -> port address
A1 = 0x41
A2 = 0x42
A3 = 0x43
bus = smbus.SMBus(1)  # start the bus


def analogRead(count):
    while True:
        try:
            return bus.read_byte_data(address, cmd + count)
        except OSError:
            time.sleep(0.02)
            pass

def read_symbols():
    while True:
        value = analogRead(0)  # read A0 data

        print("data: %1.0f" % value)
        # time.sleep(0.05)

try:
    read_symbols()
finally:
    GPIO.cleanup()
