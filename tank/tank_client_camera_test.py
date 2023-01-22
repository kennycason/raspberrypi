import cv2
import subprocess as sp
import numpy as np

# Create a VideoCapture object
cap = cv2.VideoCapture()

# Set the video source to the IP address and port of the MJPEG stream
cap.open("tcp://192.168.4.76:8888", cv2.CAP_FFMPEG)


command_old = ['ffmpeg',
           # '-rtsp_transport', 'tcp',  # Force TCP (for testing)
           '-max_delay', '30000000',  # 30 seconds (sometimes needed because the stream is from the web).
           '-i', 'tcp://192.168.4.76:8888',
           '-f', 'rawvideo',  # Video format is raw video
           '-pix_fmt', 'bgr24',  # bgr24 pixel format matches OpenCV default pixels format.
           '-an', 'pipe:']

command = ['ffmpeg', '-i', 'tcp://192.168.4.76:8888',
     '-loglevel', 'quiet', '-f', 'image2pipe', '-pix_fmt', 'bgr24',
     '-vcodec', 'rawvideo', '-']

# Open sub-process that gets in_stream as input and uses stdout as an output PIPE.
ffmpeg_process = sp.Popen(command, stdout=sp.PIPE)
width = 640
height = 480

while True:
    # Read width*height*3 bytes from stdout (1 frame)
    raw_frame = ffmpeg_process.stdout.read(width * height * 3)
    print(len(raw_frame))

    if len(raw_frame) != (width * height * 3):
        print('Error reading frame!!!')  # Break the loop in case of an error (too few bytes were read).
        break

    # Convert the bytes read into a NumPy array, and reshape it to video frame dimensions
    frame = np.frombuffer(raw_frame, np.uint8).reshape((height, width, 3))

    # Show the video frame
    cv2.imshow('image', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

ffmpeg_process.stdout.close()  # Closing stdout terminates FFmpeg sub-process.
ffmpeg_process.wait()  # Wait for FFmpeg sub-process to finish

cv2.destroyAllWindows()