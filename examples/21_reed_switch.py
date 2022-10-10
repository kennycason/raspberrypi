import RPi.GPIO as GPIO
from time import sleep

#led pin
ledPin = 5
#reed switch pin
reedPin = 18

GPIO.setmode(GPIO.BCM) # use BCM numbers
GPIO.setup(ledPin,GPIO.OUT)  #set ledPin OUTPUT mode
GPIO.setup(reedPin,GPIO.IN)  # set reed switch Pin INPUT mode

while True:
    val = GPIO.input(reedPin)
    print(val)
    if(val == 0):  #Judge whether magnetism is detected
        GPIO.output(ledPin,GPIO.HIGH)  #led on
    else:
        GPIO.output(ledPin,GPIO.LOW)  #led off
        
GPIO.cleanup() # Release all GPIO
