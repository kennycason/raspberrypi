import pygame
import cv2
import subprocess as sp
import numpy as np

pygame.init()

class TankClientCamera:

    def __init__(self):
        self.screen = pygame.display.set_mode((640, 480))
        pygame.display.set_caption("Tank Camera")
        self.pipe = sp.Popen(['ffmpeg', '-i', 'tcp://192.168.4.76:8888', '-loglevel', 'quiet', '-f', 'image2pipe', '-pix_fmt', 'bgr24', '-vcodec', 'rawvideo', '-'], stdout = sp.PIPE, bufsize=10**8)

    def start(self):
        running = True
        while running:
            try:
                raw_image = self.pipe.stdout.read(640 * 480 * 3)
                print(raw_image)
                image = np.fromstring(raw_image, dtype='uint8').reshape((480, 640, 3))
                if image is not None:
                    frame = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                    frame = np.rot90(frame)
                    frame = pygame.surfarray.make_surface(frame)
                    self.screen.blit(frame, (0, 0))
                    pygame.display.update()
                else:
                    print("Image is null")
                    running = False

            except:
                print("Error happened reading camera frame")
                running = False

        pygame.quit()


tank_client_camera = TankClientCamera()
tank_client_camera.start()
