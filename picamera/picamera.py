#!/usr/bin/python3

# run the if running from terminal/ssh
# export DISPLAY=:0
from time import sleep

from picamera2 import Picamera2

picam2 = Picamera2()
picam2.configure(picam2.create_preview_configuration(main={"format": 'XRGB8888', "size": (640, 480)}))
picam2.start()

i = 0
while True:
    image = picam2.capture_array()
    # cv2.imwrite("/tmp/camera" + str(i) + ".jpg", image)
    cv2.imshow("Camera", image)
    sleep(1)
    i += 1
