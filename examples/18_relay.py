import RPi.GPIO as GPIO
from time import sleep

relayPin = 18   #define relay pin

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(relayPin,GPIO.OUT)

while True:
	GPIO.output(relayPin,GPIO.HIGH)  #Starting relay
	print("turn on")
	sleep(2)
	GPIO.output(relayPin,GPIO.LOW)  #Close relay
	print("turn off")
	sleep(1)

GPIO.cleanup()
