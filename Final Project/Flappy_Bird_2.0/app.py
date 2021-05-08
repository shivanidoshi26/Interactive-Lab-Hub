from flask import Flask, Response,render_template
from flask_socketio import SocketIO, send, emit

import time
import board
import busio
import adafruit_mpu6050
import socket

import signal
import sys

i2c = busio.I2C(board.SCL, board.SDA)
mpu = adafruit_mpu6050.MPU6050(i2c)

hostname = socket.gethostname()
hardware = 'plughw:2,0'

app = Flask(__name__)
socketio = SocketIO(app)

@socketio.on('connect')
def test_connect():
    print('connected')
    emit('after connect',  {'data':'Lets dance'})

@socketio.on('ping-accel')
def handle_message(val):
    # print(mpu.acceleration)
    # emit('pong-gps', mpu.acceleration)

    currAccel = mpu.acceleration

    # THRESHOLD DETECTION
    #if currAccel[0] > 2.00 and currAccel[1] > 2.00 and currAccel[2] > 2.00:
    if currAccel[0] > 5:
        print("Acceleration: X:%.2f, Y: %.2f, Z: %.2f m/s^2" % (currAccel))
        emit('pong-accel', currAccel)


@app.route('/')
def index():
    return render_template('index.html', hostname=hostname)

def signal_handler(sig, frame):
    print('Closing Gracefully')
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)


if __name__ == "__main__":
    socketio.run(app, host='0.0.0.0', port=5000)


