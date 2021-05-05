from sense_hat import SenseHat
import time
from random import randint

#PROTOTYPING PHYSICAL INTERACTION PROJECT - ASSESSMENT 1

sense = SenseHat()
sense.set_imu_config(False, False, True) #Enables and disables the gyroscope, accelerometer and/or magnetometer 
x, y, z = sense.get_accelerometer_raw().values() #get x, y, z values from accelerometer
bird_y = 2
bar_x = 7
bar_y = 0
bar_free = randint(0,6)
playing = False
sense.clear()

def bird(bird_y):
    for i in range(2):
        sense.set_pixel(1,bird_y, (250, 238, 127))
        time.sleep(0.1)

def bar_scroll(bar_x, bar_free):
    for i in range(0,8):
        sense.set_pixel(bar_x, i, (100, 100, 100))
    sense.set_pixel(bar_x, bar_free, (0, 0, 0))
    sense.set_pixel(bar_x, bar_free+1, (0, 0, 0))
    time.sleep(0.3)
    
def game(x, y, z, bird_y, bar_x, bar_y, bar_free, playing):
    while playing == True:
        sense.clear()
        x, y, z = sense.get_accelerometer_raw().values()
        if x<0.06:
            sense.clear()
            x, y, z = sense.get_accelerometer_raw().values()
            bird(bird_y)
            if bird_y == 0:
              bird_y = 8
            bird_y = bird_y - 1
        if x>0.06:
            sense.clear()
            x, y, z = sense.get_accelerometer_raw().values()
            bird(bird_y)
            if bird_y == 7:
              bird_y = 0
            bird_y = bird_y + 1
        if bar_x == 2 and bird_y != bar_free and bird_y != bar_free+1:
            sense.clear()
            break
        bar_x = bar_x - 1
        bar_scroll(bar_x, bar_free)
        if bar_x == 0:
            bar_x = 8
            bar_free = randint(0,6)
    return False

while True:
    x, y, z = sense.get_accelerometer_raw().values()
    if y > 0.6 and x > 0.6 and z > 0.6:
        playing = True
    if playing == True:
        playing = game(x, y, z, bird_y, bar_x, bar_y, bar_free, playing)

