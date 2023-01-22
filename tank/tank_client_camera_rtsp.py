import cv2

# raspivid -o - -t 0 -w 800 -h 600 -fps 12 | cvlc -vvv stream:///dev/stdin --sout '#rtp{sdp=rtsp://:8081/output.h264}' :demux=h264
# raspivid -o - -t 0 -w 800 -h 600 -fps 30  | cvlc -vvv stream:///dev/stdin --sout '#rtp{sdp=rtsp://:8081/}' :demux=h264
# ffplay -probesize 32 -analyzeduration 0 -fflags nobuffer -fflags flush_packets -flags low_delay  -framedrop rtsp://192.168.4.76:8081/

face_detector = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
cv2.startWindowThread()

cap = cv2.VideoCapture("rtsp://spider.local:8081/")
i = 0
while True:
    ret, frame = cap.read()
    if ret:
        # print(frame)
        grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_detector.detectMultiScale(grey, 1.1, 5)

        if len(faces) > 0:
            print("detected face")
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0))

        # cv2.imwrite("/tmp/face_detect_" + str(i) + ".jpg", frame)

        cv2.imshow('VIDEO', frame)
        cv2.waitKey(1)
    i += 1


# Release the VideoCapture object
cap.release()

# Close all open windows
cv2.destroyAllWindows()
