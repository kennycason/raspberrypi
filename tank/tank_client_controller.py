from enum import Enum

import pygame
import requests
import os
os.environ["SDL_JOYSTICK_ALLOW_BACKGROUND_EVENTS"] = "1"

pygame.init()
pygame.event.set_grab(True)

API_URL = "http://spider.local:8080{}"

class Direction(Enum):
    FORWARD = 1
    NEUTRAL = 2
    REVERSE = 3


class TankClientController:

    def __init__(self):
        self.left_track_direction = Direction.NEUTRAL
        self.right_track_direction = Direction.NEUTRAL

    def start(self):
        requests.post(API_URL.format("/tank/stop"))
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            joystick_count = pygame.joystick.get_count()
            if joystick_count == 0:
                print("No joysticks connected")
            else:
                joystick = pygame.joystick.Joystick(0)
                joystick.init()

                left_joystick_x = joystick.get_axis(0)
                left_joystick_y = joystick.get_axis(1)

                right_joystick_x = joystick.get_axis(3)
                right_joystick_y = joystick.get_axis(4)

                print("L({}, {}), R({}, {})".format(left_joystick_x, left_joystick_y, right_joystick_x, right_joystick_y))

                if left_joystick_y < -0.9:
                    if self.left_track_direction != Direction.FORWARD:
                        self.left_track_direction = Direction.FORWARD
                        requests.post(API_URL.format("/tank/left-track/forward"))

                elif left_joystick_y > 0.9:
                    if self.left_track_direction != Direction.REVERSE:
                        self.left_track_direction = Direction.REVERSE
                        requests.post(API_URL.format("/tank/left-track/reverse"))
                else:
                    if self.left_track_direction != Direction.NEUTRAL:
                        self.left_track_direction = Direction.NEUTRAL
                        requests.post(API_URL.format("/tank/left-track/stop"))

                if right_joystick_y < -0.9:
                    if self.right_track_direction != Direction.FORWARD:
                        self.right_track_direction = Direction.FORWARD
                        requests.post(API_URL.format("/tank/right-track/forward"))

                elif right_joystick_y > 0.9:
                    if self.right_track_direction != Direction.REVERSE:
                        self.right_track_direction = Direction.REVERSE
                        requests.post(API_URL.format("/tank/right-track/reverse"))
                else:
                    if self.right_track_direction != Direction.NEUTRAL:
                        self.right_track_direction = Direction.NEUTRAL
                        requests.post(API_URL.format("/tank/right-track/stop"))

        pygame.quit()


tank_client_controller = TankClientController()
tank_client_controller.start()