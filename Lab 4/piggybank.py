import time
import subprocess
import digitalio
import board
import busio
import sys
import digitalio
import adafruit_rgb_display.st7789 as st7789
import adafruit_apds9960.apds9960
import adafruit_mpr121
import adafruit_mpu6050
import qwiic_button
import qwiic_twist
from PIL import Image, ImageDraw, ImageFont

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

# Display the image
disp.image(image, rotation)

# Turn on the backlight
backlight = digitalio.DigitalInOut(board.D22)
backlight.switch_to_output()
backlight.value = True

# Initialize the buttons on the screen
buttonA = digitalio.DigitalInOut(board.D23)
buttonB = digitalio.DigitalInOut(board.D24)
buttonA.switch_to_input()
buttonB.switch_to_input()

# For the red and green LED buttons
buttonR = qwiic_button.QwiicButton(0x6f)
buttonG = qwiic_button.QwiicButton(0x60)
buttonR.begin()
buttonG.begin()
buttonR.LED_off()
buttonG.LED_off()

# For the capacitive sensor
i2c = busio.I2C(board.SCL, board.SDA)
mpr121 = adafruit_mpr121.MPR121(i2c)

# For the rotary encoder
twist = qwiic_twist.QwiicTwist()
twist.begin()
twist.count = 0

numP = 0
numN = 0
numD = 0
numQ = 0
currC = 0

def handle_speak(val):
    subprocess.run(["sh","GoogleTTS_demo.sh",val])

while True:
    # Draw a black filled box to clear the image.
    draw.rectangle((0, 0, width, height), outline=0, fill=0)

    if twist.is_pressed():
        print("Entered")
        time.sleep(0.5)
        while not twist.is_pressed():
            print(twist.count)

        print("Left")
        if currC == 1:
            numP += twist.count
            twist.count = 0
        elif currC == 5:
            numN += twist.count
            twist.count = 0
        elif currC == 10:
            numD += twist.count
            twist.count = 0
        elif currC ==  25:
            numQ += twist.count
            twist.count = 0

    for i in range(12):
        # Pennies
        if i == 1 and mpr121[i].value:
            currC = 1
            handle_speak("You have chosen penny")
        # Nickels
        elif i == 0 and mpr121[i].value:
            currC = 5
            handle_speak("You have chosen nickel")
        # Dimes
        elif i == 11 and mpr121[i].value:
            currC = 10
            handle_speak("You have chosen dime")
        # Quarters
        elif i == 10 and mpr121[i].value:
            currC = 25
            handle_speak("You have chosen quarter")
        elif i == 5 and mpr121[i].value:
            handle_speak("Here is how to use this device")
            handle_speak("First, gently tap the type of coin you are inserting.")
            handle_speak("Then press down on the knob.")
            handle_speak("Twist it to denote the number of coins you are inserting.")
            handle_speak("Press it down once again to confirm you have finished.")
            handle_speak("Then add the coins of that type into the slip at thetop.") 
            handle_speak("The red button tells you how much money you have in total.")
            handle_speak("The green button tells you how much of each coin is present.")

    if buttonR.is_button_pressed():
        total = numP * 1 + numN * 5 + numD * 10 + numQ * 25
        if total <  100:
            handle_speak("There are " + str(total) + " cents in the bank")
        else:
            dollars = total/100
            cents = total % 100
            handle_speak("There are " + str(dollars) + " dollars and " + str(cents) + " cents in the bank")

    if buttonG.is_button_pressed():
        handle_speak("There are " + str(numP) + " pennies, " + str(numN) + "nickels, " + str(numD) + " dimes and " + str(numQ) + " quarters in the bank")

    time.sleep(0.25)

