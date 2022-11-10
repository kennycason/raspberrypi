from sense_hat import SenseHat
sense = SenseHat()


while True:
    for event in sense.stick.get_events():
        print(event.direction, event.action)

# output
# right pressed
# right held
# right held
# right released
# down pressed
# down held
# down held
# down released
# left pressed
# left released
# up pressed
# up released