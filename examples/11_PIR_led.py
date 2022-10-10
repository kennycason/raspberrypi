import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

ledPin = 5  #set led pin
pirPin = 18  #set PYE-IR pin
GPIO.setup(ledPin,GPIO.OUT)
GPIO.setup(pirPin,GPIO.IN)
 

while True:                     ##loop 
    if GPIO.input(pirPin):    #When someone is detected
        GPIO.output(ledPin,GPIO.HIGH)  #turn on the led
        print("somebody")
    else:
        GPIO.output(ledPin,GPIO.LOW)  #turn off led
        print("nobody")
    
GPIO.cleanup()
