import RPi.GPIO as GPIO
from time import sleep

#led pin
ledPin = 27
#tracking pin
trackingPin = 18

GPIO.setmode(GPIO.BCM) # use BCM numbers
GPIO.setup(ledPin,GPIO.OUT)  #set ledPin OUTPUT mode
GPIO.setup(trackingPin,GPIO.IN)  # set trackingPin INPUT mode

while True:
    val = GPIO.input(trackingPin)
    print(val)
    if(val == 0):  #Judge whether the white line is detected
        GPIO.output(ledPin,GPIO.HIGH)  #led on
    else:
        GPIO.output(ledPin,GPIO.LOW)   #led off
        
GPIO.cleanup() # Release all GPIO
