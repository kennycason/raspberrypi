import RPi.GPIO as GPIO
from time import sleep
import random

#define RGB pin
pin_R = 24
pin_G = 23
pin_B = 18
GPIO.setmode(GPIO.BCM)  # use BCM numbers
#set the RGB Pin OUTPUT mode
GPIO.setup(pin_R,GPIO.OUT)
GPIO.setup(pin_G,GPIO.OUT)
GPIO.setup(pin_B,GPIO.OUT)

# makeRGB Pin output LOW level
GPIO.output(pin_R,GPIO.LOW)
GPIO.output(pin_G,GPIO.LOW)
GPIO.output(pin_B,GPIO.LOW)

#set pwm frequence to 1000hz
pwm_R = GPIO.PWM(pin_R,100)
pwm_G = GPIO.PWM(pin_G,100)
pwm_B = GPIO.PWM(pin_B,100)
#set inital duty cycle to 0
pwm_R.start(0)
pwm_G.start(0)
pwm_B.start(0)

#function. receive the value to display different colors
def setColor(val_R,val_G,val_B):
    pwm_R.ChangeDutyCycle(val_R)
    pwm_G.ChangeDutyCycle(val_G)
    pwm_B.ChangeDutyCycle(val_B)

while True:
    # get a random in 0~100
    R = random.randint(0,100)
    G = random.randint(0,100)
    B = random.randint(0,100)
    setColor(R,G,B)  #set the color value
    print('Red=%d, Green = %d, Blue = %d' %(R, G, B))
    sleep(0.2)
    
#stop pwm
pwm_R.stop()
pwm_G.stop()
pwm_B.stop()

GPIO.cleanup()  #release all GPIO
