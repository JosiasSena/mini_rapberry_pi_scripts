from time import sleep

from gpiozero import LED

# Constants
RUNNING = True

# Init LED
led = LED(17)

# Main loop
try:
    while RUNNING:
        led.on()
        sleep(1)
        led.off()
        sleep(1)

# If CTRL+C is pressed the main loop is broken
except KeyboardInterrupt:
    RUNNING = False
