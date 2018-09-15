import serial
import time

ser = serial.Serial(port='COM7',baudrate=9600,parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE,bytesize=serial.EIGHTBITS,timeout=1)

print("connected to: " + ser.portstr)

while True:
        x=ser.readline()
        print x,":::::","%r"%x
      
