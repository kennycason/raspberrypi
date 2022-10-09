import RPi.GPIO as GPIO
from time import sleep

photofracture = 18 #set photofracturePin
val = 0 #photofracture variables
count = 0 #Record the number of photofracture
flag = 0 #Odd even variable
GPIO.setmode(GPIO.BCM)  # use BCM numbers

GPIO.setup(photofracture,GPIO.IN) #set the photofracturePin INPUT mode

while True:
    val = GPIO.input(photofracture)  #Receive photofracture value
    #print("photofracture = %d"%(val))
    if(val == 0):   #if light is broken
        sleep(0.01)
        val = GPIO.input(photofracture)  #Receive photofracture value
        if(val == 1):  #light is not broken
            count = count + 1  #Count the number of light is broken
            print("count = %d" %count)
    
    flag = count % 2  #Remainder 2 ,Even is 0, odd is 1
        
GPIO.cleanup() #release all GPIO
