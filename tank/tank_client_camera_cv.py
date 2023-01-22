import pygame
import cv2
import numpy as np

pygame.init()

size = (640, 480)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Tank Camera")
# cap = cv2.VideoCapture('tcp://192.168.4.76:8888')
cap = cv2.VideoCapture("rtsp://spider.local:8081/")

class TankClientCamera:

    def __init__(self):
        pass

    def start(self):
        running = True
        while running:
            print("running")
            ret, frame = cap.read()
            if ret:
                print("capture success")
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                frame = np.rot90(frame)
                frame = pygame.surfarray.make_surface(frame)
                screen.blit(frame, (0, 0))
                pygame.display.update()
            else:
                print("Image is null")
                # running = False

        cap.release()
        pygame.quit()


tank_client_camera = TankClientCamera()
tank_client_camera.start()
