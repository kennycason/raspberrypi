#!/usr/bin/python3

# run the if running from terminal/ssh
# export DISPLAY=:0
import cv2
from time import sleep

from picamera2 import Picamera2

# Grab images as numpy arrays and leave everything else to OpenCV.
face_detector = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
cv2.startWindowThread()

picam2 = Picamera2()
picam2.configure(picam2.create_preview_configuration(main={"format": 'XRGB8888', "size": (640, 480)}))
picam2.start()

i = 0
while True:
    image = picam2.capture_array()

    grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(grey, 1.1, 5)

    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0))

    cv2.imwrite("/tmp/camera" + str(i) + ".jpg", image)
    # cv2.imshow("Camera", image)
    sleep(1)
    i += 1
