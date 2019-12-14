import time
from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface
from digitalio import DigitalInOut, Direction, Pull
from lcd.lcd import CursorMode
import board

# Talk to the LCD at I2C address 0x27.
# The number of rows and columns defaults to 4x20, so those
# arguments could be omitted in this case.
lcd = LCD(I2CPCF8574Interface(0x27), num_rows=2, num_cols=16)
# 0x27 or 0x3F

button = DigitalInOut(board.D2)
button.direction = Direction.INPUT
button.pull = Pull.UP

button_state = None
last_state = None
value = 0
lcd.print("  CircuitPython        LCD ") # opening screen 

time.sleep(2)
lcd.clear() # clears screen


lcd.set_cursor_pos(0, 0)
lcd.print("ButtonPresses:") # prints this

# Make the cursor visible as a line.
lcd.set_cursor_mode(CursorMode.LINE)

while True:
    if button.value: 
        print("not pressed")
# prints that when button is not pressed
# for some reason the button value is backwards so I just made my code accomodate that
    else:
        value = value + 1 # when button is pressed add 1 to value
        print(value) # prints the value in serial
        button_state = None # sets the button state to none
        lcd.set_cursor_pos(1, 0)
        lcd.print(str(value)) # prints the bariable value
        time.sleep(0.2)

# if button is high and last_state = low
    time.sleep(0.01)
