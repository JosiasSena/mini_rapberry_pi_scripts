from socket import *
from subprocess import *
from time import sleep

import RPi.GPIO as GPIO

import I2C_LCD_driver

RUNNING = True

LED_PIN = 19

FREQUENCY_ON = 100  # Hz
FREQUENCY_OFF = 0  # Hz

HOST = "192.168.1.5"
PORT = 7000

lcd = I2C_LCD_driver.lcd()

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
    turn_on = "Turning LED on"
    lcd.lcd_clear()

    print turn_on
    lcd.lcd_display_string(turn_on)

    led.ChangeDutyCycle(FREQUENCY_ON)


def turn_led_off():
    turn_off = "Turning LED off"
    lcd.lcd_clear()

    print turn_off
    lcd.lcd_display_string(turn_off)

    led.ChangeDutyCycle(FREQUENCY_OFF)


def blink_led():
    print "Blinking LED"
    lcd.lcd_clear()

    for i in range(5):
        led.ChangeDutyCycle(FREQUENCY_ON)
        lcd.lcd_display_string("Blinking!")
        sleep(.5)

        lcd.lcd_clear()
        led.ChangeDutyCycle(FREQUENCY_OFF)
        sleep(.5)


try:
    while RUNNING:

        # how many bytes of data will the server receive
        data = conn.recv(1024)

        if not data:
            break

        # decoded message - a string representation
        received_message = str(data.decode('utf-8'))

        if len(received_message) > 0:
            if received_message.__contains__("turn light on"):
                turn_led_on()
            elif received_message.__contains__("turn light off"):
                turn_led_off()
            elif received_message.__contains__("blink light"):
                blink_led()
            elif received_message.__contains__("start playlist"):
                print "Starting playlist"
                call(["sudo", "bash", "/home/pi/lightshowpi/bin/start_playlist.sh"], shell=False)
            elif received_message.__contains__("stop playlist"):
                print "Stop playlist"
                call(["signal.SIGINT"])
                os.kill(1, signal.SIGINT)
            else:
                lcd.lcd_clear()
                lcd.lcd_display_string(received_message)

except KeyboardInterrupt:
    RUNNING = False

conn.close()
socket.close()
