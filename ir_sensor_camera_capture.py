# run the if running from terminal/ssh
# export DISPLAY=:0

import RPi.GPIO as GPIO
import cv2
import time
from picamera2 import Picamera2

PIN_IN = 5                     # IR or Button

GPIO.setmode(GPIO.BCM)          # use BCM numbers
GPIO.setup(PIN_IN, GPIO.IN)     # set the PIN_IN INPUT mode


# Grab images as numpy arrays and leave everything else to OpenCV.
face_detector = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
cv2.startWindowThread()

picam2 = Picamera2()
picam2.configure(picam2.create_preview_configuration(main={"format": 'XRGB8888', "size": (640, 480)}))
picam2.start()

def capture_photo(i: int):
    image = picam2.capture_array()

    grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(grey, 1.1, 5)

    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0))

    cv2.imwrite("/tmp/ir_detected_" + str(i) + ".jpg", image)
    # cv2.imshow("Camera", image)

try:
    i = 0
    while True:
        ir = GPIO.input(PIN_IN)
        if ir:
            capture_photo(i)

        time.sleep(0.02)
        i += 1
finally:
    GPIO.cleanup()
