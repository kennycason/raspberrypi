# Primary Tank code
import RPi.GPIO as GPIO
from enum import Enum
import time
# import pigpio
# from nrf24 import *

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
    def __init__(self, pin_enableA: int, pin_in1: int, pin_in2: int, is_inverted: bool = False):
        print("Init Track, enA: " + str(pin_enableA) + ", in1: " + str(pin_in1) + ", in2: " + str(pin_in2))
        self.pin_enableA = pin_enableA
        self.pin_in1 = pin_in1
        self.pin_in2 = pin_in2
        self.pwmMax = 100
        self.pwmStart = 25
        self.speed = 100  # not used
        self.direction = Direction.FORWARD
        self.is_inverted = is_inverted

        GPIO.setup(pin_in1, GPIO.OUT)
        GPIO.setup(pin_in2, GPIO.OUT)
        GPIO.setup(pin_enableA, GPIO.OUT)

        GPIO.setup(pin_in1, GPIO.LOW)
        GPIO.setup(pin_in2, GPIO.LOW)

        self.pwm = GPIO.PWM(pin_enableA, self.pwmMax)
        self.pwm.start(self.pwmStart)

    def forward(self):
        print("track forward")
        if not self.is_inverted:
            GPIO.output(self.pin_in1, True)
            GPIO.output(self.pin_in2, False)
            self.pwm.ChangeDutyCycle(100)
        else:
            GPIO.output(self.pin_in1, False)
            GPIO.output(self.pin_in2, True)
            self.pwm.ChangeDutyCycle(25)

    def reverse(self):
        print("track reverse")
        if not self.is_inverted:
            GPIO.output(self.pin_in1, False)
            GPIO.output(self.pin_in2, True)
            self.pwm.ChangeDutyCycle(25)
        else:
            GPIO.output(self.pin_in1, True)
            GPIO.output(self.pin_in2, False)
            self.pwm.ChangeDutyCycle(100)

    def stop(self):
        print("track stop")
        GPIO.output(self.pin_in1, False)
        GPIO.output(self.pin_in2, False)
        self.pwm.ChangeDutyCycle(0)

    def speed_up(self):
        print("speed++")
        self.speed += 10
        if self.speed >= 100:
            self.speed = 100
        self.pwm.ChangeDutyCycle(self.speed)

    def speed_down(self):
        print("speed--")
        self.speed -= 10
        if self.speed < 0:
            self.speed = 0
            self.stop()
        else:
            self.pwm.ChangeDutyCycle(self.speed)

class Tank:
    def __init__(self):
        self.left_track = Track(L_PIN_ENABLE_A, L_PIN_IN1, L_PIN_IN2, is_inverted=True)
        self.right_track = Track(R_PIN_ENABLE_A, R_PIN_IN1, R_PIN_IN2, is_inverted=True)

    def status(self):
        return {
            'leftTrack': {
                'speed': self.left_track.speed
            },
            'rightTrack': {
                'speed': self.right_track.speed
            }
        }

    def cleanup(self):
        GPIO.cleanup()

    def left_track_forward(self):
        self.left_track.forward()

    def left_track_reverse(self):
        self.left_track.reverse()

    def left_track_stop(self):
        self.left_track.stop()

    def right_track_forward(self):
        self.right_track.forward()

    def right_track_reverse(self):
        self.right_track.reverse()

    def right_track_stop(self):
        self.right_track.stop()

    def forward(self):
        print("forward")
        self.left_track.forward()
        self.right_track.forward()

    def reverse(self):
        print("reverse")
        self.left_track.reverse()
        self.right_track.reverse()

    def stop(self):
        print("stop")
        self.left_track.stop()
        self.right_track.stop()

    def turn_left(self):
        print("turn left")
        self.left_track.stop()
        self.right_track.forward()

    def turn_right(self):
        print("turn right")
        self.left_track.forward()
        self.right_track.stop()

    def rotate_clockwise(self):
        print("rotate clockwise")
        self.left_track.forward()
        self.right_track.reverse()

    def rotate_counterclockwise(self):
        print("rotate counterclockwise")
        self.left_track.reverse()
        self.right_track.forward()

    def speed_up(self):
        print("speed++")
        self.left_track.speed_up()
        self.right_track.speed_up()

    def speed_down(self):
        print("speed--")
        self.left_track.speed_down()
        self.right_track.speed_down()

    def init_nrf24(self):
        pass
        # for NRF24
        # export GPIOZERO_PIN_FACTORY=PiGPIOPin
        # export PIGPIO_ADDR=192.168.4.76
        # sudo pigpiod -p8889
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
