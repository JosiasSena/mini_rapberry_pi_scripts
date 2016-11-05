from time import sleep

from gpiozero import *

RUNNING = True

SLEEP_TIME = .5  # in seconds

lights = TrafficLights(25, 8, 7)
button = Button(2)
rgbLED = RGBLED(13, 6, 5)

try:
    while RUNNING:
        rgbLED.blink()

        lights.green.on()
        sleep(1)
        lights.green.off()

        lights.amber.on()
        sleep(1)
        lights.amber.off()

        lights.red.on()
        sleep(1)
        lights.red.off()

except KeyboardInterrupt:
    RUNNING = False
