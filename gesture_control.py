#!/usr/bin/python
import smbus
import math
import time
from RPi import GPIO as g

l1=40
l2=38

r1=36
r2=32

g.setmode(g.BOARD)
g.setup(40,g.OUT)
g.setup(38,g.OUT)
g.setup(36,g.OUT)
g.setup(32,g.OUT)

# Register
power_mgmt_1 = 0x6b
power_mgmt_2 = 0x6c

def read_byte(reg):
    return bus.read_byte_data(address, reg)

def read_word(reg):
    h = bus.read_byte_data(address, reg)
    l = bus.read_byte_data(address, reg+1)
    value = (h << 8) + l
    return value

def read_word_i2c(reg):
    val = read_word(reg)
    if (val >= 0x8000):
        return -((65535 - val) + 1)
    else:
        return val

def dist(a,b):
    return math.sqrt((a*a)+(b*b))

def get_y_rotation(x,y,z):
    radians = math.atan2(x, dist(y,z))
    return -math.degrees(radians)

def get_x_rotation(x,y,z):
    radians = math.atan2(y, dist(x,z))
    return math.degrees(radians)

def go_straight():
    g.output(l1, True)
    g.output(l2, False)
    g.output(r1, True)
    g.output(r2, False)
    
def go_back():
    g.output(l1, False)
    g.output(l2, True)
    g.output(r1, False)
    g.output(r2, True)
    
def stay_put():
    g.output(l1, False)
    g.output(r1, False)
    g.output(l2, False)
    g.output(r2, False)

def turn_left():
    g.output(l1, True)
    g.output(l2, False)
    g.output(r1, False)  
    g.output(r2, False)
    
def turn_right():
    g.output(l1, False)
    g.output(l2, False)
    g.output(r1, True)
    g.output(r2, False)
    
bus = smbus.SMBus(1) #bus 1
address = 0x68       # ii2cdetect -y 1

bus.write_byte_data(address, power_mgmt_1, 0)

while True:
    gyro_xout = read_word_i2c(0x43)
    gyro_yout = read_word_i2c(0x45)
    gyro_zout = read_word_i2c(0x47)


    acc_xout = read_word_i2c(0x3b)
    acc_yout = read_word_i2c(0x3d)
    acc_zout = read_word_i2c(0x3f)

    acc_xout_calib = acc_xout / 16384.0
    acc_yout_calib = acc_yout / 16384.0
    acc_zout_calib = acc_zout / 16384.0


    x_angle= get_x_rotation(acc_xout_calib, acc_yout_calib, acc_zout_calib)
    y_angle= get_y_rotation(acc_xout_calib, acc_yout_calib, acc_zout_calib)
    
    if x_angle >= 45:
        turn_left()
        print "left"
        
    if x_angle < 45 and x_angle > -45 :
        stay_put()
        print "........................"
    
    if x_angle < -45:
        turn_right()
        print "right"
    
    if y_angle >= 45:
        go_back()
        print "reverse"
        
    if y_angle < 45 and y_angle > -45 :
        stay_put()
        print "........................"
    
    if y_angle < -45:
        go_straight()
        print "forward"
    
#   print "X: ", x_angle
#   print "Y: ", y_angle
#   print "\n\n"
    time.sleep(0.5)

