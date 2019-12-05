from digitalio import DigitalInOut, Direction, Pull
import board
import time
# ggfhfghgh
max = 4
start = time.monotonic() # sets up a timeer

photo = DigitalInOut(board.D2) # pin
photo.direction = Direction.INPUT
photo.pull = Pull.UP

photo_state = False
last_state = False

value = 0
limit = 0

while True:

    photo_state = photo.value

    if photo_state and not last_state: # IF PHOTO INTERRUPTER IS INTERRUPTED AND IT WASNT BEFORE 
        value = value + 1 # add one
        # print("# of interrupts:")
        # print(value)

    last_state = photo_state

    remaining = max - time.monotonic()

    if remaining <= 0:
        print("# of interrupts:", (value))
        max = time.time() + 4
        value = 0
