import time
import board
import neopixel
import adafruit_hcsr04
import simpleio
sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D6, echo_pin=board.D5)
# simpleio.map_range(x, in_min, in_max, out_min, out_max)
dot = neopixel.NeoPixel(board.NEOPIXEL, 1, brightness=.1)

r = 0
g = 0
b = 0

while True:

    try:
        sonarValue = sonar.distance
        print((sonarValue,))
        if sonarValue < 5:
            dot.fill((255, 0, 0))
        if sonarValue > 35:
            dot.fill((0, 255, 0))
        if sonarValue <= 20 and sonarValue > 0:
            r = simpleio.map_range(sonarValue, 0, 20, 255, 0)
            b = simpleio.map_range(sonarValue, 5, 20, 0, 255)
            g = simpleio.map_range(sonarValue, 20, 35, 0, 255)

        else:
            r = simpleio.map_range(sonarValue, 0, 20, 255, 0)
            b = simpleio.map_range(sonarValue, 20, 35, 255, 0)
            g = simpleio.map_range(sonarValue, 20, 35, 0, 255)
        dot.fill((int(r), int(g), int(b)))

    except RuntimeError:
        print("NO")


time.sleep(.1)