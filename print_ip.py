import fcntl
import socket
import struct

import I2C_LCD_driver

lcd = I2C_LCD_driver.lcd()


def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,
        struct.pack('256s', ifname[:15])
    )[20:24])

lcd.lcd_display_string("IP Address:", 1)

lcd.lcd_display_string(get_ip_address('wlan0'), 2)
