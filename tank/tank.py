import RPi.GPIO as GPIO
import time

RT_PIN_EN = 25
RT_PIN_IN1 = 24
RT_PIN_IN2 = 23

LT_PIN_EN = 16
LT_PIN_IN1 = 20
LT_PIN_IN2 = 26

GPIO.setmode(GPIO.BCM)  # use BCM numbers

# Left Track
GPIO.setup(LT_PIN_IN1, GPIO.OUT)
GPIO.setup(LT_PIN_IN2, GPIO.OUT)
GPIO.setup(LT_PIN_EN, GPIO.OUT)

GPIO.setup(LT_PIN_IN1, GPIO.LOW)
GPIO.setup(LT_PIN_IN2, GPIO.LOW)
LT_P = GPIO.PWM(LT_PIN_EN, 1000)
LT_P.start(25)

# Right Track
GPIO.setup(RT_PIN_IN1, GPIO.OUT)
GPIO.setup(RT_PIN_IN2, GPIO.OUT)
GPIO.setup(RT_PIN_EN, GPIO.OUT)

GPIO.setup(RT_PIN_IN1, GPIO.LOW)
GPIO.setup(RT_PIN_IN2, GPIO.LOW)
RT_P = GPIO.PWM(RT_PIN_EN, 1000)
RT_P.start(25)

try:
    while True:
        cmd = input()
        if cmd == 'rb':
            GPIO.output(RT_PIN_IN1, GPIO.HIGH)
            GPIO.output(RT_PIN_IN2, GPIO.LOW)
            print("right backward")
        elif cmd == 'rf':
            GPIO.output(RT_PIN_IN1, GPIO.LOW)
            GPIO.output(RT_PIN_IN2, GPIO.HIGH)
            print("right forward")
        elif cmd == 'lb':
            GPIO.output(LT_PIN_IN1, GPIO.HIGH)
            GPIO.output(LT_PIN_IN2, GPIO.LOW)
            print("left backward")
        elif cmd == 'lf':
            GPIO.output(LT_PIN_IN1, GPIO.LOW)
            GPIO.output(LT_PIN_IN2, GPIO.HIGH)
            print("left forward")
        elif cmd == 'f':
            GPIO.output(LT_PIN_IN1, GPIO.LOW)
            GPIO.output(LT_PIN_IN2, GPIO.HIGH)
            GPIO.output(RT_PIN_IN1, GPIO.LOW)
            GPIO.output(RT_PIN_IN2, GPIO.HIGH)
            print("forward")
        elif cmd == 'b':
            GPIO.output(LT_PIN_IN1, GPIO.HIGH)
            GPIO.output(LT_PIN_IN2, GPIO.LOW)
            GPIO.output(RT_PIN_IN1, GPIO.HIGH)
            GPIO.output(RT_PIN_IN2, GPIO.LOW)
            print("backward")

        time.sleep(0.02)
finally:
    GPIO.cleanup()
