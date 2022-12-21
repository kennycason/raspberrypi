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
    return "forward"


@app.route('/tank/reverse')
def tank_reverse():
    tank.reverse()
    return "reverse"


@app.route('/tank/stop')
def tank_stop():
    tank.stop()
    return "stop"


@app.route('/tank/clockwise')
def tank_clockwise():
    tank.rotate_clockwise()
    return "clockwise"


@app.route('/tank/counter-clockwise')
def tank_rotate_counterclockwise():
    tank.rotate_counterclockwise()
    return "counter-clockwise"

