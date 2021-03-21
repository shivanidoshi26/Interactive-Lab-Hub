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
import digitalio
import qwiic_joystick
import os
from vosk import Model, KaldiRecognizer
import wave
import json
import shlex
from subprocess import Popen, call

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

# For the proximity sensor
i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_apds9960.apds9960.APDS9960(i2c)
sensor.enable_proximity = True

# For the joystick
joystick = qwiic_joystick.QwiicJoystick()
joystick.begin()

def handle_speak(val):
    subprocess.run(["sh","GoogleTTS_demo.sh",val])

def check_userinput():
    os.system('arecord -D hw:2,0 -f cd -c1 -r 48000 -d 10 -t wav recorded_mono.wav')
    wf = wave.open("recorded_mono.wav", "rb")

    model = Model("model")
    rec = KaldiRecognizer(model, wf.getframerate())
        
    while True:
        data = wf.readframes(4000)
        if len(data) == 0:
            break
        rec.AcceptWaveform(data)

    d = json.loads(rec.FinalResult())
    return d

door1 = 0
door2 = 0
door3 = 0
door4 = 0

while True:
    # Draw a black filled box to clear the image.
    draw.rectangle((0, 0, width, height), outline=0, fill=0)

    prox = sensor.proximity
    if prox > 1:
        main_image = Image.open("images/welcome.png")
        main_image = main_image.convert('RGB')
        main_image = main_image.resize((width, height), Image.BICUBIC)
        disp.image(main_image, rotation)
        handle_speak("Welcome to puzzle bot! You must solve 4 riddles to win. Use the joystick to navigate to each riddle. Remember to say your answer loudly and directly into the mike. Good luck!")

    if joystick.get_horizontal() > 510:
        if door1 == 0:
            door_image = Image.open("images/door1.jpeg")
            door_image = door_image.convert('RGB')
            door_image = door_image.resize((width, height), Image.BICUBIC)
            disp.image(door_image, rotation)
            handle_speak("Riddle 1")
            handle_speak("You have ten seconds to answer")

            d = check_userinput()
            if(d["text"] == "two"):
                handle_speak("Correct")
                door1 = 1
            else:
                handle_speak("Incorrect, try again")
        else:
            door_image = Image.open("images/opendoor.jpeg")
            door_image = door_image.convert('RGB')
            door_image = door_image.resize((width, height), Image.BICUBIC)
            disp.image(door_image, rotation)
            handle_speak("Riddle 1 has been solved")

    if joystick.get_vertical() < 450:
        door_image = Image.open("images/door2.jpeg")
        door_image = door_image.convert('RGB')
        door_image = door_image.resize((width, height), Image.BICUBIC)
        disp.image(door_image, rotation)
        handle_speak("Riddle 2")

    if joystick.get_horizontal() < 100:
        door_image = Image.open("images/door3.jpeg")
        door_image = door_image.convert('RGB')
        door_image = door_image.resize((width, height), Image.BICUBIC)
        disp.image(door_image, rotation)
        handle_speak("Riddle 2")

    if joystick.get_vertical() > 1000:
        door_image = Image.open("images/door4.jpeg")
        door_image = door_image.convert('RGB')
        door_image = door_image.resize((width, height), Image.BICUBIC)
        disp.image(door_image, rotation)
        handle_speak("Riddle 2")

    time.sleep(0.1)

