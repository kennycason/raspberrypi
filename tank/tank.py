import RPi.GPIO as GPIO
import time

RT_PIN_ENABLE_A = 25
RT_PIN_IN1 = 24
RT_PIN_IN2 = 23

LT_PIN_ENABLE_A = 16
LT_PIN_IN1 = 20
LT_PIN_IN2 = 26

GPIO.setmode(GPIO.BCM)  # use BCM numbers

# Left Track
GPIO.setup(LT_PIN_IN1, GPIO.OUT)
GPIO.setup(LT_PIN_IN2, GPIO.OUT)
GPIO.setup(LT_PIN_ENABLE_A, GPIO.OUT)

GPIO.setup(LT_PIN_IN1, GPIO.LOW)
GPIO.setup(LT_PIN_IN2, GPIO.LOW)
LT_P = GPIO.PWM(LT_PIN_ENABLE_A, 1000)
LT_P.start(0)

# Right Track
GPIO.setup(RT_PIN_IN1, GPIO.OUT)
GPIO.setup(RT_PIN_IN2, GPIO.OUT)
GPIO.setup(RT_PIN_ENABLE_A, GPIO.OUT)

GPIO.setup(RT_PIN_IN1, GPIO.LOW)
GPIO.setup(RT_PIN_IN2, GPIO.LOW)
RT_P = GPIO.PWM(RT_PIN_ENABLE_A, 1000)
RT_P.start(0)


def turn_left():
    print("turn left")
    GPIO.output(LT_PIN_IN1, GPIO.LOW)
    GPIO.output(LT_PIN_IN2, GPIO.LOW)
    GPIO.output(RT_PIN_IN1, GPIO.LOW)
    GPIO.output(RT_PIN_IN2, GPIO.HIGH)


def turn_right():
    print("turn right")
    GPIO.output(LT_PIN_IN1, GPIO.LOW)
    GPIO.output(LT_PIN_IN2, GPIO.HIGH)
    GPIO.output(RT_PIN_IN1, GPIO.LOW)
    GPIO.output(RT_PIN_IN2, GPIO.LOW)


def left_track_forward():
    print("left track forward")
    GPIO.output(LT_PIN_IN1, GPIO.LOW)
    GPIO.output(LT_PIN_IN2, GPIO.HIGH)


def left_track_backward():
    print("left track backward")
    GPIO.output(LT_PIN_IN1, GPIO.LOW)
    GPIO.output(LT_PIN_IN2, GPIO.HIGH)


def right_track_forward():
    print("right track forward")
    GPIO.output(RT_PIN_IN1, GPIO.LOW)
    GPIO.output(RT_PIN_IN2, GPIO.HIGH)


def right_track_backward():
    print("right track backward")
    GPIO.output(RT_PIN_IN1, GPIO.HIGH)
    GPIO.output(RT_PIN_IN2, GPIO.LOW)


def move_forward():
    print("forward")
    GPIO.output(LT_PIN_IN1, GPIO.LOW)
    GPIO.output(LT_PIN_IN2, GPIO.HIGH)
    GPIO.output(RT_PIN_IN1, GPIO.LOW)
    GPIO.output(RT_PIN_IN2, GPIO.HIGH)


def backward():
    print("backward")
    GPIO.output(LT_PIN_IN1, GPIO.HIGH)
    GPIO.output(LT_PIN_IN2, GPIO.LOW)
    GPIO.output(RT_PIN_IN1, GPIO.HIGH)
    GPIO.output(RT_PIN_IN2, GPIO.LOW)


def stop():
    print("stop")
    GPIO.output(LT_PIN_IN1, GPIO.LOW)
    GPIO.output(LT_PIN_IN2, GPIO.LOW)
    GPIO.output(RT_PIN_IN1, GPIO.LOW)
    GPIO.output(RT_PIN_IN2, GPIO.LOW)


def handle_input():
    cmd = input()
    if cmd == 'rf':
        right_track_forward()
    elif cmd == 'rb':
        right_track_backward()
    elif cmd == 'lf':
        left_track_forward()
    elif cmd == 'lb':
        left_track_backward()
    elif cmd == 'f':
        move_forward()
    elif cmd == 'b':
        backward()
    elif cmd == 'l':
        turn_left()
    elif cmd == 'r':
        turn_right()
    elif cmd == 's':
        stop()


def handle_input_asdf():
    cmd = input()
    if cmd == 'a':
        turn_left()
    elif cmd == 'd':
        turn_right()
    elif cmd == 'w':
        move_forward()
    elif cmd == 's':
        stop() # move_backward()
    else:
        stop()


stop()
try:
    while True:
        # handle_input()
        handle_input_asdf()
        time.sleep(0.02)
finally:
    GPIO.cleanup()
