import board
import busio
import time
import digitalio
import storage
import wifi
import terminalio

# Import External Modules
import adafruit_sdcard  # SD Card SPI
import adafruit_pcf8523  # RTC I2C

import displayio
import adafruit_displayio_sh1107
import adafruit_display_text.bitmap_label as label
from adafruit_debouncer import Debouncer
# Import Custom Modules
from screen_dynamics import *

# Initialize I2C Bus
# i2c = busio.I2C(board.SCL, board.SDA)
i2c = board.I2C()

# Initialize SPI Bus
spi = busio.SPI(board.SCK, board.MOSI, board.MISO)

# Initialize SD Card
# cs = digitalio.DigitalInOut(board.D19)
# sdcard = adafruit_sdcard.SDCard(spi, cs)
# vfs = storage.VfsFat(sdcard)
# storage.mount(vfs, "/sd")




# # Initialize RTC
rtc = adafruit_pcf8523.PCF8523(i2c)
# rtc.datetime = time.struct_time((2023, 12, 11, 15, 57, 0, 0, -1, -1))

print("Date: " + str(rtc.datetime.tm_mday) + "/" + str(rtc.datetime.tm_mon) + "/" + str(rtc.datetime.tm_year))
print("Time: " + str(rtc.datetime.tm_hour) + ":" + str(rtc.datetime.tm_min) + ":" + str(rtc.datetime.tm_sec))

# Initialize WiFi
# wifi.radio.connect("SSID", "PASSWORD")


# Initialize Display
display_group = displayio.Group()
displayio.release_displays()
display_bus = displayio.I2CDisplay(i2c, device_address=0x3C)
display = adafruit_displayio_sh1107.SH1107(display_bus, width=128, height=64)
display.auto_refresh = True
splash = displayio.Group()
display.show(splash)

# Initialize Onboard LED
led = digitalio.DigitalInOut(board.D13)
led.direction = digitalio.Direction.OUTPUT

# Initialize Buttons
# buttonA = digitalio.DigitalInOut(board.D5)
# buttonA.direction = digitalio.Direction.INPUT
# buttonA.pull = digitalio.Pull.UP

# buttonB = digitalio.DigitalInOut(board.D21)
# buttonB.direction = digitalio.Direction.INPUT
# buttonB.pull = digitalio.Pull.UP

# buttonC = digitalio.DigitalInOut(board.D20)
# buttonC.direction = digitalio.Direction.INPUT
# buttonC.pull = digitalio.Pull.UP

# Initialize Text Area
text_area_title = label.Label(terminalio.FONT, text="City Sensing Toolkit Dashboard")
text_area_title.x = 10
text_area_title.y = 10
display_group.append(text_area_title)

# Debouncer function
def debouncable(pin):
    switch_io = digitalio.DigitalInOut(pin)
    switch_io.direction = digitalio.Direction.INPUT
    switch_io.pull = digitalio.Pull.UP
    return switch_io

def main():
    buttonA = Debouncer(debouncable(board.D5))
    buttonB = Debouncer(debouncable(board.D21))
    buttonC = Debouncer(debouncable(board.D20))


    while True:
        buttonA.update()
        if buttonA.fell:
            print("Button A Pressed")
            led.value = True
            time.sleep(0.25)
            led.value = False
            time.sleep(0.25)
        buttonB.update()
        if buttonB.fell:
            print("Button B Pressed")
            led.value = True
            time.sleep(0.25)
            led.value = False
            time.sleep(0.25)
        buttonC.update()
        if buttonC.fell:
            print("Button C Pressed")
            led.value = True
            time.sleep(0.25)
            led.value = False
            time.sleep(0.25)

if __name__ == '__main__':
    main()
    