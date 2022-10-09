import RPi.GPIO as GPIO
from time import sleep

#define led pin
led1Pin = 17
led2Pin = 27
#define Ball Tilt Sensor Pin
tiltPin = 18


GPIO.setmode(GPIO.BCM) #use BCM unmbers
GPIO.setup(led1Pin,GPIO.OUT)  #set the ledPin OUTPUT mode
GPIO.setup(led2Pin,GPIO.OUT)
GPIO.output(led1Pin,GPIO.HIGH)  # make ledPin output HIGH level
GPIO.output(led2Pin,GPIO.LOW)  # make ledPin output LOW level
GPIO.setup(tiltPin,GPIO.IN,GPIO.PUD_UP)
pwm1 = GPIO.PWM(led1Pin,1000)  #create a pwm1 instance
pwm1.start(0)  #start pwm1
pwm2 = GPIO.PWM(led2Pin,1000)  #create a pwm2 instance
pwm2.start(0)  #start pwm2
val1 = 50
val2 = 50

while True:
    if not GPIO.input(tiltPin):
        val1 = val1 + 1
        val2 = val2 - 1
        if (val1 >= 100):  #Limit PWM value to no more than 100
            val1 = 100
        if (val2 < 0):    #Limit PWM value not less than 0
            val2 = 0
        print("led1 = %1.0f" %(val1))
        pwm1.ChangeDutyCycle(val1)  #change the frequency
        pwm2.ChangeDutyCycle(val2)
        sleep(0.1)
    else:
        val1 = val1 - 1
        val2 = val2 + 1
        if (val1 < 0):
            val1 = 0
        if (val2 >= 100):
            val2 = 100
        print("led2 = %1.0f" %(val2))
        pwm1.ChangeDutyCycle(val1)
        pwm2.ChangeDutyCycle(val2)
        sleep(0.1)
        
pwm1.stop()  #stop pwm1

GPIO.cleanup()    #release all GPIO
