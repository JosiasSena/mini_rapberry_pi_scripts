import RPi.GPIO as GPIO

FREQUENCY_ON = 100  # Hz
FREQUENCY_OFF = 0  # Hz

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

motorPin1 = 7

GPIO.setup(motorPin1, GPIO.OUT)

try:
    while True:
        GPIO.output(motorPin1, True)
        GPIO.output(motorPin1, GPIO.HIGH)

except KeyboardInterrupt:
    pass

GPIO.cleanup()
