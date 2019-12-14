import time
import board
import neopixel
import adafruit_hcsr04
import simpleio
sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D6, echo_pin=board.D5) 
# simpleio.map_range(in_min, in_max, out_min, out_max)
dot = neopixel.NeoPixel(board.NEOPIXEL, 1, brightness=.1)

r = 0
g = 0
b = 0

while True:

    try:
        sonarValue = sonar.distance
        print((sonarValue,))
        if sonarValue < 5:
            dot.fill((255, 0, 0)) # If the distance is less than 5 then make red
        if sonarValue > 35:
            dot.fill((0, 255, 0)) # If distance greater than 35 make green
        if sonarValue <= 20 and sonarValue > 0:
            r = simpleio.map_range(sonarValue, 0, 20, 255, 0) # between 0 and 20 red goes down
            b = simpleio.map_range(sonarValue, 5, 20, 0, 255) # between 5 and 20 blue goes up
            g = simpleio.map_range(sonarValue, 20, 35, 0, 255) # between 20 and 35 green does up

        else: # when distance is over 20 
            r = simpleio.map_range(sonarValue, 0, 20, 255, 0) # between 0 and 20 red goes down
            b = simpleio.map_range(sonarValue, 20, 35, 255, 0) # between 20 and 35 blue goes down 
            g = simpleio.map_range(sonarValue, 20, 35, 0, 255) # between 20 and 35 green goes up
        dot.fill((int(r), int(g), int(b))) # make it the values

    except RuntimeError:
        print("NO")


time.sleep(.1)
