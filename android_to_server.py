from socket import *
from time import sleep

import RPi.GPIO as GPIO

RUNNING = True

LED_PIN = 19

FREQUENCY_ON = 100  # Hz
FREQUENCY_OFF = 0  # Hz

HOST = "192.168.1.7"
PORT = 7000

socket = socket(AF_INET, SOCK_STREAM)
socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
socket.bind((HOST, PORT))
socket.listen(5)  # how many connections can it receive at one time
conn, addr = socket.accept()  # accept the connection

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(LED_PIN, GPIO.OUT)

led = GPIO.PWM(LED_PIN, FREQUENCY_ON)
led.start(FREQUENCY_OFF)


def turn_led_on():
    led.ChangeDutyCycle(FREQUENCY_ON)


def turn_led_off():
    led.ChangeDutyCycle(FREQUENCY_OFF)


try:
    while RUNNING:

        # how many bytes of data will the server receive
        data = conn.recv(1024)

        if not data:
            break

        # decoded message - a string representation
        message = str(data.decode('utf-8'))

        if len(message) > 0:
            if message.__contains__("on"):
                print "Turning LED on"
                turn_led_on()
            elif message.__contains__("off"):
                print "Turning LED off"
                turn_led_off()
            elif message.__contains__("blink"):
                print "Blinking LED"

                for i in range(5):
                    turn_led_on()
                    sleep(1)
                    turn_led_off()
                    sleep(1)

except KeyboardInterrupt:
    RUNNING = False

conn.close()
socket.close()
