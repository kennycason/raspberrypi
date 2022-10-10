from enum import Enum
from typing import Dict, List

import RPi.GPIO as GPIO
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

UNIT_TIME = 0.5  # seconds
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


def write_signal(signal: Signal):
    print(signal)
    if signal == Signal.DOT:
        GPIO.output(PIN_OUT, GPIO.HIGH)
        time.sleep(DOT_UNITS * UNIT_TIME)
        GPIO.output(PIN_OUT, GPIO.LOW)
    elif signal == Signal.DASH:
        GPIO.output(PIN_OUT, GPIO.HIGH)
        time.sleep(DASH_UNITS * UNIT_TIME)
        GPIO.output(PIN_OUT, GPIO.LOW)

    time.sleep(SIGNAL_BREAK_UNITS)


def write_symbol(symbol: str):
    symbol = symbol.upper()

    if symbol not in SYMBOL_MAP:
        print("Symbol not found: [" + str(symbol) + "]")
        return

    signals = SYMBOL_MAP[symbol]
    for signal in signals:
        write_signal(signal)

    if symbol == ' ':
        print('SPACE')
        time.sleep(WORD_BREAK_UNITS * UNIT_TIME)
    else:
        print('SYMBOL BREAK')
        time.sleep(SYMBOL_BREAK_UNITS)


def write_symbols(symbols: str):
    for symbol in symbols:
        write_symbol(symbol)


try:
    write_symbols("HELLO WORLD")
finally:
    GPIO.cleanup()
