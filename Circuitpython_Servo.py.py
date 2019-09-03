import time
import board
import pulseio
from adafruit_motor import servo
import touchio

# import touchio

# touch_A1 = touchio.TouchIn(board.A1)  # Not a touch pin on Trinket M0!
# touch_A2 = touchio.TouchIn(board.A2)  # Not a touch pin on Trinket M0

# create a PWMOut object on Pin A2.
pwm = pulseio.PWMOut(board.D13, duty_cycle=2 ** 15, frequency=50)

angle = 0
# Create a servo object, my_servo.
my_servo = servo.Servo(pwm)

touch_A4 = touchio.TouchIn(board.A4)
touch_A5 = touchio.TouchIn(board.A5)
while True:
    if touch_A4.value:  # If i touch A4 wire:
        print("A4")
        if angle < 180:
            angle = angle + 5  # angle goes up by 5 while I touch wire
        my_servo.angle = angle
        time.sleep(0.05)
    if touch_A5.value:  # If I touch A5 wire:
        print("A5")
        if angle > 0:
            angle = angle - 5  # angle goes down by 5 while I touch the wire
        my_servo.angle = angle
        time.sleep(0.05)