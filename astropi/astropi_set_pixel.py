from sense_hat import SenseHat
import random

sense = SenseHat()

while True:
    random_color = (random.randrange(0, 256), random.randrange(0, 256), random.randrange(0, 256))
    sense.set_pixel(2, 2, random_color)
    sense.set_pixel(4, 2, random_color)
    sense.set_pixel(3, 4, random_color)
    sense.set_pixel(1, 5, random_color)
    sense.set_pixel(2, 6, random_color)
    sense.set_pixel(3, 6, random_color)
    sense.set_pixel(4, 6, random_color)
    sense.set_pixel(5, 5, random_color)