import RPi.GPIO as GPIO
import time

ledPin = 18  #define led pin
i1 = 0
i2 = 0
i3 = 0

GPIO.setmode(GPIO.BCM)        # use BCM numbers
GPIO.setup(ledPin,GPIO.OUT)   #set the ledPin OUTPUT mode
GPIO.output(ledPin,GPIO.LOW)  # make ledPin output LOW level

while True:    #loop
    while(i1<3):
        GPIO.output(ledPin,GPIO.HIGH)  #turn on led
        time.sleep(0.1)              #wait for 1 second
        GPIO.output(ledPin,GPIO.LOW)   #turn off led
        time.sleep(0.1)
        print(".")
        i1 += 1
    
    while(i2<3):
        GPIO.output(ledPin,GPIO.HIGH)  #turn on led
        time.sleep(1)              #wait for 1 second
        GPIO.output(ledPin,GPIO.LOW)   #turn off led
        time.sleep(1)
        print("_")
        i2 += 1
    
    while(i3<3):
        GPIO.output(ledPin,GPIO.HIGH)  #turn on led
        time.sleep(0.1)              #wait for 1 second
        GPIO.output(ledPin,GPIO.LOW)   #turn off led
        time.sleep(0.1)
        print(".")
        i3 += 1
    time.sleep(3)
    i1 = 0
    i2 = 0
    i3 = 0
    

GPIO.cleanup()    #release all GPIO