import RPi.GPIO as GPIO
import time

R_PIN_ENABLE_A = 25
R_PIN_IN1 = 24
R_PIN_IN2 = 23

L_PIN_ENABLE_A = 16
L_PIN_IN1 = 20
L_PIN_IN2 = 26

speed = 50

GPIO.setmode(GPIO.BCM)  # use BCM numbers

# Left Track
GPIO.setup(L_PIN_IN1, GPIO.OUT)
GPIO.setup(L_PIN_IN2, GPIO.OUT)
GPIO.setup(L_PIN_ENABLE_A, GPIO.OUT)

GPIO.setup(L_PIN_IN1, GPIO.LOW)
GPIO.setup(L_PIN_IN2, GPIO.LOW)
L_PWM = GPIO.PWM(L_PIN_ENABLE_A, 1000)
L_PWM.start(0)
# L_PWM.ChangeDutyCycle(speed)

# Right Track
GPIO.setup(R_PIN_IN1, GPIO.OUT)
GPIO.setup(R_PIN_IN2, GPIO.OUT)
GPIO.setup(R_PIN_ENABLE_A, GPIO.OUT)

GPIO.setup(R_PIN_IN1, GPIO.LOW)
GPIO.setup(R_PIN_IN2, GPIO.LOW)
R_PWM = GPIO.PWM(R_PIN_ENABLE_A, 1000)
R_PWM.start(0)
# R_PWM.ChangeDutyCycle(speed)

speed = 100

def turn_left():
    print("turn left")
    GPIO.output(L_PIN_IN1, GPIO.LOW)
    GPIO.output(L_PIN_IN2, GPIO.LOW)
    GPIO.output(R_PIN_IN1, GPIO.LOW)
    GPIO.output(R_PIN_IN2, GPIO.HIGH)


def turn_right():
    print("turn right")
    GPIO.output(L_PIN_IN1, GPIO.LOW)
    GPIO.output(L_PIN_IN2, GPIO.HIGH)
    GPIO.output(R_PIN_IN1, GPIO.LOW)
    GPIO.output(R_PIN_IN2, GPIO.LOW)


def left_track_forward():
    print("left track forward")
    GPIO.output(L_PIN_IN1, GPIO.LOW)
    GPIO.output(L_PIN_IN2, GPIO.HIGH)


def left_track_backward():
    print("left track backward")
    GPIO.output(L_PIN_IN1, GPIO.LOW)
    GPIO.output(L_PIN_IN2, GPIO.HIGH)


def right_track_forward():
    print("right track forward")
    GPIO.output(R_PIN_IN1, GPIO.LOW)
    GPIO.output(R_PIN_IN2, GPIO.HIGH)


def right_track_backward():
    print("right track backward")
    GPIO.output(R_PIN_IN1, GPIO.HIGH)
    GPIO.output(R_PIN_IN2, GPIO.LOW)


def move_forward():
    print("forward")
    GPIO.output(L_PIN_IN1, GPIO.LOW)
    GPIO.output(L_PIN_IN2, GPIO.HIGH)
    GPIO.output(R_PIN_IN1, GPIO.LOW)
    GPIO.output(R_PIN_IN2, GPIO.HIGH)


def backward():
    print("backward")
    GPIO.output(L_PIN_IN1, GPIO.HIGH)
    GPIO.output(L_PIN_IN2, GPIO.LOW)
    GPIO.output(R_PIN_IN1, GPIO.HIGH)
    GPIO.output(R_PIN_IN2, GPIO.LOW)


def stop():
    print("stop")
    GPIO.output(L_PIN_IN1, GPIO.LOW)
    GPIO.output(L_PIN_IN2, GPIO.LOW)
    GPIO.output(R_PIN_IN1, GPIO.LOW)
    GPIO.output(R_PIN_IN2, GPIO.LOW)


def speed_up():
    global speed
    print("speed++")
    speed += 10
    if speed >= 100:
        speed = 100
    L_PWM.ChangeDutyCycle(speed)
    R_PWM.ChangeDutyCycle(speed)


def speed_down():
    global speed
    print("speed--")
    speed -= 10
    if speed < 0:
        speed = 0
    L_PWM.ChangeDutyCycle(speed)
    R_PWM.ChangeDutyCycle(speed)


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
    elif cmd == '+':
        speed_up()
    elif cmd == '-':
        speed_down()
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
