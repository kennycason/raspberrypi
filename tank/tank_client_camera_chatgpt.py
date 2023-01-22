import cv2
import pygame
import numpy as np

pygame.init()

size = (640, 480)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Video Stream")

# Creating a video capture object
cap = cv2.VideoCapture('tcp://192.168.4.76:8888')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # Reading image from video capture object
    ret, frame = cap.read()

    if ret:
        # Convert the image from OpenCV format to Pygame format
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = np.rot90(frame)
        frame = pygame.surfarray.make_surface(frame)
        screen.blit(frame, (0,0))
        pygame.display.update()
    else:
        break

cap.release()
pygame.quit()