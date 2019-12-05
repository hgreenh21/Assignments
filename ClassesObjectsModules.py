import pulseio
import time
class RGB():

    full = 65535
    half = int(65535/2)

    def __init__(self, r, g, b):
        print(str(r))
        self.r = pulseio.PWMOut(r, frequency=5000, duty_cycle=0) #sets up r,g, and b values
        self.g = pulseio.PWMOut(g, frequency=5000, duty_cycle=0)
        self.b = pulseio.PWMOut(b, frequency=5000, duty_cycle=0)

    def red(self):
        print("red")
        self.r.duty_cycle = 0 # makes it red, rgb leds are opposite
        self.g.duty_cycle = self.full
        self.b.duty_cycle = self.full

    def green(self):
        print("green")
        self.r.duty_cycle = self.full
        self.g.duty_cycle = 0 #green all the way up
        self.b.duty_cycle = self.full

    def blue(self):
        print("blue")
        self.r.duty_cycle = self.full
        self.g.duty_cycle = self.full
        self.b.duty_cycle = 0 # blue all the way up

    def cyan(self):
        print("cyan")
        self.r.duty_cycle = self.full
        self.g.duty_cycle = 0 
        self.b.duty_cycle = 0 # blue and green on to make cyan

    def magenta(self):
        print("magenta")
        self.r.duty_cycle = 0
        self.g.duty_cycle = self.full
        self.b.duty_cycle = 0 # red and blue on to make magenta color

    def yellow(self):
        print("yellow")
        self.r.duty_cycle = 0 # red and green on to make yellow color
        self.g.duty_cycle = 0
        self.b.duty_cycle = self.full

    def rainbow(self, x):
        print("rainbow")
        if x == "rate1": # for rate one, first led
            self.r.duty_cycle = 0 # starts red
            self.b.duty_cycle = (self.full)
            self.g.duty_cycle = (self.full)
            for i in range(5, 65535, 5):
                self.r.duty_cycle = i
                self.b.duty_cycle =(self.full)
                self.g.duty_cycle = (self.full)-i # turns it green
                time.sleep(.00002)
            for i in range(5, 65535, 5):
                self.r.duty_cycle = (self.full)
                self.b.duty_cycle = (self.full) - i # turns it blue
                self.g.duty_cycle = i
                time.sleep(.00002)
            for i in range(5, 65535, 5):
                self.r.duty_cycle = (self.full) - i 
                self.b.duty_cycle = i # brings it back to red
                self.g.duty_cycle = (self.full)
                time.sleep(.00002)



        elif x == "rate2":# for rate 2, 2nd led
            self.r.duty_cycle = 0
            self.b.duty_cycle = (self.full)
            self.g.duty_cycle = (self.full)
            for i in range(1, 21845): # its the same thing except faster
                self.r.duty_cycle += 11 #adds more blue and less red
                self.b.duty_cycle -= 9
            self.r.duty_cycle = (self.full)
            self.b.duty_cycle = 0 # makes it blue
            self.g.duty_cycle = (self.full)
            for i in range(21845, 43690):
                self.b.duty_cycle += 11 # less blue and more green
                self.g.duty_cycle -= 9
            self.r.duty_cycle = (self.full)
            self.b.duty_cycle = (self.full)
            self.g.duty_cycle = 0 # green
            for i in range(43690, 65535):
                self.g.duty_cycle += 11 # less green and more red
                self.r.duty_cycle -= 9
