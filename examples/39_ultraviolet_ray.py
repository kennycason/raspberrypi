import RPi.GPIO as GPIO
import smbus
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
 
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
    value = analogRead(0) ##read A0 data
    print("ultraviolet intensity:%1.0f" %(value))   ##print data
    time.sleep(0.05)                ##delay 0.05 second
    
GPIO.cleanup()
