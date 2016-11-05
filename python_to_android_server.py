from socket import *

import RPi.GPIO as GPIO

RUNNING = True

OPEN_HAVEN = "Open RapidSOS Haven App"

HOST = "192.168.1.5"
PORT = 7000

# Button breadboard pin number (change accordingly)
BUTTON_PIN = 2

socket = socket(AF_INET, SOCK_STREAM)
socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
socket.bind((HOST, PORT))
socket.listen(5)  # how many connections can it receive at one time
conn, addr = socket.accept()  # accept the connection

# Init GPIO - set GPIO to Broadcom system
GPIO.setmode(GPIO.BCM)

# Disable warnings
GPIO.setwarnings(False)

# Setting button as an input device
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
    while RUNNING:
        button_not_clicked = GPIO.input(BUTTON_PIN)

        if not button_not_clicked:
            print "Bytes sent:", conn.send(OPEN_HAVEN), "bytes"

except KeyboardInterrupt:
    RUNNING = False

conn.close()
socket.close()
