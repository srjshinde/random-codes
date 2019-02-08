#!/usr/bin/python

import spidev
import time
import os

# Open SPI bus
spi = spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz=1000000

# Function to read SPI data from MCP3008 chip
# Channel must be an integer 0-7

def ReadChannel(channel):
  adc = spi.xfer2([1,(8+channel)<<4,0])
  data = ((adc[1]&3) << 8) + adc[2]
  return data

mq2_channel = 0

# Define delay in seconds between readings
delay = 2

while True:

  # Read the light sensor data
  mq2_level = ReadChannel(mq2_channel)

  print mq2_level

  # Wait before repeating loop
  time.sleep(delay)

