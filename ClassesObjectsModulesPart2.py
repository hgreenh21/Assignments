import time
import board
from rgb import RGB   # import the RGB class from the rgb module

r1 = board.D3
g1 = board.D4
b1 = board.D5
r2 = board.D10
g2 = board.D11
b2 = board.D12

myRGB1 = RGB(r1, g1, b1)   # create a new RGB object, using pins 3, 4, and 5
myRGB2 = RGB(r2, g2, b2)   # create a new RGB object, using pins 8, 9, and 10

myRGB1.red()          # Glow red
myRGB2.green()        # Glow green
time.sleep(1.5)
myRGB1.blue()         # Glow blue
myRGB2.cyan()         # Glow cyan
time.sleep(1.5)
myRGB1.magenta()      # Glow magenta
myRGB2.yellow()       # Glow yellow
time.sleep(1.5)
myRGB1.rainbow("rate1")  # Fade colors of the rainbow at the given rate.
myRGB2.rainbow("rate2")  # Fade colors of the rainbow at the given rate.
time.sleep(1)