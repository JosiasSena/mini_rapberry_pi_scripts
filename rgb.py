import time

import RPi.GPIO as GPIO

# Constants
RUNNING = True
SLEEP_TIME = .5  # in seconds
FREQUENCY_ON = 100  # Hz
FREQUENCY_OFF = 0  # Hz

# Init GPIO - set GPIO to Broadcom system
GPIO.setmode(GPIO.BCM)

# Disable warnings
GPIO.setwarnings(False)

#  Set RGB Pin numbers
redPin = 12
greenPin = 16
bluePin = 21

# Set RGB LED pins to output mode
GPIO.setup(redPin, GPIO.OUT)
GPIO.setup(greenPin, GPIO.OUT)
GPIO.setup(bluePin, GPIO.OUT)

# Setup all the LED colors with an initial
# duty cycle of 0 which is off
RED = GPIO.PWM(redPin, FREQUENCY_ON)
RED.start(FREQUENCY_OFF)

GREEN = GPIO.PWM(greenPin, FREQUENCY_ON)
GREEN.start(FREQUENCY_OFF)

BLUE = GPIO.PWM(bluePin, FREQUENCY_ON)
BLUE.start(FREQUENCY_OFF)

# Main loop
try:
    while RUNNING:
        RED.ChangeDutyCycle(FREQUENCY_ON)
        time.sleep(SLEEP_TIME)
        RED.ChangeDutyCycle(FREQUENCY_OFF)

        GREEN.ChangeDutyCycle(FREQUENCY_ON)
        time.sleep(SLEEP_TIME)
        GREEN.ChangeDutyCycle(FREQUENCY_OFF)

        BLUE.ChangeDutyCycle(FREQUENCY_ON)
        time.sleep(SLEEP_TIME)
        BLUE.ChangeDutyCycle(FREQUENCY_OFF)

# If CTRL+C is pressed the main loop is broken
except KeyboardInterrupt:
    RED.ChangeDutyCycle(FREQUENCY_OFF)
    GREEN.ChangeDutyCycle(FREQUENCY_OFF)
    BLUE.ChangeDutyCycle(FREQUENCY_OFF)
    RUNNING = False
