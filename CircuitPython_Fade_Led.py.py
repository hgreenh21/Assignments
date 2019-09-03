import time
import board
import pulseio

led = pulseio.PWMOut(board.D13, frequency=5000, duty_cycle=0)  # D13=Pin number

while True:
    for i in range(100):
        # PWM LED up and down
        if i < 50:

            led.duty_cycle = int(i * 2 * 65535 / 100)  # fades up, how fast it goes up
        else:
            led.duty_cycle = 65535 - int((i - 50) * 2 * 65535 / 100)  # fades down, how fast it goes down
        time.sleep(0.03) # delay

# 65535 is the max power the duty cycle can send(100%)