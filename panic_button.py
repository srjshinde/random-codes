from RPi import GPIO as g
import time
import serial

button = 40

gps=serial.Serial("/dev/serial0",9600,timeout=1)
gsm=serial.Serial("/dev/ttyUSB0",9600,timeout=1)

g.setmode(g.BOARD)
g.setup(button, g.IN, pull_up_down=g.PUD_DOWN)

x="gpsdata"
lat=00
lon=00

#while "NOT" in x or "READY" not in x:				#check for gsm to be ready
#	gsm.write("AT+CPIN=?\n")
#	print "waiting for gsm..."
#	time.sleep(1)

while "GPRMC" not in x and "A" not in x:			#check for gps to be
	x=gps.readline()
	print "searching for gps..."
	time.sleep(1)

print "GPS found"

def get_coordinates():								#naam hi kaafi hai...
	global lat, lon, x
	while "GPRMC" not in x:
		x=gps.readline()

	data=x.split(",")
	if data[0]=="$GPRMC" and data[2]=="A" :
		lat = int(data[3][0:2]) + float(data[3][2:])/60
		lon = int(data[5][0:3]) + float(data[5][3:])/60
	


def send_sms(latitude,longitude,number):			#sends SMS
	gsm.write("AT+CMGF=1"+"\n")
	time.sleep(1)
	gsm.write("AT+CMGS=\""+str(number)+"\""+"\n")
	time.sleep(1)
	gsm.write("***EMERGENCY***"+"\n")
	time.sleep(0.5)
	gsm.write("panic button pressed at location:"+"\n")
	time.sleep(0.5)
	gsm.write("www.google.com/maps/search/?api=1&query="+str(latitude)+","+str(longitude)+"\n")
	time.sleep(0.5)
	gsm.write("\x1A")
	time.sleep(1)
	print "SMS sent"

while True:

	if g.input(button) ==1:
		
		print "button pressed"

		get_coordinates()
		send_sms(lat,lon,number="9665916383")
		

		while g.input(button) ==1:
			time.sleep(1)
		
