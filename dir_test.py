#!/usr/bin/python
import smbus
import math
import time

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

def read_word_2c(reg):
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

bus = smbus.SMBus(1) # bus = smbus.SMBus(0) fuer Revision 1
address = 0x68       # via i2cdetect

bus.write_byte_data(address, power_mgmt_1, 0)

while True:
    gyro_xout = read_word_2c(0x43)
    gyro_yout = read_word_2c(0x45)
    gyro_zout = read_word_2c(0x47)


    acc_xout = read_word_2c(0x3b)
    acc_yout = read_word_2c(0x3d)
    acc_zout = read_word_2c(0x3f)

    acc_xout_calib = acc_xout / 16384.0
    acc_yout_calib = acc_yout / 16384.0
    acc_zout_calib = acc_zout / 16384.0


    x_angle= get_x_rotation(acc_xout_calib, acc_yout_calib, acc_zout_calib)
    y_angle= get_y_rotation(acc_xout_calib, acc_yout_calib, acc_zout_calib)
    
    if x_angle >= 45:
        print "left"
    if x_angle < 45 and x_angle > -45 :
        print "........................"
    
    if x_angle < -45:
        print "right"
    
    if y_angle >= 45:
        print "reverse"
    if y_angle < 45 and y_angle > -45 :
        print "........................"
    
    if y_angle < -45:
        print "forward"
    
#   print "X: ", x_angle
#   print "Y: ", y_angle
#   print "\n\n"
    time.sleep(0.5)

