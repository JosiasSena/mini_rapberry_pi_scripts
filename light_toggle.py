from signal import pause

from gpiozero import LED, Button

led = LED(19)
button = Button(4)

button.when_pressed = led.on
button.when_released = led.off

pause()
