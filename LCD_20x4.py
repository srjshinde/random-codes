#!/usr/bin/python

import RPi.GPIO as GPIO
import time
 
 
# Define some device constants
LCD_WIDTH = 20    # Maximum characters per line
LCD_CHR = True
LCD_CMD = False

 
# Timing constants
E_PULSE = 0.0005
E_DELAY = 0.0005



class LCD:  # Main program block
	 
	def __init__(self, LCD_E, LCD_RS, LCD_D4, LCD_D5, LCD_D6, LCD_D7):
		  
		self.LCD_E=LCD_E
		self.LCD_RS=LCD_RS
		self.LCD_D4=LCD_D4
		self.LCD_D5=LCD_D5
		self.LCD_D6=LCD_D6
		self.LCD_D7=LCD_D7
			
		#pin configuration  
		GPIO.setmode(GPIO.BOARD)       # Use BCM GPIO numbers
		GPIO.setwarnings(False)
		GPIO.setup(self.LCD_E, GPIO.OUT)  # E
		GPIO.setup(self.LCD_RS, GPIO.OUT) # RS
		GPIO.setup(self.LCD_D4, GPIO.OUT) # DB4
		GPIO.setup(self.LCD_D5, GPIO.OUT) # DB5
		GPIO.setup(self.LCD_D6, GPIO.OUT) # DB6
		GPIO.setup(self.LCD_D7, GPIO.OUT) # DB7
		
		
		#LCD initialisation
		self.lcd_byte(0x33,LCD_CMD) # 110011 Initialise
		self.lcd_byte(0x32,LCD_CMD) # 110010 Initialise
		self.lcd_byte(0x06,LCD_CMD) # 000110 Cursor move direction
		self.lcd_byte(0x0C,LCD_CMD) # 001100 Display On,Cursor Off, Blink Off
		self.lcd_byte(0x28,LCD_CMD) # 101000 Data length, number of lines, font size
		self.lcd_byte(0x01,LCD_CMD) # 000001 Clear display
		time.sleep(E_DELAY)

		
		
		
	def lcd_toggle_enable(self):
			
		# Toggle enable
		time.sleep(E_DELAY)
		GPIO.output(self.LCD_E, True)
		time.sleep(E_PULSE)
		GPIO.output(self.LCD_E, False)
		time.sleep(E_DELAY)
			
	def lcd_byte(self,bits, mode):
		# Send byte to data pins
		# bits = data
		# mode = True  for character
		# false for command
		
		self.bits=bits
		self.mode=mode
		
		GPIO.output(self.LCD_RS, self.mode) # RS
		 
		# High bits
		GPIO.output(self.LCD_D4, False)
		GPIO.output(self.LCD_D5, False)
		GPIO.output(self.LCD_D6, False)
		GPIO.output(self.LCD_D7, False)
		
		if self.bits&0x10==0x10:
			GPIO.output(self.LCD_D4, True)
		if self.bits&0x20==0x20:
			GPIO.output(self.LCD_D5, True)
		if self.bits&0x40==0x40:
			GPIO.output(self.LCD_D6, True)
		if self.bits&0x80==0x80:
			GPIO.output(self.LCD_D7, True)
		 
		# Toggle 'Enable' pin
		self.lcd_toggle_enable()
		 
		# Low bits
		GPIO.output(self.LCD_D4, False)
		GPIO.output(self.LCD_D5, False)
		GPIO.output(self.LCD_D6, False)
		GPIO.output(self.LCD_D7, False)
		if self.bits&0x01==0x01:
			GPIO.output(self.LCD_D4, True)
		if self.bits&0x02==0x02:
			GPIO.output(self.LCD_D5, True)
		if self.bits&0x04==0x04:
			GPIO.output(self.LCD_D6, True)
		if self.bits&0x08==0x08:
			GPIO.output(self.LCD_D7, True)
			

		# Toggle 'Enable' pin
		self.lcd_toggle_enable()
	  	

	 
	def lcd_string(self,message,line,style):
		
		#0x80 LCD RAM address for the 1st line
		#0xC0 LCD RAM address for the 2nd line
		#0x94 LCD RAM address for the 3rd line
		#0xD4 LCD RAM address for the 4th line
		
		
		# Send string to display
		# style=1 Left justified
		# style=2 Centred
		# style=3 Right justified
		self.message=message
		self.style=style
		
		if line==1:
			self.line=0x80
		elif line==2:
			self.line=0xC0
		elif line==3:
			self.line=0x94
		elif line==4:
			self.line=0xD4		
		  
		if self.style==1:
			self.message = self.message.ljust(LCD_WIDTH," ")
		elif style==2:
			self.message = self.message.center(LCD_WIDTH," ")
		elif style==3:
			self.message = self.message.rjust(LCD_WIDTH," ")
		 
		self.lcd_byte(self.line, LCD_CMD)
		 
		for i in range(LCD_WIDTH):
			self.lcd_byte(ord(self.message[i]),LCD_CHR)
			
		return 0


