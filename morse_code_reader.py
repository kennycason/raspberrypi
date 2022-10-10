from enum import Enum
from typing import Dict, List
import RPi.GPIO as GPIO
import smbus
import time

PIN_IR: int = 17
PIN_OUT: int = 18  # LED or Buzzer

GPIO.setmode(GPIO.BCM)  # use BCM numbers
GPIO.setup(PIN_OUT, GPIO.OUT)  # set the PIN_LED OUTPUT mode
GPIO.output(PIN_OUT, GPIO.LOW)  # make PIN_OUT output LOW level
GPIO.setup(PIN_IR, GPIO.IN)  # set the PIN_OUT OUTPUT mode

# The length of a dot is one unit
# A dash is three units
# The space between parts of the same letter is one unit
# The space between letters is three units
# The space between words is seven units.

UNIT_TIME = 0.1  # seconds
DOT_UNITS = 1
DASH_UNITS = 3
SIGNAL_BREAK_UNITS = 1
SYMBOL_BREAK_UNITS = 3
WORD_BREAK_UNITS = 7


class Signal(Enum):
    DOT = 1
    DASH = 2


SYMBOL_MAP: Dict[str, List[Signal]] = {
    ' ': [],
    'A': [Signal.DOT, Signal.DASH],
    'B': [Signal.DASH, Signal.DOT, Signal.DOT, Signal.DOT],
    'C': [Signal.DASH, Signal.DOT, Signal.DASH, Signal.DOT],
    'D': [Signal.DASH, Signal.DOT, Signal.DOT],
    'E': [Signal.DOT],
    'F': [Signal.DOT, Signal.DOT, Signal.DASH, Signal.DOT],
    'G': [Signal.DASH, Signal.DASH, Signal.DOT],
    'H': [Signal.DOT, Signal.DOT, Signal.DOT, Signal.DOT],
    'I': [Signal.DOT, Signal.DOT],
    'J': [Signal.DOT, Signal.DASH, Signal.DASH, Signal.DASH],
    'K': [Signal.DASH, Signal.DOT, Signal.DASH],
    'L': [Signal.DOT, Signal.DASH, Signal.DOT, Signal.DOT],
    'M': [Signal.DASH, Signal.DASH],
    'N': [Signal.DASH, Signal.DOT],
    'O': [Signal.DASH, Signal.DASH, Signal.DASH],
    'P': [Signal.DOT, Signal.DASH, Signal.DASH, Signal.DOT],
    'Q': [Signal.DASH, Signal.DASH, Signal.DOT, Signal.DASH],
    'R': [Signal.DOT, Signal.DASH, Signal.DOT],
    'S': [Signal.DOT, Signal.DOT, Signal.DOT],
    'T': [Signal.DASH],
    'U': [Signal.DOT, Signal.DOT, Signal.DASH],
    'V': [Signal.DOT, Signal.DOT, Signal.DOT, Signal.DASH],
    'W': [Signal.DOT, Signal.DASH, Signal.DASH],
    'X': [Signal.DASH, Signal.DOT, Signal.DOT, Signal.DASH],
    'Y': [Signal.DASH, Signal.DOT, Signal.DASH, Signal.DASH],
    'Z': [Signal.DASH, Signal.DASH, Signal.DOT, Signal.DOT]
}

address = 0x48  # address  -> device address
cmd = 0x40  # DA converter command
A0 = 0x40  # A0  -> port address
A1 = 0x41
A2 = 0x42
A3 = 0x43
bus = smbus.SMBus(1)  # start the bus


def analogRead(count):
    read_val = bus.read_byte_data(address, cmd + count)
    return read_val


def read_symbols():
    while True:
        value = analogRead(0)  # read A0 data

        print("data:%1.0f" % value)
        time.sleep(0.05)


try:
    read_symbols()
finally:
    GPIO.cleanup()
