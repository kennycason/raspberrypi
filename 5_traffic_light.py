import RPi.GPIO as GPIO
from time import sleep

#LED pin
R = 18
Y = 23
G = 24

GPIO.setmode(GPIO.BCM)  # use BCM numbers
GPIO.setup(R,GPIO.OUT)  #set the ledPin OUTPUT mode
GPIO.setup(Y,GPIO.OUT)
GPIO.setup(G,GPIO.OUT)

GPIO.output(R,GPIO.LOW)
GPIO.output(Y,GPIO.LOW)
GPIO.output(G,GPIO.LOW)

while True:
    GPIO.output(R,GPIO.HIGH)
    sleep(5)
    GPIO.output(R,GPIO.LOW)
    
    GPIO.output(Y,GPIO.HIGH) #turn on yellow_led
    sleep(0.5)
    GPIO.output(Y,GPIO.LOW) #turn off yellow_led
    sleep(0.5)
    GPIO.output(Y,GPIO.HIGH)
    sleep(0.5)
    GPIO.output(Y,GPIO.LOW) 
    sleep(0.5)
    GPIO.output(Y,GPIO.HIGH) 
    sleep(0.5)
    GPIO.output(Y,GPIO.LOW) 
    sleep(0.5)
    
    GPIO.output(G,GPIO.HIGH)  #turn on green_led
    sleep(5)     #delay 5s
    GPIO.output(G,GPIO.LOW)   #turn off green_led
    
    
GPIO.cleanup()   #release all GPIO
