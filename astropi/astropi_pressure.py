from sense_hat import SenseHat

sense = SenseHat()
sense.clear()

pressure = sense.get_pressure()
print(pressure) # 1020.384033203125 millibars