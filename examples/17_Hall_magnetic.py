import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

ledPin = 5  #set led pin
hallPin = 18  #set hall magnetic pin
GPIO.setup(ledPin,GPIO.OUT)
GPIO.setup(hallPin,GPIO.IN)
 

while True:                     ##loop 
    if GPIO.input(hallPin):    #When Magnetic is not detected
        GPIO.output(ledPin,GPIO.LOW)  #turn off the led
        print("nonmagnetic")
    else:
        GPIO.output(ledPin,GPIO.HIGH)  #turn on the led
        print("magnetic")
    
GPIO.cleanup()
