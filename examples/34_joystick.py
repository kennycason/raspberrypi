import RPi.GPIO as GPIO
import smbus   
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

key = 26  # joystic button pin
GPIO.setup(key,GPIO.IN)
 
address = 0x48 ##address  ---> device address
cmd = 0x40     ##DA converter command
A0 = 0x40      ##A0  ----> port address
A1 = 0x41
A2 = 0x42
A3 = 0x43
bus = smbus.SMBus(1)            ##start the bus

def analogRead(count):   #function,read analog data
    read_val = bus.read_byte_data(address,cmd+count)
    return read_val

while True:                     ##loop 
    #Vout = 10                  ##10*0.0196=0.196V
    #bus.write_byte_data(address,cmd,Vout) ##DA converter
    x_val = analogRead(0) ##read A0 data
    y_val = analogRead(1) #read A1 data
    print("x:%1.0f  y:%1.0f" %(x_val,y_val))          ##print data
    if GPIO.input(key):   
        print("The key is pressed")   


GPIO.cleanup()