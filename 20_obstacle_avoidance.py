import RPi.GPIO as GPIO
from time import sleep

#active buzzer pin
buzPin = 27
#led pin
ledPin = 5
#obstacle avoidance pin
obstaclePin = 18

GPIO.setmode(GPIO.BCM) # use BCM numbers
GPIO.setup(buzPin,GPIO.OUT)  #set buzPin OUTPUT mode
GPIO.setup(ledPin,GPIO.OUT)  #set ledPin OUTPUT mode
GPIO.setup(obstaclePin,GPIO.IN)  # set obstacle avoidance Pin INPUT mode

while True:
    val = GPIO.input(obstaclePin)
    print(val)
    if(val == 0):  #Judge whether obstacle avoidance is detected
        GPIO.output(buzPin,GPIO.HIGH)  #Buzzer ring
        GPIO.output(ledPin,GPIO.HIGH)  #led on
        sleep(0.2)
        GPIO.output(ledPin,GPIO.LOW)  #led off
        sleep(0.1)
    else:
        GPIO.output(buzPin,GPIO.LOW)   #Buzzer off
        GPIO.output(ledPin,GPIO.LOW)  #led off
        
GPIO.cleanup() # Release all GPIO
