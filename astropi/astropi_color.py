from sense_hat import SenseHat
import random

sense = SenseHat()

random_color = (random.randrange(0, 256), random.randrange(0, 256), random.randrange(0, 256))
sense.clear(random_color)
sense.show_message("Hello world")