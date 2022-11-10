from sense_hat import SenseHat

sense = SenseHat()
sense.clear()

humidity = sense.get_humidity()
print(humidity) # 35.24535369873047 %