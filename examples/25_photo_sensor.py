import RPi.GPIO as GPIO
import smbus   
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

led = 5
GPIO.setup(led,GPIO.OUT)
 
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
    value = analogRead(0) ##read A0 data
    if(value<100):   #When the ambient brightness is less than 100, the LED light will be on
        GPIO.output(led,GPIO.LOW)
    else:
        GPIO.output(led,GPIO.HIGH)

    print("data:%1.0f" %(value))   ##print data
    
time.sleep(0.5)                ##delay 0.5 second
GPIO.cleanup()
