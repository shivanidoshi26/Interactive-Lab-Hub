from flask import Flask, Response,render_template
from flask_socketio import SocketIO, send, emit

import time
import board
import busio
import socket
import signal
import sys
import adafruit_mpu6050
import qwiic_joystick

# For the accelerometer
i2c = busio.I2C(board.SCL, board.SDA)
mpu = adafruit_mpu6050.MPU6050(i2c)

# For the joystick
joystick = qwiic_joystick.QwiicJoystick()
joystick.begin()

hostname = socket.gethostname()
hardware = 'plughw:2,0'

app = Flask(__name__)
socketio = SocketIO(app)

@socketio.on('connect')
def test_connect():
    print('connected')
    emit('after connect',  {'data':'Lets dance'})

# Send back accelerometer interaction
@socketio.on('ping-accel')
def handle_message(val):
    if mpu.acceleration > 5:
        emit('pong-accel', currAccel)

# Send back joystick interaction
@socketio.on('ping-joystick')
def handle_message(val):
    if joystick.get_horizontal() < 510:
        emit('pong-joystick','make a jump')

@app.route('/')
def index():
    return render_template('index.html', hostname=hostname)

def signal_handler(sig, frame):
    print('Closing Gracefully')
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)


if __name__ == "__main__":
    socketio.run(app, host='0.0.0.0', port=5000)


