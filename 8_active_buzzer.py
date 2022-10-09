import RPi.GPIO as GPIO
from time import sleep

#active buzzer pin
buzPin = 16
#button pin
btnPin = 18

GPIO.setmode(GPIO.BCM) # use BCM numbers
GPIO.setup(buzPin,GPIO.OUT)  #set buzPin OUTPUT mode
GPIO.setup(btnPin,GPIO.IN,GPIO.PUD_UP)  # set btnPin INPUT mode and btnPin to PULL UP

while True:
    val = GPIO.input(btnPin)
    print(val)
    if(val == 0):  #Judge whether the button is pressed
        GPIO.output(buzPin,GPIO.HIGH)  #Buzzer ring
    else:
        GPIO.output(buzPin,GPIO.LOW)   #buzzer off
        
GPIO.cleanup() # Release all GPIO
