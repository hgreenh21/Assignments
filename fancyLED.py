import digitalio #pylint: disable-msg=import-error 
from digitalio import DigitalInOut, Direction, Pull #pylint: disable-msg=import-error
import time
import board #pylint: disable-msg=import-error
import random #pylint: disable-msg=import-error
# those lines make i so it doesn't show up as an error
class FancyLED :

    def __init__(self, p1, p2, p3):
        self.L1 = p1 # 1st light
        self.L2 = p2 # 2nd light
        self.L3 = p3 # 3rd light
# set up the variables for the leds
        self.L1 = DigitalInOut(p1)
        self.L1.direction = Direction.OUTPUT
        self.L2 = DigitalInOut(p2)
        self.L2.direction = Direction.OUTPUT
        self.L3 = DigitalInOut(p3)
        self.L3.direction = Direction.OUTPUT

    def alternate(self):
        self.L1.value = True 
        self.L2.value = False
        self.L3.value = True
        time.sleep(1)
        self.L1.value = False
        self.L2.value = True
        self.L3.value = False
        time.sleep(0.5)
        self.L2.value = False
# makes it so 2 lights are on at a time and then one is on. It then turns last one off

    def chase(self):
        self.L1.value = True 
        time.sleep(0.1) 
        self.L2.value = True # 1st light, 2nd on, then 1st off
        time.sleep(0.1) 
        self.L1.value = False
        time.sleep(0.1)
        self.L3.value = True # 3rd on, 2nd off, 3rd off
        time.sleep(0.1)
        self.L2.value = False
        time.sleep(0.1)
        self.L3.value = False
        time.sleep(1)

        
    def blink(self):
        self.L1.value = True
        self.L2.value = True
        self.L3.value = True # all 3 on
        time.sleep(1)
        self.L1.value = False
        self.L2.value = False
        self.L3.value = False # all 3 off
        time.sleep(1)

    def sparkle(self):
        print("sparkle")
