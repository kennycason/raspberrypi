from sense_hat import SenseHat
import random

sense = SenseHat()

while True:
    random_color = (random.randrange(0, 256), random.randrange(0, 256), random.randrange(0, 256))
    sense.show_message("*", text_colour=random_color)