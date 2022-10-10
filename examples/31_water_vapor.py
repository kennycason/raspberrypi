import RPi.GPIO as GPIO
import time
import smbus

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)       # Use BCM GPIO numbers

address = 0x48 ##address--->device address
cmd = 0x40
A0 = 0x40    ##A0---->port address
A1 = 0x41
A2 = 0x42
A3 = 0x43
bus = smbus.SMBus(1) 

def analogRead(count):   #function,read analog data
    read_val = bus.read_byte_data(address,cmd+count)
    return read_val

while True:
    value = analogRead(0)   ##read A0 data
    print("water content = %s"%(value))    ##print data
    time.sleep(0.1);   ##delay 0.5 second
    
GPIO.cleanup()
