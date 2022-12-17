# Primary Tank code
import sys
import RPi.GPIO as GPIO
import time
from enum import Enum
import pigpio
from nrf24 import *

R_PIN_ENABLE_A = 25
R_PIN_IN1 = 24
R_PIN_IN2 = 23

L_PIN_ENABLE_A = 16
L_PIN_IN1 = 20
L_PIN_IN2 = 26

GPIO.setmode(GPIO.BCM)  # use BCM numbers
ADDRESS = "FNK29"


class Direction(Enum):
    FORWARD = 1
    REVERSE = 2


class Track:
    def __init__(self, pinEnableA: int, pinIn1: int, pinIn2: int, isInverted: bool = False):
        print("Init Track, enA: " + str(pinEnableA) + ", in1: " + str(pinIn1) + ", in2: " + str(pinIn2))
        self.pinEnableA = pinEnableA
        self.pinIn1 = pinIn1
        self.pinIn2 = pinIn2
        self.pwmMax = 100
        self.pwmStart = 25
        self.speed = 100 # not used
        self.direction = Direction.FORWARD
        self.isInverted = isInverted

        GPIO.setup(pinIn1, GPIO.OUT)
        GPIO.setup(pinIn2, GPIO.OUT)
        GPIO.setup(pinEnableA, GPIO.OUT)

        GPIO.setup(pinIn1, GPIO.LOW)
        GPIO.setup(pinIn2, GPIO.LOW)

        self.pwm = GPIO.PWM(pinEnableA, self.pwmMax)
        self.pwm.start(self.pwmStart)


    def forward(self):
        print("left track forward")
        if not self.isInverted:
            GPIO.output(self.pinIn1, True)
            GPIO.output(self.pinIn2, False)
            self.pwm.ChangeDutyCycle(100)
        else:
            GPIO.output(self.pinIn1, False)
            GPIO.output(self.pinIn2, True)
            self.pwm.ChangeDutyCycle(25)


    def reverse(self):
        print("left track reverse")
        if not self.isInverted:
            GPIO.output(self.pinIn1, False)
            GPIO.output(self.pinIn2, True)
            self.pwm.ChangeDutyCycle(25)
        else:
            GPIO.output(self.pinIn1, True)
            GPIO.output(self.pinIn2, False)
            self.pwm.ChangeDutyCycle(100)


    def stop(self):
        print("left track stop")
        GPIO.output(self.pinIn1, False)
        GPIO.output(self.pinIn2, False)
        self.pwm.ChangeDutyCycle(0)




class Tank:
    def __init__(self):
        self.leftTrack = Track(L_PIN_ENABLE_A, L_PIN_IN1, L_PIN_IN2, True)
        self.rightTrack = Track(R_PIN_ENABLE_A, R_PIN_IN1, R_PIN_IN2, True)

    def left_track_forward(self):
        self.leftTrack.forward()

    def left_track_reverse(self):
        self.leftTrack.reverse()

    def left_track_stop(self):
        self.leftTrack.stop()

    def right_track_forward(self):
        self.rightTrack.forward()

    def right_track_reverse(self):
        self.rightTrack.reverse()

    def right_track_stop(self):
        self.rightTrack.stop()

    def forward(self):
        print("forward")
        self.leftTrack.forward()
        self.rightTrack.forward()

    def reverse(self):
        print("reverse")
        self.leftTrack.reverse()
        self.rightTrack.reverse()

    def stop(self):
        print("stop")
        self.leftTrack.stop()
        self.rightTrack.stop()

    def turn_left(self):
        print("turn left")
        self.leftTrack.stop()
        self.rightTrack.forward()

    def turn_right(self):
        print("turn right")
        self.leftTrack.forward()
        self.rightTrack.stop()

    def rotate_clockwise(self):
        print("rotate clockwise")
        self.leftTrack.forward()
        self.rightTrack.reverse()

    def rotate_counterclockwise(self):
        print("rotate counterclockwise")
        self.leftTrack.reverse()
        self.rightTrack.forward()

    def speed_up(self):
        print("speed++")
        # self.speed += 10
        # if self.speed >= 100:
        #     self.speed = 100
        # L_PWM.ChangeDutyCycle(speed)
        # R_PWM.ChangeDutyCycle(speed)

    def speed_down(self):
        print("speed--")
        # self.speed -= 10
        # if self.speed < 0:
        #     self.speed = 0
        # L_PWM.ChangeDutyCycle(speed)
        # R_PWM.ChangeDutyCycle(speed)

    # ↖  ↑  ↗   1 speed--
    #   QWE     2 speed++
    # ← ASD →   H clockwise
    #   ZXC     J counterclockwise
    # ↙  ↓  ↘　
    def update(self):
        cmd = input()
        if cmd == 'q':
            self.leftTrack.forward()
        elif cmd == 'w':
            self.forward()
        elif cmd == 'e':
            self.rightTrack.forward()

        elif cmd == 'a':
            self.turn_left()
        elif cmd == 's':
            self.stop()
        elif cmd == 'd':
            self.turn_right()

        elif cmd == 'z':
            self.left_track_reverse()
        elif cmd == 'x':
            self.reverse()
        elif cmd == 'c':
            self.right_track_reverse()

        if cmd == 'h':
            self.rotate_clockwise()
        elif cmd == 'j':
            self.rotate_counterclockwise()

        elif cmd == '1':
            self.speed_up()
        elif cmd == '2':
            self.speed_down()



tank = Tank()

# export GPIOZERO_PIN_FACTORY=PiGPIOPin
# export PIGPIO_ADDR=192.168.4.76
# sudo pigpiod -p8889
tank.stop()
try:
    # hostname = "192.168.4.76" # "127.0.0.1" # "localhost" # "192.168.4.76"
    # port = "8889"
    # print(f'Connecting to GPIO daemon on {hostname}:{port} ...')
    # pi = pigpio.pi(hostname, port)
    # if not pi.connected:
    #     print("Not connected to Raspberry Pi ... goodbye.")
    #     sys.exit(1)
    #
    # nrf = NRF24(pi,
    #             ce=22,
    #             payload_size=RF24_PAYLOAD.DYNAMIC,
    #             channel=125,
    #             data_rate=RF24_DATA_RATE.RATE_250KBPS,
    #             pa_level=RF24_PA.MIN)
    # nrf.open_reading_pipe(RF24_RX_ADDR.P1, ADDRESS)
    # nrf.show_registers()

    while True:
        tank.update()
        time.sleep(0.02)
finally:
    GPIO.cleanup()
