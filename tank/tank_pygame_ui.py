from enum import Enum

import pygame
import requests

pygame.init()

screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Controller Test")

api_url = "http://spider.local:8080{}"


class Direction(Enum):
    FORWARD = 1
    NEUTRAL = 2
    REVERSE = 3


class TankPygameUI:

    def __init__(self):
        self.left_track_direction = Direction.NEUTRAL
        self.right_track_direction = Direction.NEUTRAL
        pass

    def start(self):
        requests.post(api_url.format("/tank/stop"))
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
                        requests.post(api_url.format("/tank/left-track/forward"))

                elif left_joystick_y > 0.9:
                    if self.left_track_direction != Direction.REVERSE:
                        self.left_track_direction = Direction.REVERSE
                        requests.post(api_url.format("/tank/left-track/reverse"))
                else:
                    if self.left_track_direction != Direction.NEUTRAL:
                        self.left_track_direction = Direction.NEUTRAL
                        requests.post(api_url.format("/tank/left-track/stop"))

                if right_joystick_y < -0.9:
                    if self.right_track_direction != Direction.FORWARD:
                        self.right_track_direction = Direction.FORWARD
                        requests.post(api_url.format("/tank/right-track/forward"))

                elif right_joystick_y > 0.9:
                    if self.right_track_direction != Direction.REVERSE:
                        self.right_track_direction = Direction.REVERSE
                        requests.post(api_url.format("/tank/right-track/reverse"))
                else:
                    if self.right_track_direction != Direction.NEUTRAL:
                        self.right_track_direction = Direction.NEUTRAL
                        requests.post(api_url.format("/tank/right-track/stop"))

        pygame.quit()



tank_joystick = TankPygameUI()
tank_joystick.start()

#
# @app.route('/tank/status', methods=['GET'])
# def tank_status():
#     return tank.status()
#
#
# @app.route('/tank/forward', methods=['POST'])
# def tank_forward():
#     tank.forward()
#     return ""
#
#
# @app.route('/tank/reverse', methods=['POST'])
# def tank_reverse():
#     tank.reverse()
#     return ""
#
#
# @app.route('/tank/stop', methods=['POST'])
# def tank_stop():
#     tank.stop()
#     return ""
#
#
# @app.route('/tank/turn-left', methods=['POST'])
# def tank_turn_left():
#     tank.turn_left()
#     return ""
#
#
# @app.route('/tank/turn-right', methods=['POST'])
# def tank_turn_right():
#     tank.turn_right()
#     return ""
#
#
# @app.route('/tank/left-track-forward', methods=['POST'])
# def tank_left_track_forward():
#     tank.left_track_forward()
#     return ""
#
#
# @app.route('/tank/left-track-reverse', methods=['POST'])
# def tank_left_track_reverse():
#     tank.left_track_reverse()
#     return ""
#
#
# @app.route('/tank/right-track-forward', methods=['POST'])
# def tank_right_track_forward():
#     tank.right_track_forward()
#     return ""
#
#
# @app.route('/tank/right-track-reverse', methods=['POST'])
# def tank_right_track_reverse():
#     tank.right_track_reverse()
#     return ""
#
#
# @app.route('/tank/clockwise', methods=['POST'])
# def tank_clockwise():
#     tank.rotate_clockwise()
#     return ""
#
#
# @app.route('/tank/counter-clockwise', methods=['POST'])
# def tank_rotate_counterclockwise():
#     tank.rotate_counterclockwise()
#     return ""
#
#
# @app.route('/tank/speed-up', methods=['POST'])
# def tank_speed_up():
#     return tank.speed_up()
#
#
# @app.route('/tank/speed-down', methods=['POST'])
# def tank_speed_down():
#     return tank.speed_down()
#
#
# @app.route('/tank/speed/<speed>', methods=['POST'])
# def tank_set_speed(speed: str):
#     return tank.set_speed(int(speed))
