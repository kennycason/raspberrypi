# Tank Flask Server
# export FLASK_APP=tank_server
# flask run -h 192.168.4.76 -p 8080
from flask import Flask
from .tank import Tank

tank = Tank()
tank.stop()

app = Flask(__name__)


@app.route('/tank/forward')
def tank_forward():
    tank.forward()
    return ""


@app.route('/tank/reverse')
def tank_reverse():
    tank.reverse()
    return ""


@app.route('/tank/stop')
def tank_stop():
    tank.stop()
    return ""


@app.route('/tank/turn-left')
def tank_turn_left():
    tank.turn_left()
    return ""


@app.route('/tank/turn-right')
def tank_turn_right():
    tank.turn_right()
    return ""


@app.route('/tank/left-track-forward')
def tank_left_track_forward():
    tank.left_track_forward()
    return ""


@app.route('/tank/left-track-reverse')
def tank_left_track_reverse():
    tank.left_track_reverse()
    return ""


@app.route('/tank/right-track-forward')
def tank_right_track_forward():
    tank.right_track_forward()
    return ""


@app.route('/tank/right-track-reverse')
def tank_right_track_reverse():
    tank.right_track_reverse()
    return ""


@app.route('/tank/clockwise')
def tank_clockwise():
    tank.rotate_clockwise()
    return ""


@app.route('/tank/counter-clockwise')
def tank_rotate_counterclockwise():
    tank.rotate_counterclockwise()
    return ""
