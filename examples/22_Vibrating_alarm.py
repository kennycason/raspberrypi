import RPi.GPIO as GPIO

buzPin = 5    # pin5 --- buzeer
vibPin = 18    # pin18 --- vibration sensor

buz_status = 0
def setup():
	GPIO.setmode(GPIO.BCM)  # use BCM numbers
	GPIO.setwarnings(False)
	GPIO.setup(buzPin,GPIO.OUT)   # Set buzPin's mode is output
	GPIO.setup(vibPin,GPIO.IN,pull_up_down=GPIO.PUD_UP)    # Set vibPin's mode is input, and pull up to high level(3.3V)

def swbuz(ev=None):
	global buz_status
	buz_status = not buz_status
	GPIO.output(buzPin, buz_status)  # switch buz status(ring-->off; off-->ring)
	if buz_status == 1:
		print 'buzzer ring...'
	else:
		print '...buzzer off'

def loop():
	GPIO.add_event_detect(vibPin, GPIO.FALLING, callback=swbuz) # wait for falling
	while True:
		pass   # Don't do anything

def destroy():
	GPIO.output(buzPin, GPIO.LOW)     # buzzer off
	GPIO.cleanup()                     # Release resource

if __name__ == '__main__':     # Program start from here
	setup()
	try:
		loop()
	except KeyboardInterrupt:  
		destroy()
