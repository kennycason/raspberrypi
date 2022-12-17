# Primary Tank code
import RPi.GPIO as GPIO
import time

R_PIN_ENABLE_A = 25
R_PIN_IN1 = 24
R_PIN_IN2 = 23

L_PIN_ENABLE_A = 16
L_PIN_IN1 = 20
L_PIN_IN2 = 26

GPIO.setmode(GPIO.BCM)  # use BCM numbers

# Left Track
GPIO.setup(L_PIN_IN1, GPIO.OUT)
GPIO.setup(L_PIN_IN2, GPIO.OUT)
GPIO.setup(L_PIN_ENABLE_A, GPIO.OUT)

GPIO.setup(L_PIN_IN1, GPIO.LOW)
GPIO.setup(L_PIN_IN2, GPIO.LOW)
L_PWM = GPIO.PWM(L_PIN_ENABLE_A, 100)
L_PWM.start(25)

# Right Track
GPIO.setup(R_PIN_IN1, GPIO.OUT)
GPIO.setup(R_PIN_IN2, GPIO.OUT)
GPIO.setup(R_PIN_ENABLE_A, GPIO.OUT)

GPIO.setup(R_PIN_IN1, GPIO.LOW)
GPIO.setup(R_PIN_IN2, GPIO.LOW)
R_PWM = GPIO.PWM(R_PIN_ENABLE_A, 100)
R_PWM.start(25)

speed = 100
leftDirection = 1
rightDirection = 1


def left_track_forward():
    print("left track forward")
    GPIO.output(L_PIN_IN1, True)
    GPIO.output(L_PIN_IN2, False)
    L_PWM.ChangeDutyCycle(100)


def left_track_reverse():
    print("left track reverse")
    GPIO.output(L_PIN_IN1, False)
    GPIO.output(L_PIN_IN2, True)
    L_PWM.ChangeDutyCycle(25)


def left_track_stop():
    print("left track stop")
    GPIO.output(L_PIN_IN1, False)
    GPIO.output(L_PIN_IN2, False)
    L_PWM.ChangeDutyCycle(0)


def right_track_forward():
    print("right track forward")
    GPIO.output(R_PIN_IN1, True)
    GPIO.output(R_PIN_IN2, False)
    R_PWM.ChangeDutyCycle(100)


def right_track_reverse():
    print("right track reverse")
    GPIO.output(R_PIN_IN1, False)
    GPIO.output(R_PIN_IN2, True)
    R_PWM.ChangeDutyCycle(25)


def right_track_stop():
    print("right track stop")
    GPIO.output(R_PIN_IN1, False)
    GPIO.output(R_PIN_IN2, False)
    R_PWM.ChangeDutyCycle(0)


def forward():
    print("forward")
    left_track_forward()
    right_track_forward()


def reverse():
    print("reverse")
    left_track_reverse()
    right_track_reverse()


def stop():
    print("stop")
    left_track_stop()
    right_track_stop()

def turn_left():
    print("turn left")
    left_track_stop()
    right_track_forward()

def turn_right():
    print("turn right")
    right_track_stop()
    left_track_forward()


def rotate_clockwise():
    print("rotate clockwise")
    right_track_reverse()
    left_track_forward()


def rotate_counterclockwise():
    print("rotate counterclockwise")
    right_track_forward()
    left_track_reverse()


def speed_up():
    global speed
    print("speed++")
    speed += 10
    if speed >= 100:
        speed = 100
    # L_PWM.ChangeDutyCycle(speed)
    # R_PWM.ChangeDutyCycle(speed)


def speed_down():
    global speed
    print("speed--")
    speed -= 10
    if speed < 0:
        speed = 0
    # L_PWM.ChangeDutyCycle(speed)
    # R_PWM.ChangeDutyCycle(speed)


# ↖  ↑  ↗   1 speed--
#   QWE     2 speed++
# ← ASD →   H clockwise
#   ZXC     J counterclockwise
# ↙  ↓  ↘　
def handle_input():
    cmd = input()
    if cmd == 'q':
        left_track_forward()
    elif cmd == 'w':
        forward()
    elif cmd == 'e':
        right_track_forward()

    elif cmd == 'a':
        turn_left()
    elif cmd == 's':
        stop()
    elif cmd == 'd':
        turn_right()

    elif cmd == 'z':
        left_track_reverse()
    elif cmd == 'x':
        reverse()
    elif cmd == 'c':
        right_track_reverse()

    if cmd == 'h':
        rotate_clockwise()
    elif cmd == 'j':
        rotate_counterclockwise()

    elif cmd == '1':
        speed_up()
    elif cmd == '2':
        speed_down()


stop()
try:
    while True:
        handle_input()
        time.sleep(0.02)
finally:
    GPIO.cleanup()
