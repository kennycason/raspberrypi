import RPi.GPIO as GPIO
import time

from morse_code import Signal, DOT_TIME, DASH_TIME, SIGNAL_BREAK_TIME, SYMBOL_MAP, SYMBOL_BREAK_TIME, \
    WORD_BREAK_TIME

PIN_OUT = 18                    # LED or Buzzer

GPIO.setmode(GPIO.BCM)          # use BCM numbers
GPIO.setup(PIN_OUT, GPIO.OUT)   # set the PIN_OUT OUTPUT mode
GPIO.output(PIN_OUT, GPIO.LOW)  # make PIN_OUT OUTPUT LOW level

def write_signal(signal: Signal):
    print(signal)
    GPIO.output(PIN_OUT, GPIO.HIGH)

    if signal == Signal.DOT:
        time.sleep(DOT_TIME)
    elif signal == Signal.DASH:
        time.sleep(DASH_TIME)

    GPIO.output(PIN_OUT, GPIO.LOW)
    time.sleep(SIGNAL_BREAK_TIME)


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
        time.sleep(WORD_BREAK_TIME)
    else:
        print('SYMBOL BREAK')
        time.sleep(SYMBOL_BREAK_TIME)


def write_symbols(symbols: str):
    for symbol in symbols:
        write_symbol(symbol)


try:
    write_symbols("HELLO WORLD")
finally:
    GPIO.cleanup()
