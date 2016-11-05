import random
import time

import RPi.GPIO as GPIO

# Constants
RUNNING = True
SLEEP_TIME = .2  # in seconds
FREQUENCY_ON = 100  # Hz
FREQUENCY_OFF = 0  # Hz

# Init GPIO - set GPIO to Broadcom system
GPIO.setmode(GPIO.BCM)

# Disable warnings
GPIO.setwarnings(False)

# RGB LED breadboard Pin numbers (change accordingly)
redPin = 12
greenPin = 16
bluePin = 21

# Button breadboard pin number (change accordingly)
buttonPin = 4

# Set RGB LED pins to output mode
GPIO.setup(redPin, GPIO.OUT)
GPIO.setup(greenPin, GPIO.OUT)
GPIO.setup(bluePin, GPIO.OUT)

# Setting button as an input device
GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Setup all the LED colors with an initial
# duty cycle of 0 which is off
RED = GPIO.PWM(redPin, FREQUENCY_ON)
RED.start(FREQUENCY_OFF)

GREEN = GPIO.PWM(greenPin, FREQUENCY_ON)
GREEN.start(FREQUENCY_OFF)

BLUE = GPIO.PWM(bluePin, FREQUENCY_ON)
BLUE.start(FREQUENCY_OFF)

lights = [RED, GREEN, BLUE]

# Main loop
try:
    while RUNNING:
        button_input_state = GPIO.input(buttonPin)

        light = random.choice(lights)

        if not button_input_state:
            light.ChangeDutyCycle(FREQUENCY_ON)
            light = random.choice(lights)
            time.sleep(SLEEP_TIME)
        else:
            light.ChangeDutyCycle(FREQUENCY_OFF)

# If CTRL+C is pressed the main loop is broken
except KeyboardInterrupt:
    RED.ChangeDutyCycle(FREQUENCY_OFF)
    GREEN.ChangeDutyCycle(FREQUENCY_OFF)
    BLUE.ChangeDutyCycle(FREQUENCY_OFF)
    RUNNING = False
