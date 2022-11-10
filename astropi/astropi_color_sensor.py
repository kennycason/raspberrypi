from sense_hat import SenseHat
from time import sleep

# only works on v2
sense = SenseHat()
sense.color.gain = 60
sense.color.integration_cycles = 64

while True:
    sleep(2 * sense.color.integration_time)
    red, green, blue, clear = sense.color.colour # readings scaled to 0-256
    print(f"R: {red}, G: {green}, B: {blue}, C: {clear}")