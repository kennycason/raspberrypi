import RPi.GPIO as GPIO
import time
import smbus

#pcf8591
address=0x48
cmd=0x40
A0=0x40##A0---->port address
A1=0x41
A2=0x42
A3=0x43
bus=smbus.SMBus(1)

#buzzer
buzPin = 18  #set buzPin to 18
GPIO.setmode(GPIO.BCM) # use BCM numbers
GPIO.setwarnings(False)
GPIO.setup(buzPin,GPIO.OUT)  #set buzPin OUTPUT mode

 
def main():
    while True:
        value = analogRead(0)
        print("MQ-2 = %s"%(value))
        time.sleep(0.01)

def analogRead(count):
    read_val=bus.read_byte_data(address,cmd+count)
    if(read_val > 60):
        GPIO.output(buzPin,GPIO.HIGH)  #Buzzer ring
    else:
        GPIO.output(buzPin,GPIO.LOW)  #Buzzer stop
    mq2_val = str(read_val)  # int to string
    return mq2_val

if __name__ == '__main__':
 
    try:
        main()
    except KeyboardInterrupt:
        pass
    finally:
        GPIO.cleanup()
