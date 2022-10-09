import RPi.GPIO as GPIO
import time

servo_min_angle = 2.5  #define pulse duty cycle for minimun angle of servo
servo_max_angle = 12.5  #define pulse duty cycle for maximun angle of servo

servopin = 18   #servo Pin
GPIO.setmode(GPIO.BCM)  #BCM numbers

GPIO.setup(servopin,GPIO.OUT)
p = GPIO.PWM(servopin,50)  #set 50Hz , The working frequency of the steering gear is 50Hz
p.start(0)  # start PWM
time.sleep(2)

#define function, map a value from one range to another range
def map(angle, val1, val2, min_angle, max_angle):
    return (max_angle-min_angle)*(angle-val1)/(val2-val1)+min_angle

while(True):  #loop
    p.ChangeDutyCycle(0)   #set 
    time.sleep(0.4)
    b = input("input Angle:")
    b = int(b)
    c = map(b, 0, 180, servo_min_angle, servo_max_angle)  #map angle from 0~180 to 2.5~12.5
    p.ChangeDutyCycle(c) 
    time.sleep(0.4)
    
p.stop()
GPIO.cleanup()

