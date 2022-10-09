import RPi.GPIO as GPIO
import smbus 
import math  
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
 
address = 0x48 ##address  ---> device address
cmd = 0x40     ##DA converter command
A0 = 0x40      ##A0  ----> port address
A1 = 0x41
A2 = 0x42
A3 = 0x43
bus = smbus.SMBus(0)            ##start the bus
time.sleep(1)

def analogRead(count):   #function,read analog data
    read_val = bus.read_byte_data(address,cmd+count)
    return read_val

while True:                     ##loop 
    value = analogRead(0)        # read ADC value A0 pin
    voltage = value / 255.0 * 5.0        # calculate voltage
    Rt = 4.7 * (5.0 / voltage) - 4.7 ;   #calculate resistance value of thermistor, 5.0*(R/(Rt+R))=voltage,>>>Rt=R*(5.0/voltage)-R
    tempK = 1/(1/(273.15 + 25) + math.log(Rt/4.7)/3950.0)  # calculate temperature (Kelvin)
    tempC = tempK - 273.15       # calculate temperature (Celsius)
    print ('ADC Value : %d, Voltage : %.2f, Temperature : %.2f'%(value,voltage,tempC))

time.sleep(0.02)
GPIO.cleanup()

