"""code: dynamic xbee API mode parser
   author: suraj shinde
"""

import time
import serial

port=serial.Serial("/dev/ttyUSB0",9600,timeout=1.5)

while True:
  x=port.readline()
  x=x.encode("hex")
  #x="7e0016920013a20041085ebe690e01010818060818020f020d74"
  print x

  if "7e" in x and x[6:8] =="92":

	index=42
	address=x[8:24]
	print "address is:  ", address

	d_mask=x[32:36]
	d_value=x[38:42]
	bd_value=bin(int(d_value, 16))
	bd_mask=bin(int(d_mask, 16))
	print "digital mask: ", d_mask
	print "bin digital mask: ", bd_mask
	print "digital value mask: ", d_value

	a_mask=x[36:38]
	ba_mask=bin(int(a_mask, 16))
	print "analog mask: ", a_mask
	print "bin analog mask: ", ba_mask

	for i in range(0,16):

	  if int (bd_mask,2) & int( bin(2**i), 2) == 2**i:
		print "digital channel %d value: " % i, bin(int (bd_value,2) & int( bin(2**i), 2)) .count("1")

	if bd_mask.count("1") > 0:
        	index=42
       	else:
        	index=38

	for i in range(0,4):
		if int (ba_mask,2) & int( bin(2**i), 2) == 2**i:
	       		print "analog channel %d value: " % i, int(x[index:index+4], 16)
			index=index+4
	print "\n\n***************************************************************************\n\n"
