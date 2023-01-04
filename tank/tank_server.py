# Tank Flask Server
# export FLASK_APP=tank_server
# flask run -h 192.168.4.76 -p 8080
from flask import Flask
from flask_cors import CORS
from .tank import Tank

tank = Tank()
tank.stop()

app = Flask(__name__)
CORS(app)


@app.route('/tank/status', methods=['GET'])
def tank_status():
    return tank.status()


@app.route('/tank/forward', methods=['POST'])
def tank_forward():
    tank.forward()
    return ""


@app.route('/tank/reverse', methods=['POST'])
def tank_reverse():
    tank.reverse()
    return ""


@app.route('/tank/stop', methods=['POST'])
def tank_stop():
    tank.stop()
    return ""


@app.route('/tank/turn-left', methods=['POST'])
def tank_turn_left():
    tank.turn_left()
    return ""


@app.route('/tank/turn-right', methods=['POST'])
def tank_turn_right():
    tank.turn_right()
    return ""


@app.route('/tank/left-track-forward', methods=['POST'])
def tank_left_track_forward():
    tank.left_track_forward()
    return ""


@app.route('/tank/left-track-reverse', methods=['POST'])
def tank_left_track_reverse():
    tank.left_track_reverse()
    return ""


@app.route('/tank/right-track-forward', methods=['POST'])
def tank_right_track_forward():
    tank.right_track_forward()
    return ""


@app.route('/tank/right-track-reverse', methods=['POST'])
def tank_right_track_reverse():
    tank.right_track_reverse()
    return ""


@app.route('/tank/clockwise', methods=['POST'])
def tank_clockwise():
    tank.rotate_clockwise()
    return ""


@app.route('/tank/counter-clockwise', methods=['POST'])
def tank_rotate_counterclockwise():
    tank.rotate_counterclockwise()
    return ""


@app.route('/tank/speed-up', methods=['POST'])
def tank_speed_up():
    return tank.speed_up()


@app.route('/tank/speed-down', methods=['POST'])
def tank_speed_down():
    return tank.speed_down()


@app.route('/tank/speed/<speed>', methods=['POST'])
def tank_set_speed(speed: str):
    return tank.set_speed(int(speed))
