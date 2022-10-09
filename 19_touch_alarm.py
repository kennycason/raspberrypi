import RPi.GPIO as GPIO
from time import sleep

#active buzzer
buzPin = 27
#touch pin
touchPin = 18

GPIO.setmode(GPIO.BCM) # use BCM numbers
GPIO.setup(buzPin,GPIO.OUT)  #set buzPin OUTPUT mode
GPIO.setup(touchPin,GPIO.IN)  # set touchPin INPUT mode

while True:
    val = GPIO.input(touchPin)
    print(val)
    if(val == 1):  #Judge whether the touch area is touched
        GPIO.output(buzPin,GPIO.HIGH)  #Buzzer ring
    else:
        GPIO.output(buzPin,GPIO.LOW)   #Buzzer off
        
GPIO.cleanup() # Release all GPIO
