import RPi.GPIO as GPIO
import time
 
GPIO.setmode(GPIO.BCM)
  
#define GPIO pin
GPIO_TRIGGER = 23
GPIO_ECHO = 24
  
#set GPIO mode (IN / OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

def distance():
    # 10us is the trigger signal
    GPIO.output(GPIO_TRIGGER, True)
    time.sleep(0.00001)  #10us
    GPIO.output(GPIO_TRIGGER, False)
    
    start_time = time.time()
    stop_time = time.time()
    
    while GPIO.input(GPIO_ECHO) == 0:   #Indicates that the ultrasonic wave has been emitted
        start_time = time.time()  #Record launch time
  
    while GPIO.input(GPIO_ECHO) == 1:   #Indicates that the returned ultrasound has been received
        stop_time = time.time()   #Record receiving time
  
    time_elapsed = stop_time - start_time  #Time difference from transmit to receive
    distance = (time_elapsed * 34300) / 2  #Calculate the distance
    return distance   #Return to calculated distance
  
if __name__ == '__main__':   #Program entry
    try:
        while True:  
            dist = distance()  #
            print("Measured Distance = {:.2f} cm".format(dist)) #{:.2f},Keep two decimal places
            time.sleep(0.1)
  
        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()
