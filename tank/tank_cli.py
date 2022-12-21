# Run Tank CLI
import time
from tank import Tank


# ↖  ↑  ↗   1 speed--
#   QWE     2 speed++
# ← ASD →   H clockwise
#   ZXC     J counterclockwise
# ↙  ↓  ↘　
class TankCli:
    def __init__(self):
        self.tank = Tank()
        self.tank.stop()

    def handle_input(self):
        cmd = input()
        if cmd == 'q':
            self.tank.left_track_forward()
        elif cmd == 'w':
            self.tank.forward()
        elif cmd == 'e':
            self.tank.right_track_forward()

        elif cmd == 'a':
            self.tank.turn_left()
        elif cmd == 's':
            self.tank.stop()
        elif cmd == 'd':
            self.tank.turn_right()

        elif cmd == 'z':
            self.tank.left_track_reverse()
        elif cmd == 'x':
            self.tank.reverse()
        elif cmd == 'c':
            self.tank.right_track_reverse()

        if cmd == 'h':
            self.tank.rotate_clockwise()
        elif cmd == 'j':
            self.tank.rotate_counterclockwise()

        elif cmd == '1':
            self.tank.speed_up()
        elif cmd == '2':
            self.tank.speed_down()

    def start(self):
        try:
            while True:
                self.handle_input()
                time.sleep(0.02)
        finally:
            self.tank.cleanup()


tank_cli = TankCli()
tank_cli.start()
