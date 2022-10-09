import RPi.GPIO as GPIO
from time import sleep

#active buzzer pin
buzPin = 16
#crash pin
crashPin = 18

GPIO.setmode(GPIO.BCM) # use BCM numbers
GPIO.setup(buzPin,GPIO.OUT)  #set buzPin OUTPUT mode
GPIO.setup(crashPin,GPIO.IN,GPIO.PUD_UP)  # set crashPin INPUT mode and crashPin to PULL UP

while True:
    val = GPIO.input(crashPin)
    print(val)
    if(val == 0): #Judge whether the metal shrapnel is pressed
        GPIO.output(buzPin,GPIO.HIGH)  #Buzzer ring
    else:
        GPIO.output(buzPin,GPIO.LOW)   #buzzer off
        
GPIO.cleanup() # Release all GPIO
