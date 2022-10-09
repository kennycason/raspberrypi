import RPi.GPIO as GPIO
import time

ledPin = 18  #define led pin

GPIO.setmode(GPIO.BCM)        # use BCM numbers
GPIO.setup(ledPin,GPIO.OUT)   #set the ledPin OUTPUT mode
GPIO.output(ledPin,GPIO.LOW)  # make ledPin output LOW level

while True:    #loop
    GPIO.output(ledPin,GPIO.HIGH)  #turn on led
    print("turned on the led")  #Print in the terminal

GPIO.cleanup()    #release all GPIO
