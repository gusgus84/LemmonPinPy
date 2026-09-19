from time import sleep
import board
import neopixel

try:
    ledStrip = neopixel.NeoPixel(board.D18, 5, brightness=0.8, auto_write=False, pixel_order=neopixel.BGR)
    ledStrip[0] = (0xFF, 0x00, 0x00)
    ledStrip[1] = (0xFF, 0xFF, 0xFF)
    ledStrip[2] = (0x00, 0x00, 0xFF)
    ledStrip[3] = (0xFF, 0x00, 0xFF)
    ledStrip[4] = (0xFF, 0xFF, 0x00)
    ledStrip.show()

    b=0

    while(True):
        b = b + 1 
        ledStrip[1] = (0xFF, 0xFF, 0xFF) if b % 2 == 0 else (0x00, 0x00, 0x00)
        sleep(0.5);
finally:
    ledStrip.deinit();