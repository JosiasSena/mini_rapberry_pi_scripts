import random
from time import sleep

import RPi.GPIO as GPIO

RUNNING = True

LED_PIN = 17

FREQUENCY_ON = 100  # Hz
FREQUENCY_OFF = 0  # Hz

TURNED_ON = True
TURNED_OFF = True
state = TURNED_OFF

# RGB Pin numbers
redPin = 13
greenPin = 6
bluePin = 5

# Button
buttonPin = 4

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(redPin, GPIO.OUT)
GPIO.setup(greenPin, GPIO.OUT)
GPIO.setup(bluePin, GPIO.OUT)

led = GPIO.PWM(LED_PIN, FREQUENCY_ON)
led.start(FREQUENCY_OFF)

# RGB LED
RED = GPIO.PWM(redPin, FREQUENCY_ON)
RED.start(FREQUENCY_OFF)

GREEN = GPIO.PWM(greenPin, FREQUENCY_ON)
GREEN.start(FREQUENCY_OFF)

BLUE = GPIO.PWM(bluePin, FREQUENCY_ON)
BLUE.start(FREQUENCY_OFF)

lights = [RED, GREEN, BLUE]


def blink_lights():
    print "Blinking!"

    global light

    while state == TURNED_ON:
        light = random.choice(lights)

        turn_led_on()
        sleep(1)

        turn_led_off()
        sleep(1)


def turn_led_on():
    led.ChangeDutyCycle(FREQUENCY_ON)
    light.ChangeDutyCycle(FREQUENCY_ON)


def turn_led_off():
    led.ChangeDutyCycle(FREQUENCY_OFF)
    light.ChangeDutyCycle(FREQUENCY_OFF)


def button_clicked_callback(channel):
    print "Clicked channel", channel

    global state

    if state == TURNED_OFF:
        state = TURNED_ON
        blink_lights()
    else:
        print "stop"
        state = TURNED_OFF


GPIO.add_event_detect(buttonPin, GPIO.RISING, callback=button_clicked_callback, bouncetime=400)

try:
    while RUNNING:
        # button_input_state = GPIO.input(buttonPin)
        global button_input_state

        # if not button_input_state:
        #     print "clicked"
        #
        #     if state == TURNED_OFF:
        #         state = TURNED_ON
        #         blink_lights()
        #         sleep(.3)

except KeyboardInterrupt:
    RUNNING = False
    turn_led_off()
    state = TURNED_OFF
