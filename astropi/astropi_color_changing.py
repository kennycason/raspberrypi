from sense_hat import SenseHat
import random
import time

sense = SenseHat()

text_colour = (random.randrange(0, 256), random.randrange(0, 256), random.randrange(0, 256))
back_colour = (random.randrange(0, 256), random.randrange(0, 256), random.randrange(0, 256))

while True:
    sense.show_message("Spider Bot is alive!", text_colour=text_colour, back_colour=back_colour, scroll_speed=0.05)
    time.sleep(1)
    text_colour = (random.randrange(0, 256), random.randrange(0, 256), random.randrange(0, 256))
    back_colour = (random.randrange(0, 256), random.randrange(0, 256), random.randrange(0, 256))