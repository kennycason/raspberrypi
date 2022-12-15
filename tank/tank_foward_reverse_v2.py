import RPi.GPIO as GPIO
from time import sleep

rin1 = 24
rin2 = 23
ren = 25

lin1 = 24
lin2 = 20
len = 16

temp1 = 1

GPIO.setmode(GPIO.BCM)
GPIO.setup(rin1, GPIO.OUT)
GPIO.setup(rin2, GPIO.OUT)
GPIO.setup(ren, GPIO.OUT)
GPIO.output(rin1, GPIO.LOW)
GPIO.output(rin2, GPIO.LOW)
rp = GPIO.PWM(ren, 1000)
rp.start(25)

GPIO.setmode(GPIO.BCM)
GPIO.setup(lin1, GPIO.OUT)
GPIO.setup(lin2, GPIO.OUT)
GPIO.setup(len, GPIO.OUT)
GPIO.output(lin1, GPIO.LOW)
GPIO.output(lin2, GPIO.LOW)
lp = GPIO.PWM(len, 1000)
lp.start(25)

print("\n")
print("The default speed & direction of motor is LOW & Forward.....")
print("r-run s-stop f-forward b-backward l-low m-medium h-high e-exit")
print("\n")

while (1):

    x = input()

    if x == 'r':
        print("run")
        if (temp1 == 1):
            GPIO.output(rin1, GPIO.HIGH)
            GPIO.output(rin2, GPIO.LOW)

            GPIO.output(lin1, GPIO.LOW)
            GPIO.output(lin2, GPIO.HIGH)
            print("forward")
            x = 'z'
        else:
            GPIO.output(rin1, GPIO.LOW)
            GPIO.output(rin2, GPIO.HIGH)

            GPIO.output(lin1, GPIO.HIGH)
            GPIO.output(lin2, GPIO.LOW)
            print("backward")
            x = 'z'


    elif x == 's':
        print("stop")
        GPIO.output(rin1, GPIO.LOW)
        GPIO.output(rin2, GPIO.LOW)
        GPIO.output(lin1, GPIO.LOW)
        GPIO.output(lin2, GPIO.LOW)
        x = 'z'

    elif x == 'f':
        print("forward")
        GPIO.output(rin1, GPIO.HIGH)
        GPIO.output(rin2, GPIO.LOW)
        GPIO.output(lin1, GPIO.LOW)
        GPIO.output(lin2, GPIO.HIGH)
        temp1 = 1
        x = 'z'

    elif x == 'b':
        print("backward")
        GPIO.output(rin1, GPIO.LOW)
        GPIO.output(rin2, GPIO.HIGH)
        GPIO.output(lin1, GPIO.HIGH)
        GPIO.output(lin2, GPIO.LOW)
        temp1 = 0
        x = 'z'

    elif x == 'l':
        print("low")
        rp.ChangeDutyCycle(25)
        lp.ChangeDutyCycle(25)
        x = 'z'

    elif x == 'm':
        print("medium")
        rp.ChangeDutyCycle(50)
        lp.ChangeDutyCycle(50)
        x = 'z'

    elif x == 'h':
        print("high")
        rp.ChangeDutyCycle(75)
        lp.ChangeDutyCycle(75)
        x = 'z'


    elif x == 'e':
        GPIO.cleanup()
        break

    else:
        print("<<<  wrong data  >>>")
        print("please enter the defined data to continue.....")