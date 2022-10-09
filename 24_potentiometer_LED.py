import RPi.GPIO as GPIO
import smbus
import time
address = 0x48 #default address of PCF8591
bus=smbus.SMBus(1)  #Create an instance of smbus
cmd=0x40 #command
# A0 = 0x40      ##A0  ----> port address
# A1 = 0x41
# A2 = 0x42
# A3 = 0x43

ledPin = 11
GPIO.setmode(GPIO.BCM)
GPIO.setup(ledPin,GPIO.OUT)
GPIO.output(ledPin,GPIO.LOW)
p = GPIO.PWM(ledPin,100)
p.start(0)

def analogRead(chn):   #read ADC value,chn:0,1,2,3
    value = bus.read_byte_data(address,cmd+chn)
    return value
 
def analogWrite(value):#write DAC value
    bus.write_byte_data(address,cmd,value) 

def loop():
    while True:
        value = analogRead(0) #read the ADC value ofchannel 0
        analogWrite(value) #write the DAC value
        p.ChangeDutyCycle(value*100/255) #Convert ADC value to duty cycle of PWM
        voltage = value / 255.0 * 3.3 #calculate the voltage value
        print ('ADC Value : %d, Voltage : %.2f'%(value,voltage))
        time.sleep(0.01)

def destroy():
    bus.close()
 
if __name__ == '__main__':
    print ('Program is starting ... ')
    try:
        loop()
    except KeyboardInterrupt:
        destroy()
