import time
import subprocess
import digitalio
import board
from PIL import Image, ImageDraw, ImageFont
import adafruit_rgb_display.st7789 as st7789
import board
import busio
import adafruit_apds9960.apds9960
import time
import qwiic_button
import sys

#gesture sensor
i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_apds9960.apds9960.APDS9960(i2c)

# Configuration for CS and DC pins (these are FeatherWing defaults on M0/M4):
cs_pin = digitalio.DigitalInOut(board.CE0)
dc_pin = digitalio.DigitalInOut(board.D25)
reset_pin = None

# Config for display baudrate (default max is 24mhz):
BAUDRATE = 64000000

# Setup SPI bus using hardware SPI:
spi = board.SPI()

# Create the ST7789 display:
disp = st7789.ST7789(
    spi,
    cs=cs_pin,
    dc=dc_pin,
    rst=reset_pin,
    baudrate=BAUDRATE,
    width=135,
    height=240,
    x_offset=53,
    y_offset=40,
)

# Create blank image for drawing.
# Make sure to create image with mode 'RGB' for full color.
height = disp.width  # we swap height/width to rotate it to landscape!
width = disp.height
image = Image.new("RGB", (width, height))
rotation = 90

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image.
draw.rectangle((0, 0, width, height), outline=0, fill=(0, 0, 0))

disp.image(image, rotation)

# Draw some shapes.
# First define some constants to allow easy resizing of shapes.
padding = -2
top = padding
bottom = height - padding

# Move left to right keeping track of the current x position for drawing shapes.
x = 5

# Alternatively load a TTF font.  Make sure the .ttf font file is in the
# same directory as the python script!
# Some other nice fonts to try: http://www.dafont.com/bitmap.php
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 26)
font1 = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 16)
font2 = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 50)
font3 = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 23)

image1 = Image.new("RGB", (width, height))
image1 = Image.open("images/red.jpg")

image2 = Image.new("RGB", (width, height))
image2 = Image.open("images/smiley.jpg")

# Scale the first image to the smaller screen dimension
image_ratio1 = image1.width / image1.height
screen_ratio = width / height
if screen_ratio < image_ratio1:
    scaled_width = image1.width * height // image1.height
    scaled_height = height
else:
    scaled_width = width
    scaled_height = image1.height * width // image1.width
image1 = image1.resize((scaled_width, scaled_height), Image.BICUBIC)

# Crop and center the first  image
x = scaled_width // 2 - width // 2
y = scaled_height // 2 - height // 2
image1 = image1.crop((x, y, x + width, y + height))

# Scale the second image to the smaller screen dimension
image_ratio2 = image2.width / image2.height
if screen_ratio < image_ratio2:
    scaled_width = image2.width * height // image2.height
    scaled_height = height
else:
    scaled_width = width
    scaled_height = image2.height * width // image2.width
image2 = image2.resize((scaled_width, scaled_height), Image.BICUBIC)

# Crop and center the second image
x = scaled_width // 2 - width // 2
y = scaled_height // 2 - height // 2
image2 = image2.crop((x, y, x + width, y + height))

# Turn on the backlight
backlight = digitalio.DigitalInOut(board.D22)
backlight.switch_to_output()
backlight.value = True

buttonA = digitalio.DigitalInOut(board.D23)
buttonB = digitalio.DigitalInOut(board.D24)
buttonA.switch_to_input()
buttonB.switch_to_input()

buttonR = qwiic_button.QwiicButton()
buttonR.begin()

DAYW = "%a, %d %b %Y"
DAYN = "%a, %m/%d/%Y"
TIMEH = "%H:%M:%S"
TIMEI = "%I:%M:%S %p"

DAY = DAYW
TIME = TIMEI

dt = 0

b = 0

sensor.enable_proximity = True

buttonR.LED_off()

while True:
    # Draw a black filled box to clear the image.
    draw.rectangle((0, 0, width, height), outline=0, fill="#5B009E")

    prox = sensor.proximity
    if prox > 2:
        backlight.value = True
    else:
        backlight.value = False

    cmd = "curl -s wttr.in/?format=1"
    WTTR = subprocess.check_output(cmd, shell=True).decode("utf-8")

    #if buttonB.value and not buttonA.value: # just button A pressed
    #    if d % 2 == 0:
    #        DAY = DAYW
    #    else:
    #        DAY = DAYN
    #    d += 1
    #if buttonA.value and not buttonB.value: # just button B pressed
    #    if t % 2 == 0:
    #        TIME = TIMEI
    #    else:
    #        TIME = TIMEH
    #    t += 1

    if buttonB.value and not buttonA.value: # just button A pressed
        if dt % 2 == 0:
            DAY = DAYW
            TIME = TIMEI
        else:
            DAY = DAYN
            TIME = TIMEH
        dt += 1
    if buttonA.value and not buttonB.value: # just button B pressed
        if b % 2 == 0:
            pass
        b += 1 

    if buttonR.is_button_pressed() == True:
        buttonR.LED_on(100)
        numS = 0
        numM = 0
        while buttonR.is_button_pressed() == False:
            draw.rectangle((0, 0, width, height), outline=0, fill="#000000")
            if numS != 0 and numS % 60 == 0:
                numM += 1
            ptime = "{0:0=2d}".format(numM) + ":" + "{0:0=2d}".format(numS % 60)
            draw.text((50, 40), ptime, font=font2, fill="#FFFFFF")
            disp.image(image, rotation)
            numS += 1
            time.sleep(1)
        buttonR.LED_off()
        time.sleep(1)
        draw.rectangle((0, 0, width, height), outline=0, fill="#5B009E")

    y = top
    draw.text((5, y), time.strftime(DAY), font=font, fill="#FFFFFF")
    y += font.getsize(DAY)[1] + 10
    draw.text((5, y), time.strftime(TIME), font=font, fill="#00AABA")
    y += font.getsize(DAY)[1] + 5
    draw.text((5, y), WTTR, font=font1, fill="#99BA00")
    y += font.getsize(DAY)[1]

    if int(time.strftime("%H")) < 6 or int(time.strftime("%H")) >= 18:
        draw.text((5, y), "Have a good night!", font=font3, fill="#FF69B4")
    else:
        draw.text((5, y), "Have a great day!", font=font3, fill="#FF69B4")

    disp.image(image, rotation)
    time.sleep(0.1)

