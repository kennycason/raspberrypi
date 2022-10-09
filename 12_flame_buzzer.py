import RPi.GPIO as GPIO
from time import sleep

#define buzzer pin
buzPin = 16
#define flame Pin
flamePin = 18

val = 0  #

GPIO.setmode(GPIO.BCM) #use BCM numbers
GPIO.setup(buzPin,GPIO.OUT)  #set the buzPin OUTPUT
GPIO.setup(flamePin,GPIO.IN,GPIO.PUD_UP) #set the flamePin INPUT

while True:
    val = GPIO.input(flamePin) #Receives the value of the flame sensor
    print("val = %d" %val)
    if (val == 0):  #When flame is detected
        GPIO.output(buzPin,GPIO.HIGH)  #Buzzer turn on
    else:
        GPIO.output(buzPin,GPIO.LOW)   #buzzer turn off
        
GPIO.cleanup() # Release all GPIO
